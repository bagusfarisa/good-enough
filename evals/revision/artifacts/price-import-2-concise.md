# Weekly catalog price import SOP

1. **Confirm the file and approvals.** Get the approved supplier CSV and verify that its effective date matches the scheduled import date. Keep the approved copy for the post-import check. Before publishing, get written Merchandising approval for any price increase or decrease greater than 10%. A change of exactly 10% requires no additional approval.
2. **Upload and preview.** In Admin, go to **Catalog → Bulk price import**, upload the approved CSV, and open **Preview**. Check for missing required fields and duplicate SKUs. If either appears, stop and ask the supplier to correct the file. Do not edit the CSV yourself. Get the corrected CSV approved, start a fresh upload, and rerun Preview.
3. **Publish once.** When Preview shows zero errors and all required approvals are in place, select **Publish** once. Keep the returned batch ID handy and wait while the batch status is **Processing**.
4. **Verify and log the result.**
   - **Applied:** Compare the prices of two affected SKUs in Catalog with their prices in the approved CSV. If both match, record the batch ID and effective date in the **Import log**.
   - **Applied with a price mismatch:** Send the batch ID and both observed Catalog prices to the **Catalog Operations** queue. Wait for instructions. Do not publish again or log completion.
   - **Failed:** Send the batch ID to the **Catalog Operations** queue and wait for instructions. Do not rerun the batch on your own.
