# Weekly catalog price import SOP

## Before opening Admin

- Obtain the approved supplier CSV and confirm that its effective date matches the scheduled import date. If the dates differ, stop before uploading.
- Keep the approved CSV for the post-import price check.
- Obtain written approval from Merchandising before publishing if any price increases or decreases by more than 10%. A change of exactly 10% requires no additional approval.

## Upload and validate

1. In Admin, go to **Catalog → Bulk price import** and upload the approved CSV.
2. Open **Preview**. Check for missing required fields and duplicate SKUs. Preview validates the file without changing catalog prices.
3. If Preview reports missing required fields or duplicate SKUs, stop. Ask the supplier through the normal supplier contact for a corrected CSV. Do not edit the file by hand. Obtain approval for the corrected CSV, recheck its effective date and any required Merchandising approvals, then restart at step 1 with the corrected file.
4. Continue to publishing only when Preview reports zero errors and all required written Merchandising approvals are in place.

## Publish, verify, and log

1. Select **Publish** once. Note the batch ID returned by Admin and wait while the status is **Processing**.
2. When the status is **Applied**, look up two affected SKUs in **Catalog** and compare each displayed price with its price in the approved CSV.
3. If both prices match, record the batch ID and effective date in the **Import log**. This completes the import.
4. If either price differs, send the batch ID and both observed prices to the **Catalog Operations** queue. Wait for instructions before taking further action. Do not publish again or log completion.
5. If the batch status is **Failed**, send the batch ID to the **Catalog Operations** queue. Do not automatically rerun the batch.
