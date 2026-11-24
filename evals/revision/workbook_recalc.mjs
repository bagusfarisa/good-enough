// Apply scenario inputs on disposable in-memory copies of each artifact.
import fs from 'node:fs/promises';
import { createRequire } from 'node:module';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const [modules, requestFile, outputFile, previews] = process.argv.slice(2);
const require = createRequire(join(resolve(modules), '..', 'resolve-artifact-tool.cjs'));
const { FileBlob, SpreadsheetFile } = await import(pathToFileURL(require.resolve('@oai/artifact-tool')));
const requests = JSON.parse(await fs.readFile(requestFile, 'utf8'));
await fs.mkdir(previews, { recursive: true });
const results = {};
for (const request of requests) {
  try {
    const book = await SpreadsheetFile.importXlsx(await FileBlob.load(request.file));
    const inputs = book.worksheets.getItem(request.input_sheet);
    const build = book.worksheets.getItem(request.build_sheet);
    const open = book.worksheets.getItem(request.opening_sheet);
    const read = (sheet, cells) => Object.fromEntries(cells.map(address =>
      [address, sheet.getRange(address).values[0][0]]));
    const readBuild = () => read(build, Object.keys(request.outputs));
    const edit = values => {
      for (const [cell, value] of Object.entries(values)) inputs.getRange(cell).values = [[value]];
      book.recalculate();
    };
    book.recalculate();
    const base = readBuild();
    const original = read(inputs, Object.keys(request.edit));
    const headlineBefore = read(open, request.headline_cells);
    const png = await book.render({
      sheetName: request.opening_sheet, range: 'A1:H24', scale: 1, format: 'png',
    });
    await fs.writeFile(join(previews, `${request.identifier}.png`), new Uint8Array(await png.arrayBuffer()));
    edit(request.edit);
    const primary = readBuild();
    const headlineAfter = read(open, request.headline_cells);
    edit({ ...original, ...request.secondary_edit });
    results[request.identifier] = {
      base, primary, secondary: readBuild(), headline_before: headlineBefore, headline_after: headlineAfter,
    };
  } catch (error) {
    results[request.identifier] = {error: error.message};
  }
}
await fs.writeFile(outputFile, JSON.stringify(results));
