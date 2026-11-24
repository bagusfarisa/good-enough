# Weekly territory dashboard refresh handoff notes

## Preparation

The analyst updates the territory dashboard on Monday. Keep the currently published dashboard available until a replacement passes the refresh checks. Create a draft in the Refresh workspace and retain the approved roster and adjustment files with the draft for the publication log.

## Missing account IDs

Validate checks the roster for blank account IDs, duplicate account IDs, and required columns. If any account ID is blank, stop the refresh and ask Data Operations for a corrected roster. Keep the affected draft unpublished. When the corrected roster is available and the refresh is cleared to proceed, replace the draft roster and rerun Validate. Leave adjustments in the draft unless Sales Operations has supplied a replacement.

If Validate flags duplicate IDs or missing required columns, get a corrected roster from Data Operations and rerun Validate after replacing the draft roster. Use the roster provided by Data Operations. The analyst does not repair upstream roster IDs by hand.

## Adjustment file after the cutoff

The approved territory adjustment file must arrive by Monday at 11:30 UTC for the normal publication slot. If it arrives later, keep the last published dashboard live. Notify Sales Operations, which will confirm a revised publication slot. The analyst waits for the revised slot before publishing the replacement.

## Normal refresh and publication

Upload the approved roster and approved adjustment file into the draft. Run Validate. After Validate reports zero errors and the applicable publication slot begins, select Publish once. Open the published dashboard and compare its roster count with the count reported by Validate. Record the version, roster count, and publication time in the publication log only if the counts match. For a mismatch, keep the version unconfirmed and send the version and both counts to Reporting Support. Wait for their response before marking the version complete.

## Ownership

Data Operations owns roster corrections. Sales Operations owns adjustment approvals and revised publication slots. The Reporting process owner handles questions these instructions leave unresolved.
