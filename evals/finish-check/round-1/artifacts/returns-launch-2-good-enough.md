# Returns expiry launch-day handoff

**Launch: May 12 at 09:00 UTC**

Before briefing the team, check the launch tracker for two decisions. The scope decision determines what agents should tell customers with requests already open at launch.

| Decision | Owner and deadline | Support guidance |
|---|---|---|
| Do requests already open at launch fall under the expiry rule? | Elena, Product · May 8 at 12:00 UTC | While the decision is pending, keep these requests out of the automation. Tell affected customers their current request stays open and they can upload documents there. Ask customers to start a new request only after the original has expired. |
| Will expiry also trigger an email? | Nia, Communications · May 9 at 15:00 UTC | Check the tracker before confirming whether an expiry email is sent. Communications will update it after the decision. The portal displays **Expired** either way. |

If Elena includes already-open requests, customers whose requests have already spent seven or more calendar days in **Awaiting customer documents** could have to start again at launch.

## What agents should tell customers

| Request state | What to tell the customer |
|---|---|
| Still awaiting documents | Upload the documents to the current request. If the documents arrive before expiry, the request leaves **Awaiting customer documents** and continues as usual. |
| **Expired** in the portal | Submit a new return request through the portal. The original request stays closed. |

For requests opened after launch, count seven calendar days from entry into **Awaiting customer documents**. The automation checks hourly and expires requests on the next run after they reach the threshold, provided they are still in that status. All other statuses are outside the rule.

## First-week monitoring

Operations checks the exception queue each weekday at 16:00 UTC and logs mismatches in the launch tracker.
