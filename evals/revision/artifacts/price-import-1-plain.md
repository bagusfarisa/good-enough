# Weekly catalog price import SOP

## 1. Check the file and approvals

1. Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. If the dates differ, stop and obtain an approved CSV with the correct effective date.
2. Keep the approved CSV for the post-import price check.
3. Identify any price increase or decrease greater than 10% against the current catalog price. Obtain written approval from Merchandising for each such change before publishing. A change of exactly 10% can proceed without additional Merchandising approval.

## 2. Upload and validate the file

1. In Admin, go to **Catalog → Bulk price import**.
2. Upload the approved CSV and open **Preview**. Preview checks the file without changing catalog prices.
3. Check for missing required fields and duplicate SKUs. If Preview reports either issue, stop and ask the supplier to correct the file through the usual supplier contact. Do not edit the supplier CSV by hand.
4. Obtain approval for the corrected CSV, then restart at step 1 of this SOP with that file. Upload it as a fresh import and rerun Preview.
5. Proceed only when Preview reports zero errors and all required written approvals are in place.

## 3. Publish and monitor the batch

1. Select **Publish** once. Keep the returned batch ID handy for verification or escalation.
2. Wait while the batch status is **Processing**.
3. If the status becomes **Applied**, continue to the post-import check.
4. If the status becomes **Failed**, send the batch ID to the **Catalog Operations** queue and wait for instructions. Do not rerun the batch or log it as complete.

## 4. Verify prices and record completion

1. Choose two SKUs affected by the batch. In **Catalog**, compare each SKU’s displayed price with its price in the approved CSV.
2. If both prices match, record the **batch ID** and **effective date** in the **Import log**. The import is complete.
3. If either price differs, send the **batch ID**, **both SKU identifiers**, and **both observed catalog prices** to the **Catalog Operations** queue. Wait for instructions. Do not publish again or log the batch as complete.
