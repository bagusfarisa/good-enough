# Weekly catalog price import SOP

The import is complete when the batch shows **Applied**, two affected SKU prices match the approved CSV, and you have recorded the batch ID and effective date in the Import log.

## Before opening Admin

1. Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date.
2. Keep the approved CSV for the post-import price check.

## Preview and publish

1. In Admin, open **Catalog → Bulk price import**. Upload the approved CSV and open **Preview**. Preview checks the file without changing catalog prices.
2. Check Preview for duplicate SKUs and missing required fields. If either appears, stop and ask the supplier to correct the file through your normal supplier contact. Do not edit the CSV by hand. Obtain approval for the corrected CSV, confirm its effective date, and start again with a fresh upload and Preview.
3. Before publishing, obtain written approval from Merchandising for any price increase or decrease greater than 10%. A change of exactly 10% requires no additional approval.
4. When Preview shows zero errors and all required approvals are in place, select **Publish** once. Keep the returned batch ID and wait while the batch shows **Processing**.

## Verify and log the import

- **Applied.** Open two affected SKUs in **Catalog** and compare each displayed price with the corresponding price in the approved CSV. If both match, enter the batch ID and effective date in the **Import log**.
- **Applied with a price mismatch.** Send the batch ID and both observed prices to the **Catalog Operations** queue. Wait for instructions before taking further action. Do not publish again or log completion.
- **Failed.** Send the batch ID to the **Catalog Operations** queue. Do not rerun the batch automatically.
