# Returns expiry launch-day handoff

The rollout starts **May 12 at 09:00 UTC**. Before briefing the team, check the launch tracker for Product’s decision on requests already open at launch and Communications’ decision on expiry emails. **While Product’s decision is pending, keep already-open requests out of the automation.** Tell affected customers their current request stays open and they can upload documents there.

## What to tell customers

| Request state | Support guidance |
|---|---|
| Already open at launch and Product’s decision is pending | “Your current return request is still open. You can upload your documents there.” |
| Portal shows **Expired** | “This request is closed and will stay closed. You can submit a new return request from the portal.” |
| Documents arrive before expiry | The request leaves **Awaiting customer documents** and continues as usual. |

For requests opened after launch, the seven-calendar-day clock starts when the request enters **Awaiting customer documents**. If it is still in that status when it reaches seven days, the next hourly run expires it. The automation applies only to that status.

## Decisions to check before launch

| Decision | Owner and deadline | What Support needs to know |
|---|---|---|
| Whether expiry applies to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | Some requests have already waited seven days or more. If included, they could expire on the first run and customers would need to submit a new request. |
| Whether expiry sends an email | Nia, Communications · May 9 at 15:00 UTC | Communications will record the decision in the launch tracker. The portal shows **Expired** either way. |

During the first week, Operations will check the exception queue each weekday at **16:00 UTC** and log mismatches in the launch tracker.
