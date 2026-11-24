# Weekly catalog price import

The import is complete when Admin shows **Applied**, both checked prices match the approved CSV, and you have recorded the batch ID and effective date in the Import log.

## 1. Prepare the file

1. Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date before opening Admin. Keep the approved copy for the post-import check.
2. Obtain written approval from Merchandising before publishing any price increase or decrease greater than 10%. A change of exactly 10% requires only the standard CSV approval.

## 2. Upload, preview, and publish

1. In Admin, open **Catalog → Bulk price import**. Upload the approved CSV and open **Preview**.
2. Check Preview for missing required fields and duplicate SKUs. Preview validates the rows without changing catalog prices.
   - **Missing required fields or duplicate SKUs:** Stop. Ask the supplier through your usual contact for a corrected CSV. Leave the supplier file unedited. Obtain approval for the corrected CSV, confirm its effective date, and start again with a fresh upload and Preview.
   - **Any other preview error:** Stop. Publish only after Preview reports zero errors.
3. When Preview reports zero errors and all required approvals are in place, select **Publish** once. Admin returns a batch ID and shows **Processing**. Keep the batch ID for verification or escalation.

## 3. Verify and log the import

- **Processing:** Wait for the batch status to change.
- **Applied:** Open **Catalog** and compare the prices of two affected SKUs with their prices in the approved CSV. If both match, record the batch ID and effective date in the **Import log**. If either differs, stop before logging completion or publishing again. Send the batch ID and both prices you observed in Catalog to the **Catalog Operations** queue, then wait for instructions.
- **Failed:** Send the batch ID to the **Catalog Operations** queue and wait for instructions before retrying.
