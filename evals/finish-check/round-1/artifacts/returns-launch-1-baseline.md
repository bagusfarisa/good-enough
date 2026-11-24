# Returns expiry rollout — Support launch-day handoff

**Launch is May 12 at 09:00 UTC.** Before briefing the team, check the launch tracker for Product’s decision on requests already open at launch and Communications’ decision on expiry emails.

## What to tell customers

| Request status or situation | Support guidance |
|---|---|
| Already open at launch, with Product’s decision still pending | Keep these requests out of the automation. Tell customers their current request stays open and they can upload documents there. Ask them to continue with that request. |
| In **Awaiting customer documents** and still open | Tell the customer to upload documents to the current request. If the documents arrive before expiry, the request leaves that status and continues as usual. |
| **Expired** in the portal | Tell the customer they can submit a new return request in the portal. The original request stays closed. |

## When a request expires

The automation checks hourly and applies only to requests in **Awaiting customer documents**. Count seven calendar days from when the request entered that status. For requests opened after launch, the next hourly run after they reach seven days expires the request if it is still in that status. The portal then shows **Expired**, regardless of the email decision.

## Decisions and first-week monitoring

| Owner and deadline | What Support needs to know |
|---|---|
| Elena, Product · May 8 at 12:00 UTC | Decides whether the rule applies to requests already open at launch. Some have already waited seven days or more and could expire immediately if included. Until Elena decides, use the guidance above for requests already open at launch. |
| Nia, Communications · May 9 at 15:00 UTC | Decides whether expiry also sends an email. Communications will record the decision in the launch tracker. Confirm the decision before telling customers to expect an email. |
| Operations · 16:00 UTC each weekday during the first week | Checks the exception queue and logs mismatches in the launch tracker. |
