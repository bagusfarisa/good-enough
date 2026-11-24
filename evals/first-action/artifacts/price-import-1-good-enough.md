# Weekly catalog price import SOP

## Before opening Admin

1. Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. If the file is unapproved or the dates differ, stop until you have an approved CSV with the correct effective date.
2. Keep the approved CSV for the post-import price check.
3. Identify any price increase or decrease of more than 10% from the current catalog price. Obtain written approval from Merchandising for each such change before publishing. A change of exactly 10% requires no additional approval.

## Upload, preview, and publish

1. In Admin, go to **Catalog → Bulk price import**. Upload the approved CSV and open **Preview**. Preview checks the file without changing catalog prices.
2. Check Preview for missing required fields and duplicate SKUs. If either appears, stop and ask the supplier for a corrected file through your normal supplier contact. Do not edit the CSV by hand. Obtain approval for the corrected CSV, recheck its effective date and any required Merchandising approvals, then upload it as a fresh import and run Preview again.
3. When Preview shows **zero errors** and all required written approvals are in place, select **Publish** once. Keep the batch ID returned by the system. While the batch is **Processing**, wait for it to finish.

## Verify and log the batch

| Batch result | What to do |
| --- | --- |
| **Applied** | In Catalog, look up two SKUs affected by the batch. Compare each displayed price with the price for that SKU in the approved CSV. Record the batch ID and effective date in the **Import log** only after both prices match. |
| **Applied**, with either price differing | Send the batch ID and both observed Catalog prices to the **Catalog Operations** queue and wait for instructions. Do not publish again or log completion. |
| **Failed** | Send the batch ID to the **Catalog Operations** queue. Do not automatically rerun the batch. |
