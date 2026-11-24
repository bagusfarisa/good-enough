# Weekly catalog price import SOP

The import is complete when the batch status is **Applied**, two affected SKU prices in Catalog match the approved CSV, and the batch ID and effective date are recorded in the Import log.

## 1. Confirm the file and approvals

Before opening Admin:

1. Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. If the date differs, stop until you have an approved CSV for the scheduled date.
2. Keep the approved CSV for the post-import price check.
3. Obtain written Merchandising approval before publishing any price increase or decrease greater than 10%. A change of exactly 10% requires no additional approval.

## 2. Upload and preview

1. In Admin, open **Catalog → Bulk price import**.
2. Upload the approved CSV and open **Preview**. Preview checks the rows without changing catalog prices.
3. Check for missing required fields and duplicate SKUs. Either error means you must stop. Ask the supplier through the normal supplier contact for a corrected CSV. Obtain approval for the corrected file, then start again at step 1 of this SOP with that file. Do not edit the supplier CSV by hand.

## 3. Publish and wait for the result

When Preview reports **zero errors** and all required Merchandising approvals are in place, select **Publish** once. Keep the batch ID returned by Admin.

- **Processing** — Wait for the batch status to change.
- **Applied** — Verify the prices as described below.
- **Failed** — Send the batch ID to the Catalog Operations queue. Do not automatically rerun the batch.

## 4. Verify prices and log completion

1. In Catalog, look up two SKUs affected by the batch. Compare each displayed price with the price for that SKU in the approved CSV.
2. If both prices match, record the batch ID and the CSV’s effective date in the **Import log**.
3. If either price differs, send the batch ID and both observed prices, labeled with their SKUs, to the Catalog Operations queue. Wait for instructions. Do not publish again or log completion.
