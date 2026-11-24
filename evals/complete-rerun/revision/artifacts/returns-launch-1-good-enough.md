# Returns expiry rollout — Support handoff

**Launch is May 12 at 09:00 UTC.** Before briefing the team, confirm whether Product has approved expiry for requests already open at launch. While that decision is pending, those requests stay out of the automation. Tell affected customers their current request stays open and they can upload documents there.

## What to tell customers

| Request status | Support guidance |
|---|---|
| **Awaiting customer documents** | Customers can upload documents to their current request. If the documents arrive before expiry, the request leaves this status and continues as usual. |
| **Expired** | The portal shows **Expired**. The original request stays closed. Customers can submit a new return request through the portal. |

For requests opened after launch, count **seven calendar days** from when the request enters **Awaiting customer documents**. Once the request reaches that threshold, the next hourly run expires it if it is still in that status. The automation applies only to **Awaiting customer documents**.

## Decisions to confirm before launch

| Decision | Owner and deadline | What Support needs to know |
|---|---|---|
| Whether expiry applies to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | Follow the pending-decision guidance above until Elena decides. Some existing requests have already waited seven days or more. If they are included and expire at launch, those customers will need to submit a new request. |
| Whether customers receive an expiry email | Nia, Communications · May 9 at 15:00 UTC | Check the launch tracker for Communications’ decision before telling customers to expect an email. The portal shows **Expired** either way. |

During the first week, Operations will check the exception queue each weekday at **16:00 UTC** and log mismatches in the launch tracker.
