# Returns expiry rollout | Support handoff

**Launch: May 12 at 09:00 UTC.** Check the launch tracker for the Product and Communications decisions before briefing agents. While Product’s decision is pending, requests already open at launch are excluded from automation. Tell affected customers their current request stays open and they can upload documents there.

## What to tell customers

| Request situation | Support guidance |
|---|---|
| Already open at launch, with Product’s decision still pending | Tell the customer to upload documents to their current request. Ask them to continue using that request. |
| Opened after launch and awaiting customer documents | The customer can upload documents to the current request before it expires. If documents arrive before expiry, the request leaves **Awaiting customer documents** and continues as usual. |
| Expired | The portal displays **Expired**. Direct the customer to submit a new return request in the portal. The original request stays closed. |

For requests opened after launch, count seven calendar days from entry into **Awaiting customer documents**. The next hourly automation run expires requests that reach the threshold and are still in that status. Requests in every other status are outside the rule.

## Decisions to check before launch

| Owner and deadline | Decision and handoff impact |
|---|---|
| **Elena, Product · May 8 at 12:00 UTC** | Decides whether automation applies to requests already open at launch. Some have already spent seven or more days awaiting documents. If included, they could expire on the first launch run and require customers to submit a new request. |
| **Nia, Communications · May 9 at 15:00 UTC** | Decides whether expiry also sends an email and records the decision in the launch tracker. The portal displays **Expired** either way. |

During the first week, Operations checks the exception queue each weekday at **16:00 UTC** and logs mismatches in the launch tracker.
