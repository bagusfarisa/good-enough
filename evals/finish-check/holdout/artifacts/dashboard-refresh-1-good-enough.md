# Weekly territory dashboard refresh

Run the refresh on Monday. Keep the last published dashboard live until the replacement passes validation and the applicable publication slot begins.

## Prerequisites

- Obtain the approved roster from Data Operations and the approved territory adjustment file from Sales Operations.
- Create a draft in the Refresh workspace. Keep the approved files with the draft for the publication log.

## Refresh and publish

1. **Confirm the publication slot.** If the approved adjustment file arrives by Monday at 11:30 UTC, use the normal publication slot. If it arrives after the cutoff, keep the last published dashboard live, notify Sales Operations, and wait for them to confirm a revised slot. Use that slot in step 4.
2. **Upload both approved files** to the draft.
3. **Run Validate.** It checks for blank account IDs, duplicate account IDs, and missing required columns. Continue to step 4 only when Validate reports zero errors.
   - **Blank account IDs.** Stop the refresh, keep the draft unpublished, and ask Data Operations for a corrected roster. Once the correction is available and the refresh is cleared to proceed, replace the roster and rerun step 3. Keep the adjustment file in the draft unless Sales Operations supplies a replacement.
   - **Duplicate account IDs or missing required columns.** Get a corrected roster from Data Operations, replace the roster in the draft, and rerun step 3.
   - Use the corrected roster supplied by Data Operations. Leave upstream ID corrections to them.
4. **Publish once** when Validate reports zero errors and the slot from step 1 has begun.
5. **Verify the published version.** Open the published dashboard and compare its roster count with the count reported by Validate.
   - **Counts match.** Record the version, roster count, and publication time in the publication log. The refresh is complete.
   - **Counts differ.** Keep the version unconfirmed and send Reporting Support the version and both counts. Wait for their response before marking the version complete. Record the publication only after the counts match.

If a roster correction makes you miss the applicable slot, ask the Reporting process owner which slot to use before proceeding to step 4. Direct other unresolved procedure questions to the same owner.
