# Weekly territory dashboard refresh SOP

## Before you start

Run the refresh on Monday in the Refresh workspace. Keep the last published dashboard live until the replacement passes validation and its publication slot begins.

Use the approved roster and the approved territory adjustment file. The adjustment file must arrive by **Monday at 11:30 UTC** to use the normal publication slot.

## Prepare and validate the draft

1. Create a draft in the Refresh workspace. Upload the approved roster and adjustment file, and retain both files with the draft for the publication log.
2. Run **Validate**. It checks for blank account IDs, duplicate account IDs, and missing required columns.
   - **Blank account IDs.** Stop the refresh, keep the draft unpublished, and ask Data Operations for a corrected roster. When the corrected roster is available and the refresh is cleared to proceed, replace the draft roster and rerun **Validate**. Keep the existing adjustments unless Sales Operations has supplied a replacement.
   - **Duplicate account IDs or missing required columns.** Ask Data Operations for a corrected roster. Replace the draft roster with the file they provide and rerun **Validate**.
   
   Use the corrected roster from Data Operations for all roster errors. Leave upstream ID corrections to Data Operations.
3. If the approved adjustment file arrives **after Monday at 11:30 UTC**, keep the last published dashboard live and notify Sales Operations. Wait for Sales Operations to confirm the revised publication slot and for that slot to begin before publishing. Ask the Reporting process owner where to resume if the late file coincides with a roster correction. The procedure does not specify which exception takes precedence.

## Publish and verify

1. Once **Validate** reports **zero errors** and the applicable publication slot has begun, select **Publish** once.
2. Open the published dashboard and compare its roster count with the count reported by **Validate**.
   - **Counts match.** Record the published version, roster count, and publication time in the publication log. The refresh is complete.
   - **Counts differ.** Keep the version unconfirmed and send the version and both counts to Reporting Support. Wait for their response before marking the version complete.
