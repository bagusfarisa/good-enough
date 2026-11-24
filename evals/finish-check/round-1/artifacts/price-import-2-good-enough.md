# Weekly catalog price import SOP

## Before you start

- Obtain the approved supplier CSV and confirm that its effective date matches the scheduled import date. If the dates differ, stop before uploading and confirm the correct file and date with the catalog lead.
- Keep the approved CSV for the post-import price check.

## 1. Upload and validate the CSV

In Admin, go to **Catalog → Bulk price import**. Upload the approved CSV and open **Preview**. Check for missing required fields and duplicate SKUs. Preview checks the file without changing catalog prices.

If Preview reports a duplicate SKU or a missing required field, stop. Ask the supplier through the normal supplier contact for a corrected CSV. Keep the supplier file as received. Obtain approval for the corrected CSV, then return to **Before you start** and repeat the upload and Preview with that file.

## 2. Confirm approvals and publish

Check each proposed price against its current catalog price. Obtain written approval from Merchandising for every increase or decrease greater than 10%. A change of exactly 10% requires only the standard CSV approval.

When Preview shows **zero errors** and all required approvals are in place, select **Publish** once. Keep the returned batch ID handy while you wait for the batch to leave **Processing**.

## 3. Verify the batch and log completion

- **Applied.** Choose two SKUs affected by the batch. In **Catalog**, compare each SKU’s current price with its price in the approved CSV. If both match, record the batch ID and effective date in the **Import log**. That completes the import.
- **Applied with a price mismatch.** Send the batch ID and both observed catalog prices to the **Catalog Operations** queue. Leave the import unlogged and wait for instructions before publishing again.
- **Failed.** Send the batch ID to the **Catalog Operations** queue. Wait for their instructions before rerunning the import.
