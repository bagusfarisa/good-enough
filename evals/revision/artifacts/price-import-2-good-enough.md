# Weekly catalog price import SOP

## 1. Get the approved CSV

Before opening Admin, obtain the approved supplier CSV and confirm that its effective date matches the scheduled import date. If the dates differ, stop and obtain an approved CSV for the scheduled date. Keep the approved copy for the post-import price check.

## 2. Upload and validate the file

1. In Admin, go to **Catalog → Bulk price import**.
2. Upload the approved CSV and open **Preview**. Check for missing required fields and duplicate SKUs. Preview validates the rows without changing catalog prices.
3. If Preview reports duplicate SKUs or missing required fields, stop. Ask the supplier to correct the file through the normal supplier contact. Obtain approval for the corrected CSV, then start again with a fresh upload and Preview. Do not edit the supplier CSV by hand.
4. Before publishing, obtain written approval from Merchandising for each price increase or decrease greater than 10%. A change of exactly 10% requires no additional approval.

## 3. Publish and wait for the batch result

When Preview shows zero errors and all required Merchandising approvals are in place, select **Publish** once. Keep the batch ID that Admin returns and wait while the status is **Processing**.

- **Applied** — Verify the prices in Catalog.
- **Failed** — Send the batch ID to the Catalog Operations queue and wait for instructions. Do not automatically rerun the batch.

## 4. Verify prices and record completion

1. In Catalog, compare the displayed prices for two affected SKUs against their prices in the approved CSV.
2. If both prices match, record the batch ID and effective date in the **Import log**. The import is complete.
3. If either price differs, send the batch ID and both observed prices to the Catalog Operations queue and wait for instructions. Do not publish again or log completion.
