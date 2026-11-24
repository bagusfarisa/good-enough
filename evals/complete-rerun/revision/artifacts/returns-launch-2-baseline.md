# Returns expiry rollout — Support launch-day handoff

**Launch** · May 12 at 09:00 UTC

## What to tell customers

| Request status | Support guidance |
|---|---|
| **Already open at launch, with Product’s decision pending** | These requests stay out of the automation. Tell customers their current request stays open and they can upload documents there. |
| **Awaiting customer documents, opened after launch** | Customers can upload documents to the current request before it expires. If documents arrive before expiry, the request moves out of that status and proceeds as usual. |
| **Expired** | The portal shows **Expired**. Tell customers to submit a new return request in the portal. The original request stays closed. |

## Decisions to confirm before the handoff

| Decision | Owner and deadline | What Support needs to know |
|---|---|---|
| Whether expiry applies to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | Keep these requests out of the automation while the decision is pending. If Product includes them, requests that have already spent seven or more days in **Awaiting customer documents** could expire on the first eligible run. |
| Whether expiry also triggers an email | Nia, Communications · May 9 at 15:00 UTC | Confirm the email decision in the launch tracker before advising customers about email. The portal shows **Expired** either way. |

## Expiry timing and launch monitoring

The automation runs hourly and only checks requests in **Awaiting customer documents**. For requests opened after launch, it counts seven calendar days from entry into that status and expires the request on the next hourly run once the threshold is reached.

During the first week, Operations checks the exception queue each weekday at 16:00 UTC and logs mismatches in the launch tracker.
