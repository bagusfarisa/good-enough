"""Test whether a model reader can explain cash results using visible workbook cells."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from hashlib import sha256
import json
from pathlib import Path
import random
import re
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'automated'))
from run import cli, dump, schema_object

QUESTION_FILE = HERE / 'reader-questions.json'
QUESTIONS = json.loads(QUESTION_FILE.read_text())
MODEL = 'gpt-6.1-terra'


def score_answers(record, answers):
    cells = {f'{sheet}!{address}': value for sheet, rows in record['visible'].items()
             for row in rows for address, value in row.items()}
    for question in QUESTIONS:
        item = answers[question['id']]
        evidence = list(dict.fromkeys(item['evidence']))
        cited = [address for address in evidence if address in cells]
        invalid = [address for address in evidence if address not in cells
                   and re.fullmatch(r'.+!\$?[A-Z]+\$?\d+', address)]
        amounts = Counter(abs(cells[address]) for address in cited if isinstance(cells[address], (int, float)))
        expected = question['expected']
        correct = all(item['answer'][name] == value if isinstance(value, int)
                      else value.casefold() in str(item['answer'][name]).casefold()
                      for name, value in expected.items())
        item['correct'] = correct
        item['verified_cells'] = cited
        item['supported'] = correct and bool(cited) and not invalid and amounts >= Counter(question['evidence_amounts'])


def grade(record, output):
    key = f'{record["pair"]:02}-{record["variant"]}'
    path = output / f'{key}.json'
    if path.is_file():
        result = json.loads(path.read_text())
        score_answers(record, result['answers'])
        dump(path, result)
        return result
    schema = {}
    prompts = {}
    for question in QUESTIONS:
        fields = schema_object(**{name: {'type': ['integer' if isinstance(value, int) else 'string', 'null']}
                                 for name, value in question['expected'].items()})
        schema[question['id']] = schema_object(answer=fields, evidence={'type': 'array', 'items': {'type': 'string'}})
        prompts[question['id']] = question['question']
    instructions = ('You are reviewing a workbook. You have the values of visible cells, grouped by sheet and row. '
                    'Use only these labels and values and arithmetic you can explain from them. '
                    'For each answer, cite the unique cell addresses needed to support all figures. '
                    'Use the exact notation Sheet name!A1. Use null for any value you cannot determine. '
                    'Do not use tools.')
    response, _ = cli(instructions + '\n\n' + json.dumps({'questions': prompts, 'visible_cells': record['visible']},
                                                            ensure_ascii=False), MODEL, schema_object(**schema))
    answers = json.loads(response)
    score_answers(record, answers)
    result = {k: record[k] for k in ('pair', 'variant', 'workbook')}
    result['answers'] = answers
    dump(path, result)
    print(key, sum(item['supported'] for item in answers.values()), 'of', len(QUESTIONS), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--values', type=Path, default=HERE / 'visible-values.json')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    values_bytes = args.values.read_bytes()
    configuration = {'values_sha256': sha256(values_bytes).hexdigest(),
                     'questions_sha256': sha256(QUESTION_FILE.read_bytes()).hexdigest(), 'model': MODEL}
    manifest = args.out / 'reader-config.json'
    if manifest.is_file() and json.loads(manifest.read_text()) != configuration:
        raise ValueError('Use a fresh output directory for different inputs.')
    dump(manifest, configuration)
    values = json.loads(values_bytes)
    runs = values['runs']
    random.Random(421).shuffle(runs)
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(partial(grade, output=args.out), runs))
    dump(args.out / 'reader-scores.json', {**configuration, 'skill_commit': values['skill_commit'],
                                          'previous_skill_commit': values['previous_skill_commit'], 'runs': results})


if __name__ == '__main__':
    main()
