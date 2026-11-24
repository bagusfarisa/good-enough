# Returns expiry rollout · Support launch-day handoff

Launch is **May 12 at 09:00 UTC**. Before briefing agents, check Elena’s decision on requests already open at launch and the launch tracker for Nia’s decision on expiry emails.

## What agents should tell customers

| Customer’s situation | Support guidance |
| --- | --- |
| The request was already open at launch and Elena’s decision is pending | Tell the customer their current request stays open and they can upload documents there. Keep these requests out of the automation and hold off on asking customers to start over. |
| The portal shows **Expired** | Tell the customer the original request stays closed. They can submit a new return request through the portal. |
| Documents arrive before the request expires | The request leaves **Awaiting customer documents** and continues as usual. |

## How expiry works

For requests opened after launch, count **seven calendar days** from when the request enters **Awaiting customer documents**. The next hourly run after the request reaches that threshold expires it if it is still in that status. All other statuses are outside the rule.

## Decisions to check before launch

| Decision | Owner and deadline | What Support needs to know |
| --- | --- | --- |
| Whether expiry applies to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | Confirm the scope before advising affected customers. Some existing requests have already waited seven days or more and could expire at launch if included, requiring customers to submit a new request. |
| Whether expiry also sends an email | Nia, Communications · May 9 at 15:00 UTC | Communications will record the decision in the launch tracker. The portal shows **Expired** either way. |

During the first week, Operations will check the exception queue each weekday at **16:00 UTC** and log mismatches in the launch tracker.
