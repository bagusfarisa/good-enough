# Weekly catalog price import SOP

The import is complete when the batch status is **Applied**, the prices for two affected SKUs match the approved CSV, and you record the batch ID and effective date in the **Import log**.

## Before opening Admin

- Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. If the dates differ, stop before uploading.
- Keep the approved CSV for the post-import price check.
- Identify any price increase or decrease of more than 10%. Obtain written approval from Merchandising for each of these changes before publishing. A change of exactly 10% needs no additional approval.

## Upload, preview, and publish

1. In **Admin**, open **Catalog → Bulk price import** and upload the approved CSV.
2. Open **Preview**. Check for missing required fields and duplicate SKUs. Preview validates the file without changing catalog prices.
   - If Preview reports a duplicate SKU or a missing required field, stop. Ask the supplier through your normal contact for a corrected CSV. Do not edit the supplier file by hand. Obtain approval for the corrected CSV, confirm its effective date, and start again with a fresh upload and Preview.
3. When Preview shows **zero errors** and all required written Merchandising approvals are in place, select **Publish** once. Keep the batch ID that Admin returns.

## Verify and record the import

1. While the batch shows **Processing**, wait for the status to change.
   - If the batch shows **Failed**, send the batch ID to the **Catalog Operations** queue and wait for instructions. Do not automatically rerun the batch.
2. When the batch shows **Applied**, choose two affected SKUs from the approved CSV. Look up each SKU in **Catalog** and compare its displayed price with the price for that SKU in the CSV.
   - If either price differs, send the batch ID and both observed Catalog prices, labeled by SKU, to the **Catalog Operations** queue. Wait for instructions. Do not publish again or log completion.
3. When both prices match, record the batch ID and the CSV’s effective date in the **Import log**.
