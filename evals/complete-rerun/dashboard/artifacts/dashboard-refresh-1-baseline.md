# Weekly territory dashboard refresh SOP

Refresh the territory dashboard on Monday. Keep the currently published dashboard live until the replacement passes validation and its publication slot begins. The approved territory adjustment file must arrive by **Monday at 11:30 UTC** to use the normal publication slot.

## 1. Prepare the draft

Create a draft in the Refresh workspace. Upload the approved roster and the approved territory adjustment file when each is available. Retain the approved files used for publication with the draft for the publication log.

If the adjustment file arrives after the cutoff, keep the last published dashboard live and notify Sales Operations. Wait for Sales Operations to confirm a revised publication slot, then wait until that slot begins before publishing.

## 2. Validate the roster

With both approved files in the draft, run **Validate**. It checks for blank account IDs, duplicate account IDs, and missing required columns.

- **Blank account ID.** Stop the refresh, keep the draft unpublished, and ask Data Operations for a corrected roster. Resume once the corrected roster is available and the refresh is cleared to proceed.
- **Duplicate account IDs or missing required columns.** Ask Data Operations for a corrected roster before proceeding.

Use the roster supplied by Data Operations and leave upstream account ID corrections to that team. Replace the roster in the draft, keep the adjustment file unless Sales Operations supplies a replacement, and rerun **Validate**.

## 3. Publish and verify

1. When **Validate** reports zero errors and the applicable publication slot begins, select **Publish** once.
2. Open the published dashboard and compare its roster count with the count reported by **Validate**.
3. If the counts match, record the version, roster count, and publication time in the publication log. This completes the refresh.
4. If the counts differ, keep the version unconfirmed. Send the version and both counts to Reporting Support and wait for their response before marking the version complete.

Direct questions this SOP leaves unresolved to the Reporting process owner.
