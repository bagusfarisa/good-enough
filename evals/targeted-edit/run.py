"""Deterministic guardrail evaluation for targeted edits.

Tests Rule 1 of good-enough/SKILL.md:
'For a targeted edit, reuse the existing structure and change only what was
requested and what depends on it.'
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
from difflib import SequenceMatcher
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import random
import re
from statistics import median
import subprocess


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CASE_FILE = HERE / 'cases.json'
VARIANTS = ('baseline', 'good-enough')

_AUTO_SPEC = importlib.util.spec_from_file_location('automated_run', HERE.parent / 'automated' / 'run.py')
_AUTO = importlib.util.module_from_spec(_AUTO_SPEC)
_AUTO_SPEC.loader.exec_module(_AUTO)


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def load_skill_text(revision):
    if revision == 'WORKTREE':
        return (REPO / 'skills' / 'good-enough' / 'SKILL.md').read_text()
    return subprocess.check_output(
        ['git', '-C', str(REPO), 'show', f'{revision}:skills/good-enough/SKILL.md'],
        text=True,
    )


def changed_ratio(source, revised):
    """Fraction of text changed based on word-level SequenceMatcher ratio."""
    src_tokens = source.split()
    rev_tokens = revised.split()
    similarity = SequenceMatcher(None, src_tokens, rev_tokens).ratio()
    return round(1.0 - similarity, 4)


def score_artifact(source, revised, case):
    missing_required = [
        pattern for pattern in case.get('required_substrings', [])
        if not re.search(pattern, revised, re.IGNORECASE)
    ]
    present_forbidden = [
        pattern for pattern in case.get('forbidden_substrings', [])
        if re.search(pattern, revised, re.IGNORECASE)
    ]
    occurrence_failures = {}
    for pattern, minimum in case.get('min_occurrences', {}).items():
        count = len(re.findall(pattern, revised, re.IGNORECASE))
        if count < minimum:
            occurrence_failures[pattern] = {'expected_min': minimum, 'found': count}

    revised_lines = {line.strip() for line in revised.splitlines()}
    missing_headings = [
        heading for heading in case.get('required_headings', [])
        if heading not in revised_lines
    ]
    diff_ratio = changed_ratio(source, revised)
    max_ratio = case.get('max_changed_ratio', 0.25)

    checks = {
        'required_updates': not missing_required and not occurrence_failures,
        'no_stale_values': not present_forbidden,
        'headings_preserved': not missing_headings,
        'scope_discipline': diff_ratio <= max_ratio,
    }
    return {
        'passed': all(checks.values()),
        'checks': checks,
        'changed_ratio': diff_ratio,
        'max_changed_ratio': max_ratio,
        'missing_required': missing_required,
        'occurrence_failures': occurrence_failures,
        'present_forbidden': present_forbidden,
        'missing_headings': missing_headings,
    }


def generate(output, cases, revision, *, baseline_revision=None,
             generator=_AUTO.GENERATOR, repeats=3, reasoning_effort='low', workers=4):
    revisions = {'baseline': baseline_revision, 'good-enough': revision}
    skills = {variant: load_skill_text(rev) for variant, rev in revisions.items() if rev}
    jobs = [(case, repeat, variant) for repeat in range(1, repeats + 1)
            for case in cases for variant in VARIANTS]
    random.Random(314).shuffle(jobs)

    def run_job(job):
        case, repeat, variant = job
        name = f'{case["id"]}-{repeat}-{variant}'
        path = output / 'artifacts' / f'{name}.md'
        usage_path = path.with_suffix('.json')
        if path.is_file() and usage_path.is_file():
            return
        source = (HERE / case['fixture']).read_text()
        skill = skills.get(variant)
        guidance = f'Apply the following skill instructions.\n\n<skill>\n{skill}\n</skill>\n\n' if skill else ''
        prompt = (
            guidance
            + 'Return the updated Markdown document as your final response. '
            + 'Complete this self-contained exercise using the supplied document without tools.\n\n'
            + f'{case["task"]}\n\n<document>\n{source}\n</document>'
        )
        artifact, usage = _AUTO.cli(prompt, generator, reasoning_effort=reasoning_effort)
        path.write_text(_AUTO.artifact_only(artifact) + '\n')
        dump(usage_path, {'usage': usage})
        print('generated', name, flush=True)

    (output / 'artifacts').mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(run_job, jobs))


def grade(output, cases, configuration, *, repeats=3):
    runs = []
    for case in cases:
        source = (HERE / case['fixture']).read_text()
        for repeat in range(1, repeats + 1):
            for variant in VARIANTS:
                name = f'{case["id"]}-{repeat}-{variant}'
                revised = (output / 'artifacts' / f'{name}.md').read_text()
                usage_data = json.loads((output / 'artifacts' / f'{name}.json').read_text())
                result = score_artifact(source, revised, case)
                runs.append({
                    'case': case['id'],
                    'repeat': repeat,
                    'variant': variant,
                    'artifact': f'artifacts/{name}.md',
                    **result,
                    **usage_data,
                })

    case_ids = [case['id'] for case in cases]
    summary = {}
    for variant in VARIANTS:
        condition = [run for run in runs if run['variant'] == variant]
        by_case = {cid: [run['passed'] for run in condition if run['case'] == cid] for cid in case_ids}
        pass_all_k = sum(bool(flags) and all(flags) for flags in by_case.values())
        pass_at_k = sum(any(flags) for flags in by_case.values())
        summary[variant] = {
            'documents_passing': sum(run['passed'] for run in condition),
            'documents': len(condition),
            'cases_pass_all_k': pass_all_k,
            'cases_pass_at_k': pass_at_k,
            'cases': len(case_ids),
            'pass_all_k_rate': round(pass_all_k / len(case_ids), 4),
            'pass_at_k_rate': round(pass_at_k / len(case_ids), 4),
            'headings_preserved': sum(run['checks']['headings_preserved'] for run in condition),
            'scope_discipline': sum(run['checks']['scope_discipline'] for run in condition),
            'median_changed_ratio': round(median(run['changed_ratio'] for run in condition), 4),
            **_AUTO.summarize_usage(condition),
        }

    report = {
        **configuration,
        'harness': subprocess.check_output(['codex', '--version'], text=True).strip(),
        'summary': summary,
        'runs': runs,
    }
    dump(output / 'scores.json', report)
    print(json.dumps(summary, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, help='Output directory for artifacts and scores')
    parser.add_argument('--revision', default='HEAD', help='Commit with SKILL.md, or WORKTREE')
    parser.add_argument('--baseline-revision', help='Optional skill commit for baseline')
    parser.add_argument('--cases', type=Path, default=CASE_FILE, help='Path to targeted-edit cases JSON')
    parser.add_argument('--generator', default=_AUTO.GENERATOR, help='Model used to generate edits')
    parser.add_argument('--reasoning-effort', default='low', help='Codex model_reasoning_effort value')
    parser.add_argument('--repeats', type=int, default=3, help='Trials (k) per case and variant')
    parser.add_argument('--stage', choices=['generate', 'grade', 'all'], default='all')
    parser.add_argument('--dry-run', action='store_true', help='Validate fixtures and scoring logic without calling Codex')
    args = parser.parse_args()

    if args.repeats < 1:
        parser.error('--repeats must be positive')
    case_bytes = args.cases.read_bytes()
    cases = json.loads(case_bytes)
    if not cases:
        parser.error('--cases must contain at least one case')

    if args.dry_run:
        checks = []
        for case in cases:
            source = (HERE / case['fixture']).read_text()
            unchanged_score = score_artifact(source, source, case)
            checks.append({
                'id': case['id'],
                'fixture_exists': True,
                'unchanged_has_headings': unchanged_score['checks']['headings_preserved'],
                'unchanged_fails_update': not unchanged_score['checks']['required_updates'],
            })
        print(json.dumps({'cases': len(cases), 'sanity_checks': checks}, indent=2))
        return

    if not args.out:
        parser.error('--out is required unless --dry-run is set')
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    revision = (
        'WORKTREE' if args.revision == 'WORKTREE'
        else subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', args.revision], text=True).strip()
    )
    baseline_revision = None
    if args.baseline_revision:
        baseline_revision = (
            'WORKTREE' if args.baseline_revision == 'WORKTREE'
            else subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', args.baseline_revision], text=True).strip()
        )
    manifest = output / 'run.json'
    config = {
        'skill_commit': revision,
        'generator': args.generator,
        'reasoning_effort': args.reasoning_effort,
        'repeats': args.repeats,
        'cases_sha256': sha256(case_bytes).hexdigest(),
    }
    if baseline_revision:
        config['baseline_skill_commit'] = baseline_revision
    if manifest.exists() and json.loads(manifest.read_text()) != config:
        raise ValueError('Use a fresh output directory for a different evaluation configuration.')
    dump(manifest, config)

    if args.stage in ('generate', 'all'):
        generate(output, cases, revision, baseline_revision=baseline_revision,
                 generator=args.generator, repeats=args.repeats, reasoning_effort=args.reasoning_effort)
    if args.stage in ('grade', 'all'):
        grade(output, cases, config, repeats=args.repeats)


if __name__ == '__main__':
    main()
