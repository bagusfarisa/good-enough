# Weekly catalog price import

The import is complete when Admin shows **Applied**, two affected SKU prices in Catalog match the approved CSV, and you have recorded the batch ID and effective date in the Import log.

## Before opening Admin

- Obtain the approved supplier CSV and confirm its effective date matches the scheduled import date. Keep that approved copy for the post-import check.
- Obtain written approval from Merchandising before publishing any price change of more than 10% in either direction. A change of exactly 10% can proceed without this additional approval.

## 1. Upload and validate the CSV

In Admin, go to **Catalog → Bulk price import**, upload the approved CSV, and open **Preview**. Preview checks for missing required fields and duplicate SKUs without changing prices.

If Preview finds a missing required field or a duplicate SKU, stop. Ask the supplier to correct the file through your normal supplier contact. Do not edit the supplier CSV by hand. Obtain approval for the corrected CSV, repeat the pre-import checks for that file, then restart at step 1 with a fresh upload and Preview.

## 2. Publish and wait for the batch status

When Preview shows **zero errors** and all required approvals are in place, select **Publish** once. Keep the batch ID returned by Admin and wait while the batch is **Processing**.

- **Applied** → Continue to step 3.
- **Failed** → Send the batch ID to the Catalog Operations queue and wait for instructions. Do not rerun the batch on your own.

## 3. Verify two prices and log the import

Look up two affected SKUs in **Catalog**. Compare each displayed price with the price for that SKU in the approved CSV you uploaded.

- **Both prices match** → Record the batch ID and effective date in the Import log.
- **Either price differs** → Send the batch ID and both observed Catalog prices to the Catalog Operations queue and wait for instructions. Do not publish again or log completion.
