# Weekly territory dashboard refresh SOP

Refresh the territory dashboard on Monday. Keep the currently published dashboard live until the replacement passes Validate and the applicable publication slot begins.

## Prepare the draft

1. Create a draft in the Refresh workspace. Use the approved roster from Data Operations and the approved territory adjustment file from Sales Operations. Retain both files with the draft for the publication log.
2. Check when the approved adjustment file arrived. If it arrived by **Monday at 11:30 UTC**, use the normal publication slot. If it arrives later, keep the last published dashboard live, notify Sales Operations, and wait for the revised publication slot they confirm before publishing.
3. Upload the approved roster and adjustment file to the draft.

## Validate the draft

1. Run **Validate**. It checks for blank account IDs, duplicate account IDs, and missing required columns.
2. If Validate flags any of these errors, keep the draft unpublished and request a corrected roster from Data Operations. Use their corrected roster without editing upstream IDs by hand.
   - If any account ID is blank, stop the refresh. Resume only when the corrected roster is available and the refresh is cleared to proceed.
   - Replace the draft roster and rerun **Validate**. Keep the adjustment file already in the draft unless Sales Operations supplies a replacement.
3. Proceed to publication only when **Validate** reports zero errors.

## Publish and confirm

1. When the applicable publication slot begins and **Validate** has reported zero errors, select **Publish** once.
2. Open the published dashboard and compare its roster count with the count reported by **Validate**.
   - **Counts match.** Record the version, roster count, and publication time in the publication log. This confirms the refresh is complete.
   - **Counts differ.** Keep the version unconfirmed and send the version and both counts to Reporting Support. Wait for their response before marking the version complete. Record the publication log entry only when the counts match.

Direct questions this procedure does not resolve to the Reporting process owner.
