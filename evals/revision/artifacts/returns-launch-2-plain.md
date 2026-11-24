# Returns expiry rollout — Support launch-day handoff

**Launch:** May 12 at 09:00 UTC

## How expiry works

For requests opened after launch, the seven-calendar-day clock starts when the request enters **Awaiting customer documents**. Once seven days have passed, the next hourly automation run closes the request if it is still in that status. If documents arrive before expiry, the request leaves that status and continues as usual. The automation applies only to **Awaiting customer documents**.

## What to tell customers

| Request state | Support guidance |
|---|---|
| Open and awaiting documents | “You can upload your documents to your current return request.” |
| Already open at launch, while Product’s decision is pending | “Your current return request stays open. You can upload your documents there.” |
| Expired | “Your return request has closed and will stay closed. You can submit a new return request through the portal.” |

The portal shows **Expired** when the automation closes a request, regardless of the email decision.

## Decisions to confirm before the handoff

| Owner and deadline | Decision | Until confirmed |
|---|---|---|
| Elena, Product · May 8 at 12:00 UTC | Whether expiry applies to requests already open at launch. Some have already spent seven or more days awaiting documents and could expire as soon as the rule applies. | Keep these requests out of the automation and direct customers to upload documents to their current request. |
| Nia, Communications · May 9 at 15:00 UTC | Whether expiry also triggers an email. Nia will record the decision in the launch tracker. | Use the portal status in customer guidance and avoid promising an email. |

## First-week monitoring

Operations will check the exception queue each weekday at 16:00 UTC and log mismatches in the launch tracker.
