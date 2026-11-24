# Weekly catalog price import SOP

## Before opening Admin

1. Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. If the dates differ, stop until you have an approved CSV for the scheduled date.
2. Keep the approved CSV for the post-import price check.
3. Identify any price increase or decrease greater than 10%. Obtain written approval from Merchandising before publishing any such change. A change of exactly 10% in either direction needs no additional approval.

## Upload, preview, and publish

1. In Admin, open **Catalog → Bulk price import**. Upload the approved CSV and open **Preview**.
2. Check Preview for missing required fields and duplicate SKUs. Preview validates the rows without changing catalog prices.
   - If a required field is missing or a SKU appears more than once, stop. Ask the supplier through the normal supplier contact to correct the CSV. Obtain approval for the corrected file, then restart this SOP with that file. Do not edit the supplier CSV by hand.
   - If Preview reports any other error, stop. Publish only when Preview reports zero errors.
3. When Preview reports zero errors and all required Merchandising approvals are in place, select **Publish** once. Publish submits the price changes. Keep the batch ID returned by Admin.

## Verify and log the import

1. While the batch status is **Processing**, wait.
2. When the status is **Applied**, open two affected SKUs in **Catalog** and compare each displayed price with the price for that SKU in the approved CSV.
   - If both prices match, record the batch ID and effective date in the **Import log**. The import is complete.
   - If either price differs, send the batch ID and both observed prices to the **Catalog Operations** queue. Do not publish again or log completion. Wait for Catalog Operations’ instructions.
3. If the batch status is **Failed**, send the batch ID to the **Catalog Operations** queue. Do not rerun the batch automatically.
