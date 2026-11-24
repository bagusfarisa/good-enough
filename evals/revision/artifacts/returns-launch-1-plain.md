# Returns expiry rollout · Support launch-day handoff

**Launch: May 12 at 09:00 UTC**

Before briefing the team, check the launch tracker for the decisions on requests already open at launch and customer expiry emails. Use the pending guidance below until each decision is confirmed.

## What to tell customers

| Customer’s situation | Support guidance |
| --- | --- |
| The portal shows **Expired** | “This return request is closed. You can submit a new return request from the portal.” The original request stays closed. |
| The request was already open at launch and Product’s decision is pending | “Your current request stays open. You can upload your documents there.” |
| The customer asks whether they’ll receive an expiry email | Check the Communications decision in the launch tracker before confirming whether an email is sent. The portal shows **Expired** either way. |

## How expiry works

- For requests opened after launch, the seven-calendar-day countdown starts when the request enters **Awaiting customer documents**.
- If documents arrive before expiry, the request leaves that status and continues as usual.
- Once an eligible request reaches seven calendar days, the next hourly run closes it. The automation applies only to requests in **Awaiting customer documents**.

## Decisions to confirm before launch

| Decision | Owner and deadline | Support impact |
| --- | --- | --- |
| Whether to include requests already open at launch | Elena, Product · May 8 at 12:00 UTC | These requests stay out of the automation while the decision is pending. Some have already waited seven or more calendar days and could expire at launch if included. |
| Whether expiry sends a customer email | Nia, Communications · May 9 at 15:00 UTC | Communications will record the decision in the launch tracker. The portal label applies either way. |

## First-week monitoring

Operations will check the exception queue each weekday at **16:00 UTC** and log mismatches in the launch tracker.
