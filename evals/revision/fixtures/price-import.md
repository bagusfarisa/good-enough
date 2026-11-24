# Weekly catalog price import working notes

## Purpose and normal cadence

The catalog lead uses the price file to apply the weekly supplier changes. Before opening Admin, obtain the approved CSV and confirm that its effective date matches the scheduled import date. Keep the approved copy for the post-import check. For a price change over 10% in either direction, obtain written approval from Merchandising before publishing. A change of exactly 10% does not require that additional approval.

## Admin navigation

Open Catalog, then Bulk price import. Upload the approved CSV and open Preview. Use Preview to check required fields and duplicate SKUs. The preview does not change prices. Once Preview reports zero errors and any required price approvals are in place, select Publish once. The system returns a batch ID and places the batch in Processing. Wait for it to finish.

## Troubleshooting before publish

Duplicate SKUs mean two rows target the same item. Stop the import. Ask the supplier for a corrected file. Obtain approval for the corrected CSV, upload the corrected CSV from the start of the import, and rerun Preview. Missing required fields also mean stop. Ask the supplier to correct the CSV, obtain approval, and run a fresh upload and Preview. Do not patch a supplier CSV by hand.

## Status and records

After Publish, wait for status Applied. Compare two affected SKUs in Catalog with the approved CSV before logging the batch ID. Record the batch ID and effective date in the Import log once both prices match. A mismatch after Applied means do not publish again or log completion. Send the batch ID and both observed prices to Catalog Operations and wait for their instructions. A batch marked Failed also goes to Catalog Operations with the batch ID. Do not automatically rerun a Failed batch.

## Keep for reference

Preview is the row validation step. Publish is the action that changes catalog prices. The two affected items need a post-publish comparison, and the batch ID is part of the import record. Use the normal supplier contact for corrections to the file and the Catalog Operations queue for problems with a submitted batch.
