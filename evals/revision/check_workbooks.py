"""Verify source driver and formula retention with two spreadsheet engines."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import tempfile

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.workbook.properties import CalcProperties

from run import HERE, VARIANTS, common

OPENING_ROWS, OPENING_COLUMNS = 18, 8
HEADLINE = {'cash-review': ('ending cash', 'B12'), 'margin-review': ('gross profit', 'C17')}


def locked_content(sheet):
    return {cell.coordinate: cell.value for row in sheet for cell in row if cell.value is not None}


def visible_tab(sheet, rows=120, columns=24):
    result = {}
    hidden_columns = set()
    for dimension in sheet.column_dimensions.values():
        if dimension.hidden and dimension.min and dimension.max:
            hidden_columns.update(range(dimension.min, dimension.max + 1))
    for row in sheet.iter_rows(max_row=min(rows, sheet.max_row), max_col=min(columns, sheet.max_column)):
        if sheet.row_dimensions[row[0].row].hidden:
            continue
        cells = [(c.coordinate, c.value) for c in row
                 if c.column not in hidden_columns and not sheet.column_dimensions[get_column_letter(c.column)].hidden
                 and c.value is not None]
        if cells:
            result[row[0].row] = cells
    return result


def view(sheet, rows=120, columns=24):
    return f'[{sheet.title}]\n' + '\n'.join(' | '.join(f'{key}={value}' for key, value in row)
                                            for row in visible_tab(sheet, rows, columns).values())


def values(sheet, addresses):
    return {address: sheet[address].value for address in addresses}


def opening_headlines(sheet, label, base_value):
    matches = []
    for row in visible_tab(sheet).values():
        current_label = ''
        for address, value in row:
            if isinstance(value, str):
                current_label = value.lower()
            elif (value == base_value and label in current_label
                  and not re.search(r'\b(?:test|scenario|basis|change|may)\b', current_label)):
                matches.append(address)
    return matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--node', default='node')
    parser.add_argument('--node-modules', type=Path, required=True)
    parser.add_argument('--soffice', default='soffice')
    args = parser.parse_args()
    case_list = [case for case in json.loads((HERE / 'cases.json').read_text())
                 if case.get('source') == 'xlsx']
    out = args.out.resolve()
    repeats = json.loads((out / 'run.json').read_text())['repeats']
    subprocess.run([args.soffice, '--version'], check=True)
    checks = {}
    requests = []

    with tempfile.TemporaryDirectory(prefix='good-enough-revision-verify-') as directory:
        scratch = Path(directory)
        calculated = scratch / 'native'
        calculated.mkdir()
        native_cases = []
        for case in case_list:
            source_path = HERE / 'fixtures' / f'{case["id"]}.xlsx'
            source = load_workbook(source_path)
            input_name, build_name = case['input_sheet'], case['build_sheet']
            expected_base = {key: pair[0] for key, pair in case['outputs'].items()}
            expected_primary = {key: pair[1] for key, pair in case['outputs'].items()}
            expected_secondary = case['secondary_outputs']
            label, headline_output = HEADLINE[case['id']]
            for repeat, variant in [(0, 'source')] + [
                (i, v) for i in range(1, repeats + 1) for v in VARIANTS
            ]:
                identifier = f'{case["id"]}-{repeat}-{variant}'
                path = source_path if repeat == 0 else out / 'artifacts' / f'{identifier}.xlsx'
                book = load_workbook(path)
                cached = load_workbook(path, data_only=True)
                opening = cached.active
                if opening is None or opening.sheet_state != 'visible':
                    opening = next(sheet for sheet in cached if sheet.sheet_state == 'visible')
                headline_cells = opening_headlines(opening, label, expected_base[headline_output])
                required_tabs = input_name in book.sheetnames and build_name in book.sheetnames
                document = {
                    'opening_sheet': opening.title,
                    'opening_view': view(opening, OPENING_ROWS, OPENING_COLUMNS),
                    'full_view': '\n\n'.join(view(sheet) for sheet in cached if sheet.sheet_state == 'visible'),
                    'headline_cells': headline_cells,
                    'cached_outputs': values(cached[build_name], case['outputs']) if required_tabs else {},
                    'checks': {
                        'expected_tabs': required_tabs,
                        'drivers_retained': required_tabs and all(
                            book[input_name][key].value == value
                            for key, value in locked_content(source[input_name]).items()
                        ),
                        'schedule_retained': required_tabs and all(
                            book[build_name][key].value == value
                            for key, value in locked_content(source[build_name]).items()
                        ),
                        'saved_outputs': required_tabs and values(cached[build_name], case['outputs']) == expected_base,
                        'no_saved_formula_errors': not any(cell.data_type == 'e'
                                                           for sheet in cached for row in sheet for cell in row),
                        'artifact_tool_base_and_edits': False,
                        'libreoffice_primary_and_secondary_edits': False,
                        'published_headline_recalculates': not headline_cells,
                    }
                }
                checks[identifier] = document
                if not required_tabs:
                    continue
                requests.append({'identifier': identifier, 'file': str(path), 'opening_sheet': opening.title,
                                 'headline_cells': headline_cells, **{k: case[k] for k in
                                     ('input_sheet', 'build_sheet', 'edit', 'outputs', 'secondary_edit')}})
                edits = [('primary', case['edit'], expected_primary), ('secondary', case['secondary_edit'], expected_secondary)]
                for scenario, changes, expected in edits:
                    copy = load_workbook(path)
                    for address, value in changes.items():
                        copy[input_name][address] = value
                    if copy.calculation is None:
                        copy.calculation = CalcProperties()
                    copy.calculation.fullCalcOnLoad = True
                    copy.calculation.forceFullCalc = True
                    disposable = scratch / f'{identifier}-{scenario}.xlsx'
                    copy.save(disposable)
                    native_cases.append((identifier, scenario, build_name, expected, disposable))

        requests_file, results_file = scratch / 'requests.json', scratch / 'results.json'
        common.dump(requests_file, requests)
        subprocess.run([args.node, str(HERE / 'workbook_recalc.mjs'), str(args.node_modules.resolve()),
                        str(requests_file), str(results_file), str(out / 'previews')],
                       check=True, timeout=120)
        tool_results = json.loads(results_file.read_text())
        native_run = subprocess.run(
            [args.soffice, f'-env:UserInstallation={scratch.as_uri()}/profile', '--headless',
             '--convert-to', 'xlsx', '--outdir', str(calculated), *(str(item[4]) for item in native_cases)],
            capture_output=True, text=True, timeout=90,
        )
        if native_run.returncode:
            raise RuntimeError(f'LibreOffice exit {native_run.returncode}: {native_run.stderr[-1000:]}')

        for identifier, scenario, name, expected, disposable in native_cases:
            native = load_workbook(calculated / disposable.name, data_only=True)
            checks[identifier].setdefault('libreoffice', {})[scenario] = values(native[name], expected)
        for request in requests:
            identifier = request['identifier']
            current = checks[identifier]
            case = next(case for case in case_list if identifier.startswith(case['id'] + '-'))
            expected_base = {key: pair[0] for key, pair in case['outputs'].items()}
            expected_primary = {key: pair[1] for key, pair in case['outputs'].items()}
            expected_secondary = case['secondary_outputs']
            result = tool_results[identifier]
            native = current['libreoffice']
            current['artifact_tool'] = result
            current['checks']['artifact_tool_base_and_edits'] = (
                result.get('base') == expected_base and result.get('primary') == expected_primary
                and result.get('secondary') == expected_secondary
            )
            current['checks']['libreoffice_primary_and_secondary_edits'] = (
                native['primary'] == expected_primary and native['secondary'] == expected_secondary
            )
            headline_output = HEADLINE[case['id']][1]
            if current['headline_cells']:
                current['checks']['published_headline_recalculates'] = (
                    result.get('headline_after') == dict.fromkeys(current['headline_cells'], expected_primary[headline_output])
                )
            print(identifier, 'pass' if all(current['checks'].values()) else current['checks'], flush=True)

    common.dump(out / 'workbook-checks.json', checks)


if __name__ == '__main__':
    main()
