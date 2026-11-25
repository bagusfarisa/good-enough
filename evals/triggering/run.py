"""Evaluate whether an agent discovers and loads the good-enough skill appropriately."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CASE_FILE = HERE / 'cases.json'
DEFAULT_MODEL = 'gpt-6.2-sol'
SKILL_PATTERN = re.compile(r'good-enough[/\\]SKILL\.md|\bgood-enough\b', re.IGNORECASE)


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def load_skill_text(revision):
    if revision == 'WORKTREE':
        return (REPO / 'skills' / 'good-enough' / 'SKILL.md').read_text()
    return subprocess.check_output(
        ['git', '-C', str(REPO), 'show', f'{revision}:skills/good-enough/SKILL.md'],
        text=True,
    )


def detect_skill_trigger(events):
    """Inspect Codex JSONL events for evidence that good-enough/SKILL.md was actually read."""
    evidence = []
    for event in events:
        event_type = str(event.get('type', ''))
        item = event.get('item') if isinstance(event.get('item'), dict) else None
        if item:
            # Check command/tool invocation targets, NOT aggregated_output (which can match `find`/`rg --files`).
            command = str(item.get('command', ''))
            if 'good-enough' in command and 'SKILL.md' in command:
                evidence.append({'type': event_type, 'item_type': item.get('type'), 'command': command})
                continue
            target_fields = json.dumps(
                {k: v for k, v in item.items() if k in ('path', 'arguments', 'tool', 'name', 'skill')},
                ensure_ascii=False,
            )
            if 'good-enough' in target_fields and 'SKILL.md' in target_fields:
                evidence.append({'type': event_type, 'item_type': item.get('type'), 'match': 'tool_target'})
                continue
        if 'skill' in event_type.lower() and SKILL_PATTERN.search(json.dumps(event, ensure_ascii=False)):
            evidence.append({'type': event_type, 'match': 'skill_event'})
    return bool(evidence), evidence


def run_probe(prompt, skill_text, model, reasoning_effort):
    with tempfile.TemporaryDirectory(prefix='good-enough-trigger-') as directory:
        workspace = Path(directory)
        skill_dir = workspace / '.agents' / 'skills' / 'good-enough'
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / 'SKILL.md').write_text(skill_text)
        answer = workspace / 'answer.txt'
        command = [
            'codex', '--ask-for-approval', 'never', 'exec', '--model', model,
            '-c', f'model_reasoning_effort="{reasoning_effort}"',
            '-c', 'skills.config=[{name="artifact-ponytail",enabled=false}]',
            '--disable', 'memories', '--ignore-user-config', '--ignore-rules',
            '--ephemeral', '--skip-git-repo-check', '--sandbox', 'read-only',
            '--json', '--output-last-message', str(answer), '-C', str(workspace),
        ]
        wrapped = (
            f'{prompt}\n\n'
            'Briefly state your plan in 2-3 bullet points without creating files.'
        )
        result = subprocess.run(command + ['-'], input=wrapped, text=True,
                                capture_output=True, cwd=workspace, timeout=180)
        if result.returncode:
            raise RuntimeError(f'{model} returned CLI exit {result.returncode}: {result.stderr[-700:]}')
        events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
        usage = next((event.get('usage') for event in reversed(events)
                      if event.get('type') == 'turn.completed'), None)
        triggered, evidence = detect_skill_trigger(events)
        return {
            'triggered': triggered,
            'evidence': evidence,
            'usage': usage,
            'response': answer.read_text().strip() if answer.is_file() else '',
        }


def compute_metrics(runs):
    tp = sum(r['should_trigger'] and r['triggered'] for r in runs)
    fp = sum((not r['should_trigger']) and r['triggered'] for r in runs)
    tn = sum((not r['should_trigger']) and (not r['triggered']) for r in runs)
    fn = sum(r['should_trigger'] and (not r['triggered']) for r in runs)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
    accuracy = (tp + tn) / len(runs) if runs else 0.0
    return {
        'total_trials': len(runs),
        'tp': tp,
        'fp': fp,
        'tn': tn,
        'fn': fn,
        'precision': round(precision, 4),
        'recall': round(recall, 4),
        'f1': round(f1, 4),
        'accuracy': round(accuracy, 4),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, help='Output directory for traces and scores')
    parser.add_argument('--revision', default='HEAD',
                        help='Git commit containing skills/good-enough/SKILL.md, or WORKTREE for uncommitted file')
    parser.add_argument('--cases', type=Path, default=CASE_FILE, help='Path to triggering cases JSON')
    parser.add_argument('--model', default=DEFAULT_MODEL, help='Model to test for skill discovery')
    parser.add_argument('--reasoning-effort', default='low', help='Codex model_reasoning_effort value')
    parser.add_argument('--repeats', type=int, default=1, help='Trials (k) per case')
    parser.add_argument('--workers', type=int, default=4, help='Parallel Codex workers')
    parser.add_argument('--dry-run', action='store_true', help='Validate cases and print dataset stats without running Codex')
    args = parser.parse_args()

    if args.repeats < 1:
        parser.error('--repeats must be positive')
    case_bytes = args.cases.read_bytes()
    cases = json.loads(case_bytes)
    if not cases:
        parser.error('--cases must contain at least one case')

    positives = sum(1 for c in cases if c['should_trigger'])
    negatives = len(cases) - positives
    if args.dry_run:
        skill_text = load_skill_text(args.revision)
        print(json.dumps({
            'cases': len(cases),
            'positives': positives,
            'negatives': negatives,
            'repeats': args.repeats,
            'total_trials': len(cases) * args.repeats,
            'revision': args.revision,
            'skill_chars': len(skill_text),
        }, indent=2))
        return

    if not args.out:
        parser.error('--out is required unless --dry-run is set')
    output = args.out.resolve()
    (output / 'trials').mkdir(parents=True, exist_ok=True)
    skill_text = load_skill_text(args.revision)
    resolved_rev = (
        'WORKTREE' if args.revision == 'WORKTREE'
        else subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', args.revision], text=True).strip()
    )

    jobs = [(case, repeat) for repeat in range(1, args.repeats + 1) for case in cases]

    def execute(job):
        case, repeat = job
        trial_path = output / 'trials' / f'{case["id"]}-{repeat}.json'
        if trial_path.is_file():
            return json.loads(trial_path.read_text())
        probe = run_probe(case['prompt'], skill_text, args.model, args.reasoning_effort)
        record = {
            'id': case['id'],
            'category': case['category'],
            'repeat': repeat,
            'should_trigger': case['should_trigger'],
            'triggered': probe['triggered'],
            'correct': probe['triggered'] == case['should_trigger'],
            'evidence': probe['evidence'],
            'usage': probe['usage'],
            'response': probe['response'],
        }
        dump(trial_path, record)
        status = 'OK' if record['correct'] else ('FP' if record['triggered'] else 'FN')
        print(f'{status:2s} {case["id"]} #{repeat} (expected={case["should_trigger"]}, triggered={record["triggered"]})',
              flush=True)
        return record

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        runs = list(pool.map(execute, jobs))

    by_case = {case['id']: [r['correct'] for r in runs if r['id'] == case['id']] for case in cases}
    pass_all_k = sum(all(flags) for flags in by_case.values())
    metrics = {
        **compute_metrics(runs),
        'cases': len(cases),
        'cases_pass_all_k': pass_all_k,
        'pass_all_k_rate': round(pass_all_k / len(cases), 4),
    }
    report = {
        'skill_commit': resolved_rev,
        'model': args.model,
        'reasoning_effort': args.reasoning_effort,
        'repeats': args.repeats,
        'cases_sha256': sha256(case_bytes).hexdigest(),
        'harness': subprocess.check_output(['codex', '--version'], text=True).strip(),
        'metrics': metrics,
        'false_positives': [r['id'] for r in runs if (not r['should_trigger']) and r['triggered']],
        'false_negatives': [r['id'] for r in runs if r['should_trigger'] and (not r['triggered'])],
        'runs': runs,
    }
    dump(output / 'scores.json', report)
    print(json.dumps(metrics, indent=2))


if __name__ == '__main__':
    main()
