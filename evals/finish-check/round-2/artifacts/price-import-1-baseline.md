# Weekly catalog price import SOP

## Before you start

- Obtain the approved supplier CSV and confirm that its effective date matches the scheduled import date. Keep the approved copy for the post-import price check.
- Obtain written approval from Merchandising before publishing any price increase or decrease greater than 10%. A change of exactly 10% requires only the standard CSV approval.

## Upload, validate, and publish

1. In Admin, go to **Catalog → Bulk price import**. Upload the approved CSV and open **Preview**. Preview checks the file without changing catalog prices.
2. Check Preview for missing required fields and duplicate SKUs. If either appears, stop. Ask your usual supplier contact for a corrected CSV. Do not edit the supplier file by hand. Obtain approval for the corrected CSV, then start again at step 1.
3. When Preview shows zero errors and all required Merchandising approvals are in place, select **Publish** once. Keep the batch ID that Admin returns.
4. While the batch is **Processing**, wait. When it reaches **Applied**, continue to the price check. If it reaches **Failed**, send the batch ID to the Catalog Operations queue and wait for instructions. Do not automatically rerun the batch.

## Verify prices and log completion

1. In **Catalog**, look up two SKUs affected by the batch. Compare each displayed price with the price for that SKU in the approved CSV.
2. If both prices match, record the batch ID and effective date in the **Import log**. The import is complete once this entry is recorded.
3. If either price differs, send the batch ID and both observed prices to the Catalog Operations queue and wait for instructions. Do not publish again or log completion.
