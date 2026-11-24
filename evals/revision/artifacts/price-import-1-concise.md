# Weekly catalog price import SOP

1. **Confirm the file.** Obtain the approved supplier CSV. Confirm that its effective date matches the scheduled import date. Keep the approved CSV for the post-import check.
2. **Run Preview.** In Admin, open **Catalog → Bulk price import**, upload the approved CSV, and open **Preview**. Check for missing required fields and duplicate SKUs. If either appears, stop. Ask the supplier for a corrected CSV through the usual supplier contact, obtain approval for the corrected file, then start a fresh upload and rerun Preview. Do not edit the supplier CSV by hand.
3. **Publish once.** Proceed only when Preview shows zero errors and Merchandising has given written approval for every increase or decrease greater than 10%. Exactly 10% requires no additional approval. Select **Publish** once, capture the batch ID, and wait for the batch to leave **Processing**.
4. **Verify and log.** When the batch status is **Applied**, compare the prices of two affected SKUs in **Catalog** with their prices in the approved CSV. If both match, record the batch ID and effective date in the **Import log**.

## Escalate submitted batches

- **Applied with a price mismatch.** Send the batch ID and both observed Catalog prices to the **Catalog Operations** queue. Wait for instructions. Do not publish again or log completion.
- **Failed.** Send the batch ID to the **Catalog Operations** queue and wait for instructions. Do not automatically rerun the batch.
