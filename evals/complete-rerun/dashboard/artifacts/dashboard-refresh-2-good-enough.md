# Weekly territory dashboard refresh SOP

Refresh the territory dashboard each Monday. Keep the last published dashboard live until the replacement passes validation and its publication slot begins. The approved territory adjustment file must arrive by **Monday at 11:30 UTC** to use the normal publication slot. If it arrives after the cutoff, notify Sales Operations and wait for the revised slot they confirm.

## Prepare the draft

1. Create a draft in the Refresh workspace.
2. Upload the approved roster and the approved territory adjustment file. Retain both files with the draft for the publication log.

## Validate and resolve roster errors

Run **Validate**. It checks for blank account IDs, duplicate account IDs, and missing required columns.

- **Blank account IDs.** Stop the refresh, keep the draft unpublished, and request a corrected roster from Data Operations. Once the corrected roster is available and the refresh is cleared to proceed, replace the roster in the draft and rerun **Validate**. Keep the existing adjustments unless Sales Operations has supplied a replacement.
- **Duplicate account IDs or missing required columns.** Request a corrected roster from Data Operations. Replace the roster in the draft and rerun **Validate**.

Use the roster supplied by Data Operations for all corrections. Do not edit upstream roster IDs by hand. If a blank-ID stop overlaps with a late adjustment file, ask the Reporting process owner to confirm when validation can resume. The draft still requires zero validation errors and the start of the revised slot before publication.

## Publish and confirm

1. Once **Validate** reports zero errors and the applicable publication slot has begun, select **Publish** once.
2. Open the published dashboard and compare its roster count with the count reported by **Validate**.
3. If the counts match, record the version, roster count, and publication time in the publication log. The refresh is complete.
4. If the counts differ, keep the version unconfirmed and send the version and both counts to Reporting Support. Wait for their response before marking the version complete.
