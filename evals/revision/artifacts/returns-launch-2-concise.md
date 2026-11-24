# Returns expiry rollout — Support handoff

**Launch:** May 12 at 09:00 UTC

## What Support should tell customers

| Request status | What to tell the customer |
|---|---|
| **Expired** in the portal | The original request stays closed. Submit a new return request in the portal. |
| **Already open at launch, while Product’s decision is pending** | Your current request stays open. Upload your documents there. |

## When a request expires

The automation runs hourly and applies only to requests in **Awaiting customer documents**. For requests opened after launch, expiry happens on the first run once seven calendar days have elapsed since the request entered that status. If documents arrive before expiry, the request leaves that status and continues as usual.

## Decisions to confirm before launch

| Owner | Deadline (UTC) | Decision and interim handling |
|---|---|---|
| Elena, Product | May 8 at 12:00 | Decide whether the rule covers requests already open at launch. Keep those requests out of the automation while the decision is pending. Some have already reached the seven-day threshold and could expire on the first run if included. |
| Nia, Communications | May 9 at 15:00 | Decide whether expiry also triggers an email and record the decision in the launch tracker. The portal displays **Expired** either way. |

## First-week monitoring

Operations checks the exception queue each weekday at 16:00 UTC and logs mismatches in the launch tracker.
