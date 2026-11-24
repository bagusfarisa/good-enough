// Build the two synthetic source workbooks and render them for inspection.
import fs from 'node:fs/promises';
import { createRequire } from 'node:module';
import { join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const [modules, previewDirectory] = process.argv.slice(2);
const require = createRequire(join(resolve(modules), '..', 'resolve-artifact-tool.cjs'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(require.resolve('@oai/artifact-tool')));
const fixtures = new URL('./fixtures/', import.meta.url);
const currency = '"$"#,##0;("$"#,##0);"-"';

function makeSheet(book, name, color) {
  const sheet = book.worksheets.add(name);
  sheet.showGridLines = false;
  sheet.tabColor = color;
  sheet.getRange('A:A').format.columnWidth = 33;
  sheet.getRange('B:C').format.columnWidth = 19;
  sheet.getRange('A1:C24').format.font.name = 'Arial';
  sheet.getRange('A1:C24').format.font.size = 10;
  return sheet;
}

function title(sheet, text) {
  sheet.getRange('A2').values = [[text]];
  sheet.getRange('A2').format.font.bold = true;
  sheet.getRange('A2').format.font.size = 14;
}

function header(sheet, row, periods) {
  sheet.getRange(`A${row}:C${row}`).values = [['Line item', ...periods]];
  sheet.getRange(`A${row}:C${row}`).format.fill = '#DDE6F2';
  sheet.getRange(`A${row}:C${row}`).format.font.bold = true;
}

function notes(sheet, rows) {
  for (const [row, text] of rows) sheet.getRange(`A${row}`).values = [[text]];
}

function sourcesAndBuild(book, driverName, buildName, periods) {
  const inputs = makeSheet(book, driverName, '#7194B8');
  const build = makeSheet(book, buildName, '#9CA8B7');
  title(inputs, 'Editable assumptions');
  title(build, 'Monthly calculation');
  header(inputs, 4, periods);
  header(build, 4, periods);
  return [inputs, build];
}

function linkedBuild(build, firstRow, labels, formulas) {
  build.getRange(`A${firstRow}:A${firstRow + labels.length - 1}`).values = labels.map(label => [label]);
  build.getRange(`B${firstRow}:C${firstRow + labels.length - 1}`).formulas = formulas;
  build.getRange(`A${firstRow + labels.length - 1}:C${firstRow + labels.length - 1}`).format.font.bold = true;
}

const cash = Workbook.create();
const cashCover = makeSheet(cash, 'Review notes', '#365679');
title(cashCover, 'Forecast review packet');
notes(cashCover, [
  [4, 'Monthly cash planning workbook for internal review.'],
  [6, 'Workbook overview'],
  [7, 'The forecast review packet has three tabs.'],
  [8, 'Monthly inputs are stored in Drivers.'],
  [9, 'The working schedule is in Build.'],
  [11, 'Review sequence'],
  [12, 'Review dates, assumptions and totals before sharing.'],
  [13, 'Use the planning workbook when reviewing cash.'],
  [15, 'Version notes'],
  [16, 'The forecast uses US dollars. April and May are forecasts.'],
  [19, 'End of cover notes. Continue to the working sheets.'],
]);
const [drivers, cashBuild] = sourcesAndBuild(cash, 'Drivers', 'Build', ['April 2027', 'May 2027']);
drivers.getRange('A5:C9').values = [
  ['Customer collections', 24000, 20000],
  ['Payroll', 15000, 11000],
  ['Rent', 4000, 4000],
  ['Equipment', 3000, 1000],
  ['Opening cash at start of April', 11000, null],
];
drivers.getRange('B5:C9').setNumberFormat(currency);
drivers.getRange('B5:C9').format.font.color = '#245CA6';
linkedBuild(cashBuild, 5, ['Opening cash', 'Customer collections', 'Payroll', 'Rent', 'Equipment',
  'Total payments', 'Net cash change', 'Ending cash'], [
  ['=Drivers!B9', '=B12'],
  ['=Drivers!B5', '=Drivers!C5'],
  ['=-Drivers!B6', '=-Drivers!C6'],
  ['=-Drivers!B7', '=-Drivers!C7'],
  ['=-Drivers!B8', '=-Drivers!C8'],
  ['=SUM(B7:B9)', '=SUM(C7:C9)'],
  ['=B6+B10', '=C6+C10'],
  ['=B5+B11', '=C5+C11'],
]);
cashBuild.getRange('B5:C12').setNumberFormat(currency);
cashCover.getRange('B23').formulas = [['=Build!B12']];
cashCover.getRange('A23').values = [['April ending cash']];
cashCover.getRange('B23').setNumberFormat(currency);

const margin = Workbook.create();
const marginCover = makeSheet(margin, 'Reporting guide', '#365679');
title(marginCover, 'Product reporting packet');
notes(marginCover, [
  [4, 'Prepared for the monthly finance review.'],
  [6, 'Scope'],
  [7, 'The model covers one product in May and June.'],
  [8, 'Assumptions and calculations are stored separately.'],
  [9, 'Amounts are in US dollars.'],
  [11, 'Review process'],
  [12, 'Read the notes and scan each tab.'],
  [13, 'Inputs holds the monthly assumptions.'],
  [14, 'Calculation holds the monthly formula schedule.'],
  [17, 'Report handoff'],
  [18, 'Record the reporting period when sharing the file.'],
]);
const [inputs, calculation] = sourcesAndBuild(margin, 'Inputs', 'Calculation', ['May 2027', 'June 2027']);
inputs.getRange('A5:C9').values = [
  ['Units sold', 800, 1000],
  ['Selling price per unit', 34, 35],
  ['Product cost per unit', 13, 14],
  ['Sales returns', 800, 1500],
  ['Freight', 600, 1000],
];
inputs.getRange('B6:C9').setNumberFormat(currency);
inputs.getRange('B5:C9').format.font.color = '#245CA6';
linkedBuild(calculation, 5, ['Units sold', 'Selling price per unit', 'Product cost per unit', 'Gross sales',
  'Sales returns', 'Net sales', 'Product cost', 'Freight', 'Total cost', 'Gross margin',
  'Gross margin basis', 'Gross profit basis', 'Gross profit'], [
  ['=Inputs!B5', '=Inputs!C5'],
  ['=Inputs!B6', '=Inputs!C6'],
  ['=Inputs!B7', '=Inputs!C7'],
  ['=B5*B6', '=C5*C6'],
  ['=-Inputs!B8', '=-Inputs!C8'],
  ['=B8+B9', '=C8+C9'],
  ['=B5*B7', '=C5*C7'],
  ['=Inputs!B9', '=Inputs!C9'],
  ['=SUM(B11:B12)', '=SUM(C11:C12)'],
  ['=IFERROR(B17/B10,0)', '=IFERROR(C17/C10,0)'],
  ['=B10', '=C10'],
  ['=B13', '=C13'],
  ['=B10-B13', '=C10-C13'],
]);
calculation.getRange('B6:C17').setNumberFormat(currency);
calculation.getRange('B14:C14').setNumberFormat('0.0%');
marginCover.getRange('A23').values = [['June gross profit']];
marginCover.getRange('B23').formulas = [['=Calculation!C17']];
marginCover.getRange('B23').setNumberFormat(currency);

await fs.mkdir(previewDirectory, { recursive: true });
for (const [name, book, sheet, coordinate, expected] of [
  ['cash-review', cash, cashBuild, 'B12', 13000],
  ['margin-review', margin, calculation, 'C17', 18500],
]) {
  book.recalculate();
  if (sheet.getRange(coordinate).values[0][0] !== expected) throw new Error(`${name} failed to calculate`);
  for (const tab of book.worksheets.items) {
    const image = await book.render({ sheetName: tab.name, range: 'A1:E24', scale: 1, format: 'png' });
    await fs.writeFile(join(previewDirectory, `${name}-${tab.name}.png`), new Uint8Array(await image.arrayBuffer()));
  }
  const xlsx = await SpreadsheetFile.exportXlsx(book);
  const path = new URL(`${name}.xlsx`, fixtures);
  await xlsx.save(fileURLToPath(path));
  await fs.rm(new URL(`${name}.xlsx.inspect.ndjson`, fixtures), { force: true });
}
