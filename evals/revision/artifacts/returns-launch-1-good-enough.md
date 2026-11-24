# Returns expiry rollout — Support handoff

**Launch is May 12 at 09:00 UTC.** Before briefing the team, confirm whether Product has approved expiry for requests already open at launch. **While that decision is pending, keep those requests out of the automation.** Tell affected customers their current request stays open and they can upload documents there. Ask customers to start a new request only after their original request has expired.

| Decision to confirm | Owner and deadline | What Support needs to know |
| --- | --- | --- |
| Whether expiry applies to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | Confirm the scope before changing customer guidance. Some requests have already spent seven or more days awaiting documents and could expire at launch if included. |
| Whether expiry sends a customer email | Nia, Communications · May 9 at 15:00 UTC | Check the launch tracker for Nia’s decision before advising customers about email. The portal shows **Expired** either way. |

## What to tell customers

| Request state | Customer guidance |
| --- | --- |
| Already open at launch and the scope decision is pending | “Your current request stays open. You can upload your documents there.” |
| Awaiting customer documents and eligible for expiry | “Upload your documents before the request expires so it can continue. The expiry window is based on when your request entered **Awaiting customer documents**.” |
| Expired | “Your original request stays closed. You can submit a new return request in the portal.” |

## How expiry works

For requests opened after launch, count seven calendar days from when the request enters **Awaiting customer documents**. The automation runs hourly and expires a request on the next run after it reaches the threshold, provided it is still in that status. If documents arrive before expiry, the request leaves that status and continues as usual. All other statuses are outside the rule.

## First-week exception checks

Operations checks the exception queue each weekday at 16:00 UTC during the first week and logs mismatches in the launch tracker.
