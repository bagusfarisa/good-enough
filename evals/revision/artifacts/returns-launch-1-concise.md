# Returns expiry rollout — Support handoff

**Launch:** May 12 at 09:00 UTC

## What to tell customers

| Situation | Support guidance |
|---|---|
| The portal shows **Expired** | The original request stays closed. The customer can submit a new return request in the portal. |
| The request was already open at launch and Product’s decision is pending | The current request stays open. The customer can upload documents to that request. |
| The customer asks whether they’ll get an expiry email | Check the launch tracker before confirming. The portal shows **Expired** regardless of the email decision. |

## When requests expire

For requests opened after launch, count seven calendar days from entry into **Awaiting customer documents**. If the request is still in that status at the threshold, it expires on the next hourly run. If documents arrive before expiry, the request leaves that status and continues as usual. The automation applies only to **Awaiting customer documents**.

## Decisions to confirm before handoff

- **May 8 at 12:00 UTC — Elena (Product)** decides whether the rule applies to requests already open at launch. Keep those requests out of the automation while the decision is pending.
- **May 9 at 15:00 UTC — Nia (Communications)** decides whether expiry triggers an email and updates the launch tracker.

## First-week monitoring

Operations checks the exception queue each weekday at 16:00 UTC and logs mismatches in the launch tracker.
