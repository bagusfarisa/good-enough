# Weekly territory dashboard refresh SOP

Refresh the territory dashboard on Monday. Keep the current dashboard live until the replacement passes validation and its publication slot begins.

## 1. Prepare the draft and confirm the publication slot

Create a draft in the Refresh workspace. Use the approved roster and approved territory adjustment file. Retain both files with the draft for the publication log.

The approved adjustment file must arrive by **Monday at 11:30 UTC** to use the normal publication slot. If it misses the cutoff, keep the current dashboard live, notify Sales Operations, and wait for the revised publication slot they confirm.

## 2. Upload and validate the files

Upload both approved files to the draft and run **Validate**. It checks the roster for blank account IDs, duplicate account IDs, and missing required columns.

If Validate flags any of these errors, stop the refresh, keep the draft unpublished, and request a corrected roster from Data Operations. Use their corrected roster without editing account IDs by hand. If any account ID was blank, wait until the refresh is cleared to proceed before replacing the roster and rerunning Validate.

Replace the draft roster and rerun **Validate**. Keep the existing adjustment file in the draft unless Sales Operations provides an approved replacement. Proceed only when Validate reports zero errors.

## 3. Publish and verify

1. Once Validate reports zero errors and the applicable publication slot begins, select **Publish** once.
2. Open the published dashboard and compare its roster count with the count reported by Validate.
3. If the counts match, record the version, roster count, and publication time in the publication log. The refresh is complete.
4. If the counts differ, keep the version unconfirmed and send the version and both counts to Reporting Support. Wait for their response before marking the version complete. Record the publication details only once the counts match.

Direct questions this procedure leaves unresolved to the Reporting process owner.
