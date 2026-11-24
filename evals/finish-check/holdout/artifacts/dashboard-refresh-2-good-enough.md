# Weekly territory dashboard refresh SOP

Run the refresh on Monday. Keep the last published dashboard live until the replacement passes Validate and the applicable publication slot begins.

## 1. Prepare the draft

Create a draft in the Refresh workspace. Use the approved roster and the approved territory adjustment file. Retain both files with the draft for the publication log.

The approved adjustment file must arrive by **Monday at 11:30 UTC** to use the normal publication slot. If it arrives after the cutoff, keep the last published dashboard live and notify Sales Operations. Sales Operations owns adjustment approvals and will confirm a revised publication slot. Use that slot in step 3.

## 2. Upload the files and run Validate

Upload both approved files to the draft and run **Validate**. Validate checks for blank account IDs, duplicate account IDs, and missing required columns.

- **Blank account IDs.** Stop the refresh, keep the draft unpublished, and request a corrected roster from Data Operations. When the corrected roster is available and the refresh is cleared to proceed, replace the roster in the draft and rerun Validate.
- **Duplicate account IDs or missing required columns.** Request a corrected roster from Data Operations. Replace the roster in the draft and rerun Validate.

Use the corrected roster from Data Operations as provided. Leave the adjustment file in the draft unless Sales Operations supplies a replacement. If a roster correction leaves the publication slot or clearance to resume unclear, ask the Reporting process owner to resolve it before proceeding.

## 3. Publish and confirm the refresh

1. When Validate reports **zero errors** and the applicable publication slot begins, select **Publish** once.
2. Open the published dashboard and compare its roster count with the count reported by Validate.
3. If the counts match, record the version, roster count, and publication time in the publication log. The refresh is complete.
4. If the counts differ, keep the version unconfirmed and send the version and both counts to Reporting Support. Wait for their response before marking the version complete. Record the publication in the log only if the counts match.
