# Returns expiry rollout — Support launch-day handoff

**Launch is May 12 at 09:00 UTC.** Before briefing the team, check whether Product has decided if the rule covers requests already open at launch. While that decision is pending, those requests stay out of the automation. Tell affected customers their current request stays open and they can upload documents there. Ask customers to start a new request only after their original request has expired.

## What to tell customers

| What you see | What to tell the customer |
|---|---|
| The request was already open at launch and the Product decision is pending | “Your current request is still open. You can upload your documents there.” |
| The portal shows **Expired** | “Your original request is closed and will stay closed. You can submit a new return request in the portal.” |
| The customer submitted documents before expiry | The request leaves **Awaiting customer documents** and continues as usual. |

## When a request expires

The automation runs hourly and checks only requests in **Awaiting customer documents**. For requests opened after launch, count seven calendar days from entry into that status. If the request is still in that status at the threshold, it expires on the next hourly run. The portal shows **Expired** regardless of whether an email is sent.

## Decisions to confirm before the handoff

| Decision | Owner and deadline | Why it matters for Support |
|---|---|---|
| Whether to include requests already open at launch | Elena, Product · May 8 at 12:00 UTC | If included, requests that have already spent seven or more days waiting could expire at launch, requiring affected customers to submit a new request. |
| Whether expiry sends an email | Nia, Communications · May 9 at 15:00 UTC | Check the launch tracker before telling customers to expect an email. Communications will record the decision there. |

## First-week monitoring

Operations will check the exception queue each weekday at 16:00 UTC and log mismatches in the launch tracker.
