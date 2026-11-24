# Weekly catalog price import SOP

## Before you start

- Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. If the dates differ, stop and obtain an approved CSV for the scheduled date.
- Keep the approved CSV for the post-import price check.
- Obtain written approval from Merchandising before publishing if any price increases or decreases by more than 10%. A change of exactly 10% requires no additional approval.

## Upload and validate the CSV

1. In Admin, open **Catalog → Bulk price import**.
2. Upload the approved CSV and open **Preview**. Preview checks required fields and duplicate SKUs without changing catalog prices.
3. Continue only when Preview reports zero errors and you have any required written approval from Merchandising.
   - **Duplicate SKUs or missing required fields:** Stop. Use the normal supplier contact to request a corrected CSV. Do not edit the supplier file by hand. Obtain approval for the corrected CSV, start again at step 1, and rerun Preview.

## Publish and verify

1. Select **Publish** once. Keep the returned batch ID and wait while the batch status is **Processing**.
2. When the status is **Applied**, check two affected SKUs in **Catalog**. Compare each displayed price with the price for that SKU in the approved CSV.
   - **Both prices match:** Record the batch ID and effective date in the **Import log**. The import is complete.
   - **Either price differs:** Send the batch ID and both observed Catalog prices to the **Catalog Operations queue**. Wait for instructions. Do not publish again or log completion.
3. If the batch status is **Failed**, send the batch ID to the **Catalog Operations queue**. Do not automatically rerun the batch.
