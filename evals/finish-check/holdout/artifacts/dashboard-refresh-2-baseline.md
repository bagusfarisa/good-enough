# Weekly territory dashboard refresh SOP

## 1. Prepare the Monday draft

1. Create a draft in the Refresh workspace. Keep the current dashboard live until the replacement passes validation and its publication slot begins.
2. Upload the approved roster and approved territory adjustment file. Retain both files with the draft for the publication log.
3. Check when the approved adjustment file arrived. If it arrived by **Monday at 11:30 UTC**, use the normal publication slot. If it arrived later, keep the current dashboard live, notify Sales Operations, and wait for the revised publication slot they confirm.

## 2. Validate the draft

1. Run **Validate**. It checks for blank account IDs, duplicate account IDs, and missing required columns.
2. If Validate flags any of these errors, stop the refresh, leave the draft unpublished, and request a corrected roster from Data Operations. Use the corrected roster they supply and leave upstream account ID corrections to them.
3. Once the corrected roster is available and the refresh is cleared to proceed, replace the roster in the draft and rerun **Validate**. Keep the existing adjustment file unless Sales Operations has supplied an approved replacement.

## 3. Publish and confirm

1. When **Validate reports zero errors** and the applicable publication slot has begun, select **Publish** once.
2. Open the published dashboard and compare its roster count with the count reported by Validate.
3. If the counts match, record the version, roster count, and publication time in the publication log. The refresh is complete.
4. If the counts differ, leave the version unconfirmed and send the version and both counts to Reporting Support. Wait for their response before marking the version complete.

Direct unresolved questions to the Reporting process owner.
