# Returns expiry rollout | Support launch-day handoff

**Launch: May 12 at 09:00 UTC**

Before briefing the team, confirm Product’s decision on requests already open at launch and check the launch tracker for Communications’ email decision. Use the customer guidance below, and mention an expiry email only if Communications confirms it.

## What to tell customers

| Request state | Support guidance |
| --- | --- |
| Already open at launch, with the Product decision still pending | “Your current request stays open. You can upload your documents there.” Keep these requests out of the automation while the decision is pending. Do not ask customers to start over. |
| Awaiting customer documents and still open | The customer can upload documents to the current request. If the documents arrive before expiry, the request leaves that status and continues as usual. |
| Expired | The portal shows **Expired**. The original request stays closed. The customer can submit a new return request in the portal. |

## When requests expire

The automation checks hourly and applies only to requests in **Awaiting customer documents**. Count seven calendar days from the time the request enters that status. For requests opened after launch, the next hourly run after the threshold expires the request if it is still in that status.

## Decisions and first-week checks

| Owner | Deadline or schedule (UTC) | What Support needs to know |
| --- | --- | --- |
| Elena, Product | May 8 at 12:00 | Decides whether the rule covers requests already open at launch. Some have already spent seven or more days waiting, so including them could cause immediate expiry at launch and require customers to file again. |
| Nia, Communications | May 9 at 15:00 | Decides whether expiry also sends an email and records the decision in the launch tracker. The portal shows **Expired** either way. |
| Operations | Each weekday at 16:00 during the first week | Checks the exception queue and logs mismatches in the launch tracker. |
