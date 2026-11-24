# Weekly catalog price import SOP

The import is complete when the batch shows **Applied**, two affected SKU prices match the approved CSV, and you record the batch ID and effective date in the Import log.

## Before you open Admin

- Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. Keep the approved file for the post-import check.
- Identify any price increase or decrease greater than 10% and obtain written approval from Merchandising before publishing. A change of exactly 10% requires no additional approval.

## Upload, preview, and publish

1. In Admin, open **Catalog → Bulk price import**. Upload the approved CSV and open **Preview**. Preview checks the rows without changing catalog prices.
2. Check Preview for missing required fields and duplicate SKUs. If either appears, stop and ask the supplier to correct the file through your normal supplier contact. Obtain approval for the corrected CSV, then start again with a fresh upload and Preview. Use the supplier’s corrected file without editing it by hand.
3. When Preview reports zero errors and all required Merchandising approvals are in place, select **Publish** once. Keep the batch ID returned by Admin and wait for the batch to leave **Processing**.

## Verify and log the batch

- **Applied.** Open two affected SKUs in **Catalog** and compare each displayed price with the price for that SKU in the approved CSV. If both match, record the batch ID and effective date in the **Import log**. If either price differs, send the batch ID and both observed prices to the **Catalog Operations** queue. Wait for instructions before taking further action. Do not publish again or log completion.
- **Failed.** Send the batch ID to the **Catalog Operations** queue. Do not automatically rerun the batch.
