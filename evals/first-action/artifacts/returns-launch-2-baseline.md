# Returns expiry rollout — Support launch-day handoff

**Launch is May 12 at 09:00 UTC.** Before briefing the team, check the launch tracker for the decision on requests already open at launch and the decision on expiry emails. The first determines what to tell customers with an open request. The second determines whether to mention an email.

## What to tell customers

| Request situation | Support guidance |
|---|---|
| The request was already open at launch and the Product decision is pending | Tell the customer their current request stays open and they can upload documents there. Ask them to continue with that request. |
| The request is still awaiting documents and is subject to the expiry rule | Ask the customer to upload documents to the current request. If documents arrive before expiry, the request leaves **Awaiting customer documents** and continues as usual. |
| The portal shows **Expired** | Tell the customer the original request stays closed. They can submit a new return request from the portal. |

## How expiry works

The automation runs hourly and checks only requests in **Awaiting customer documents**. It counts seven calendar days from entry into that status. For eligible requests opened after launch, the next hourly run after the threshold is reached closes the request and the portal shows **Expired**.

## Decisions to confirm before handoff

| Decision | Owner and deadline | What Support needs to know |
|---|---|---|
| Whether expiry applies to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | Keep these requests out of the automation while the decision is pending. If Product includes them, requests that have already waited seven or more calendar days in **Awaiting customer documents** could expire on the first run, requiring affected customers to submit a new request. |
| Whether expiry sends an email | Nia, Communications · May 9 at 15:00 UTC | Communications will record the decision in the launch tracker. Mention an expiry email only if the tracker confirms it. The portal shows **Expired** either way. |

## First-week monitoring

Operations will check the exception queue each weekday at 16:00 UTC and log mismatches in the launch tracker.
