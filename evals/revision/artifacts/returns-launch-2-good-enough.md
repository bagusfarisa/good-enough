# Returns expiry rollout — Support launch-day handoff

**Launch: May 12 at 09:00 UTC.** Before briefing the team, confirm Elena’s decision on requests already open at launch. While that decision is pending, keep those requests out of the automation. Tell affected customers their current request stays open and they can upload documents there.

## What to tell customers

| Request state | Support guidance |
| --- | --- |
| Already open at launch and Product’s decision is pending | “Your current request is still open. You can upload your documents there.” |
| Eligible and awaiting customer documents | “Upload your documents to your current request before it expires. If we receive them before expiry, your request continues as usual.” |
| Expired | “Your original request is closed. You can submit a new return request in the portal.” The portal shows **Expired** and the original request stays closed. |

## When a request expires

For requests opened after launch, count **seven calendar days** from entry into **Awaiting customer documents**. The next hourly run after the request reaches that threshold expires it if it is still in that status. If documents arrive before expiry, the request leaves that status and continues as usual. The automation only applies to **Awaiting customer documents**.

## Launch decisions to confirm

| Owner and deadline | Decision and effect on Support |
| --- | --- |
| **Elena, Product** · May 8 at 12:00 UTC | Decide whether to include requests already open at launch. Some have already waited seven days or more and could expire on the first run if included, requiring customers to start a new request. Use the pending-decision guidance above until Elena decides. |
| **Nia, Communications** · May 9 at 15:00 UTC | Decide whether expiry also triggers an email and record the decision in the launch tracker. The portal shows **Expired** either way. Check the tracker before telling customers to expect an email. |

During the first week, **Operations** will check the exception queue each weekday at **16:00 UTC** and log mismatches in the launch tracker.
