# Returns expiry rollout — launch-day Support handoff

**Launch is May 12 at 09:00 UTC.** Before briefing the team, confirm Elena’s decision on requests already open at launch and check the launch tracker for Nia’s decision on expiry emails.

| Launch decision | Owner and deadline | Support guidance |
| --- | --- | --- |
| Whether expiry applies to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | While the decision is pending, keep these requests out of the automation. Tell affected customers their current request stays open and they can upload documents there. Ask them to continue with that request. |
| Whether expiry sends a customer email | Nia, Communications · May 9 at 15:00 UTC | Confirm the decision in the launch tracker, which Communications will update. Until then, avoid promising an email. The portal displays **Expired** either way. |

## What to tell customers

- **The portal shows Expired.** The original request stays closed. The customer can submit a new return request from the portal.
- **The request is still open and awaiting documents.** The customer can upload documents to the current request. If the documents arrive before expiry, the request leaves **Awaiting customer documents** and continues as usual.

## When a request expires

For requests opened after launch, count seven calendar days from entry into **Awaiting customer documents**. If the request is still in that status at the threshold, the next hourly run expires it. The automation only acts on requests in that status.

Elena’s decision determines whether the rule also applies to requests already open at launch. If those requests are included, any that have already spent seven or more calendar days in **Awaiting customer documents** could expire on the first run, requiring customers to start a new request.

## First-week exception checks

Operations checks the exception queue each weekday at 16:00 UTC during the first week and logs mismatches in the launch tracker.
