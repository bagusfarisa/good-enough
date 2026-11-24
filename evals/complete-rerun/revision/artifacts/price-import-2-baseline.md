# Weekly catalog price import

Use this procedure to apply the weekly supplier price changes in Admin. The import is complete when the batch shows **Applied**, two affected SKU prices match the approved CSV, and you record the batch ID and effective date in the Import log.

## Before you open Admin

- Obtain the approved supplier CSV and confirm that its effective date matches the scheduled import date. Keep the approved copy for the post-import check.
- Obtain written approval from Merchandising before publishing any price increase or decrease greater than 10%. A change of exactly 10% does not require additional approval.

## Upload, preview, and publish

1. In Admin, open **Catalog** → **Bulk price import**. Upload the approved CSV and open **Preview**. Preview checks required fields and duplicate SKUs without changing prices.
2. If Preview reports duplicate SKUs or missing required fields, stop. Ask your usual supplier contact for a corrected CSV. Do not edit the supplier file by hand. Obtain approval for the corrected CSV, confirm its effective date, then start again with a fresh upload and Preview.
3. When Preview shows zero errors and you have all required written Merchandising approvals, select **Publish** once. Note the batch ID returned by the system.

## Verify and log the import

1. While the batch shows **Processing**, wait. If it shows **Failed**, send the batch ID to the Catalog Operations queue. Do not automatically rerun the batch.
2. When the batch shows **Applied**, look up two affected SKUs in **Catalog**. Compare each displayed price with the price for that SKU in the approved CSV.
3. If both prices match, record the batch ID and effective date in the **Import log**.
4. If either price differs, send the batch ID and both prices you observed in Catalog to the Catalog Operations queue. Do not publish again or log completion. Wait for Catalog Operations to tell you how to proceed.
