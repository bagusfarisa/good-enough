# Weekly catalog price import

Start with the approved supplier CSV. Publish only after Preview reports zero errors and Merchandising has approved every price change over 10% in either direction. Log the import only after the batch shows **Applied** and two affected prices match the approved CSV.

## Before opening Admin

1. Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. If the dates differ, stop until you have an approved CSV for the scheduled date.
2. Obtain written approval from Merchandising for each price increase or decrease over 10%. A change of exactly 10% requires no additional approval.
3. Keep the approved CSV for the post-import check.

## Upload, preview, and publish

1. In Admin, open **Catalog → Bulk price import**.
2. Upload the approved CSV and open **Preview**. Preview checks required fields and duplicate SKUs without changing catalog prices.
3. If Preview finds duplicate SKUs or missing required fields, stop. Ask the supplier through the normal supplier contact for a corrected CSV. Obtain approval for the corrected file, then restart at step 1 of this procedure and rerun **Preview**. Do not edit the supplier CSV by hand.
4. When Preview reports zero errors and all required written approvals are in place, select **Publish** once. The system returns a batch ID and shows the batch as **Processing**. Keep the batch ID and wait for processing to finish.

## Verify and log the import

- **Applied** — Look up two affected SKUs in **Catalog** and compare each displayed price with its price in the approved CSV. If both prices match, record the batch ID and effective date in the **Import log**. This completes the import.
- **Applied with a price mismatch** — Send the batch ID and both observed catalog prices to the **Catalog Operations** queue. Wait for instructions before taking further action. Do not publish again or log completion.
- **Failed** — Send the batch ID to the **Catalog Operations** queue and wait for instructions. Do not automatically rerun the batch.
