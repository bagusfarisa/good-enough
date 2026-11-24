# Weekly catalog price import SOP

## Before opening Admin

- Obtain the approved supplier CSV and confirm its effective date matches the scheduled import date. If the dates differ, pause until you have an approved CSV for the scheduled date.
- Keep the approved CSV for the post-import price check.

## Run the import

1. **Upload the approved CSV.** In Admin, go to **Catalog → Bulk price import**, upload the file, and open **Preview**.
2. **Check Preview for errors.** Proceed only when Preview shows zero errors. If Preview reports duplicate SKUs or missing required fields, stop and ask the supplier through the usual contact to correct all reported issues. Obtain approval for the corrected CSV, repeat the checks under **Before opening Admin**, and restart at step 1. Do not edit the supplier CSV by hand.
3. **Check for price changes over 10%.** Obtain written approval from Merchandising before publishing any increase or decrease greater than 10%. A change of exactly 10% in either direction requires no additional approval. If approval is pending, pause and resume at step 4 once you have it.
4. **Publish once.** With zero Preview errors and any required written approval in place, select **Publish** once. Keep the batch ID returned by Admin and wait while the batch is **Processing**.
   - **Applied** — Continue to step 5.
   - **Failed** — Send the batch ID to the **Catalog Operations** queue and wait for instructions. Do not automatically rerun the batch.
5. **Verify two affected SKUs.** In **Catalog**, compare the current price of each SKU with its price in the approved CSV. If either price differs, send the batch ID and both observed prices to the **Catalog Operations** queue and wait for instructions. Do not publish again or log completion.
6. **Record completion.** Once both prices match, enter the batch ID and the CSV’s effective date in the **Import log**.
