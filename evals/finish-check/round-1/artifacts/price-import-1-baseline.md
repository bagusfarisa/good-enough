# Weekly catalog price import

## Before you start

- Obtain the approved supplier CSV and confirm that its effective date matches the scheduled import date. Keep the approved file for the post-import check.
- Check the proposed prices against current Catalog prices. If any price increases or decreases by more than 10%, obtain written approval from Merchandising before publishing. A change of exactly 10% in either direction does not require additional approval.

## Upload, preview, and publish

1. In Admin, open **Catalog → Bulk price import**. Upload the approved CSV and open **Preview**.
2. Check Preview for missing required fields and duplicate SKUs. If either appears, stop. Ask the supplier to correct the file through the usual supplier contact. Do not edit the supplier CSV by hand. Obtain approval for the corrected CSV, start again with a fresh upload, and rerun Preview.
3. When Preview shows zero errors and all required written Merchandising approvals are in place, select **Publish** once. Preview validates the file. Publish submits the price changes.
4. Keep the batch ID returned by the system. Wait while the batch status is **Processing**.
   - **Applied**. Continue to the post-import check.
   - **Failed**. Send the batch ID to the Catalog Operations queue and wait for instructions. Do not rerun the batch automatically.

## Verify and log completion

1. In **Catalog**, look up two affected SKUs and compare each displayed price with its price in the approved CSV.
2. If both prices match, record the batch ID and effective date in the **Import log**. The import is complete when both prices match and the log entry is saved.
3. If either price differs, send the batch ID and both observed prices, labeled by SKU, to the Catalog Operations queue. Wait for instructions. Do not publish again or log completion.
