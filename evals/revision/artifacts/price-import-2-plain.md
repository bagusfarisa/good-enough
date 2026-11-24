# Weekly catalog price import SOP

## 1. Confirm the file and approvals

1. Obtain the approved supplier CSV before opening Admin.
2. Confirm that the CSV’s effective date matches the scheduled import date. If the dates differ, stop before uploading and obtain an approved CSV for the scheduled date.
3. Keep the approved CSV for the post-import price check.
4. Obtain written approval from Merchandising before publishing any price increase or decrease greater than 10%. A change of exactly 10% in either direction requires only the standard CSV approval.

## 2. Upload and validate the CSV

1. In Admin, go to **Catalog → Bulk price import**.
2. Upload the approved CSV and open **Preview**. Preview checks required fields and duplicate SKUs without changing catalog prices.
3. If Preview flags a duplicate SKU or a missing required field, stop. Ask the supplier to correct the file through your normal supplier contact. Leave edits to the supplier.
4. Obtain approval for the corrected CSV, then restart at step 1 of this SOP using the corrected file. Run a fresh Preview.

## 3. Publish and monitor the batch

1. When Preview shows zero errors and all required written approvals are in place, select **Publish** once.
2. Retain the batch ID displayed by Admin. While the batch status is **Processing**, wait for it to finish.
3. If the status changes to **Applied**, proceed to the price check below.
4. If the status changes to **Failed**, send the batch ID to the **Catalog Operations** queue and wait for instructions before retrying.

## 4. Verify prices and record completion

1. Select two affected SKUs from the approved CSV used for the import.
2. In **Catalog**, compare the displayed price for each SKU with its price in that CSV.
3. If both prices match, record the batch ID and effective date in the **Import log**.
4. If either price differs, send the batch ID and both observed Catalog prices to the **Catalog Operations** queue. Leave the batch unlogged and wait for instructions before taking further action.
