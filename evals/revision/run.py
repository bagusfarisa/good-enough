"""Generate three revisions of each fixture in isolated Codex CLI sessions."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import random
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('document_eval', HERE.parent / 'automated' / 'run.py')
common = importlib.util.module_from_spec(spec)
spec.loader.exec_module(common)

VARIANTS = ('plain', 'concise', 'good-enough')
REPEATS = 2
CONCISE = 'Make it concise and actionable.'
RUNTIME = (
    'Use source.xlsx as the source workbook. The current folder is writable. '
    'Use Node.js and the provided @oai/artifact-tool library to edit it. '
    'Read spreadsheet-api.md as needed. Verify the workbook and save revision.xlsx. '
    'Work only with files in this exercise.'
)


def generate(case, repeat, variant, output, skill, api, modules):
    identifier = f'{case["id"]}-{repeat}-{variant}'
    extension = 'xlsx' if case.get('source') == 'xlsx' else 'md'
    artifact = output / 'artifacts' / f'{identifier}.{extension}'
    metadata = output / 'runs' / f'{identifier}.json'
    if artifact.exists() and metadata.exists():
        return
    source = HERE / 'fixtures' / f'{case["id"]}.{extension}'
    guidance = CONCISE + '\n\n' if variant == 'concise' else ''
    if variant == 'good-enough':
        guidance = f'Apply the following skill instructions.\n\n<skill>\n{skill}\n</skill>\n\n'
    task = guidance + case['task']
    if extension == 'md':
        prompt = (task + '\nReturn only the finished artifact. Do not use tools.\n\n'
                  '<source>\n' + source.read_text() + '\n</source>')
        response, usage = common.cli(prompt, common.GENERATOR)
        artifact.write_text(common.artifact_only(response) + '\n')
    else:
        with tempfile.TemporaryDirectory(prefix='good-enough-revision-') as directory:
            root = Path(directory)
            shutil.copyfile(source, root / 'source.xlsx')
            shutil.copyfile(api, root / 'spreadsheet-api.md')
            (root / 'node_modules').symlink_to(modules, target_is_directory=True)
            command = [
                'codex', '--ask-for-approval', 'never', 'exec', '-m', common.GENERATOR,
                '-c', 'model_reasoning_effort="low"',
                '-c', 'skills.config=[{name="artifact-ponytail",enabled=false},{name="good-enough",enabled=false}]',
                '--disable', 'memories', '--ignore-user-config', '--ignore-rules',
                '--ephemeral', '--skip-git-repo-check', '--sandbox', 'workspace-write',
                '--json', '-C', str(root), '-',
            ]
            result = subprocess.run(command, input=task + '\n\n' + RUNTIME, cwd=root,
                                    capture_output=True, text=True, timeout=360)
            book = root / 'revision.xlsx'
            if result.returncode or not book.is_file():
                raise RuntimeError(f'{identifier}: missing revision, exit {result.returncode}')
            events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
            usage = next((event.get('usage') for event in reversed(events)
                          if event.get('type') == 'turn.completed'), None)
            shutil.copyfile(book, artifact)
    common.dump(metadata, {'case': case['id'], 'repeat': repeat, 'variant': variant,
                           'artifact': f'artifacts/{artifact.name}', 'usage': usage})
    print('generated', identifier, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--revision', default='HEAD')
    parser.add_argument('--format', choices=['all', 'md', 'xlsx'], default='all')
    parser.add_argument('--api', type=Path)
    parser.add_argument('--node-modules', type=Path)
    args = parser.parse_args()
    cases_path = HERE / 'cases.json'
    cases = json.loads(cases_path.read_text())
    revision = subprocess.check_output(['git', 'rev-parse', args.revision], cwd=HERE, text=True).strip()
    skill = subprocess.check_output(['git', 'show', f'{revision}:skills/good-enough/SKILL.md'],
                                    cwd=HERE, text=True)
    out = args.out.resolve()
    (out / 'artifacts').mkdir(parents=True, exist_ok=True)
    (out / 'runs').mkdir(exist_ok=True)
    manifest = {'skill_commit': revision, 'harness': subprocess.check_output(['codex', '--version'], text=True).strip(),
                'generator': common.GENERATOR, 'reasoning': 'low', 'repeats': REPEATS,
                'concise_instruction': CONCISE, 'reader_source': 'revised artifact only',
                'cases_sha256': sha256(cases_path.read_bytes()).hexdigest()}
    config = out / 'run.json'
    if config.exists() and json.loads(config.read_text()) != manifest:
        parser.error('Use a new --out directory for a different revision or fixture set.')
    common.dump(config, manifest)
    jobs = []
    for case in cases:
        extension = case.get('source', 'md')
        if args.format not in ('all', extension):
            continue
        if extension == 'xlsx' and (args.api is None or args.node_modules is None):
            parser.error('Workbook trials require --api and --node-modules.')
        jobs.extend((case, repeat, variant, out, skill, args.api, args.node_modules)
                    for repeat in range(1, REPEATS + 1) for variant in VARIANTS)
    random.Random(284).shuffle(jobs)
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda job: generate(*job), jobs))


if __name__ == '__main__':
    main()
