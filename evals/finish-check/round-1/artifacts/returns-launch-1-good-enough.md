# Returns expiry rollout — Support launch-day handoff

**Launch is May 12 at 09:00 UTC.** Check the launch tracker for Elena’s decision on requests already open at launch. While that decision is pending, those requests stay outside the automation. Tell affected customers their current request stays open and they can upload documents there.

## What to tell customers

| Request state | Support guidance |
| --- | --- |
| Already open at launch | Follow Elena’s scope decision once confirmed. While it’s pending, direct customers to upload documents to their current request. |
| Opened after launch and awaiting documents | Customers can upload documents to the current request before it expires. If documents arrive before expiry, the request leaves **Awaiting customer documents** and continues as usual. |
| Expired in the portal | The original request stays closed. Customers can submit a new return request in the portal. |

## When requests expire

The automation checks eligible requests hourly. For requests opened after launch, it counts seven calendar days from entry into **Awaiting customer documents**. The next hourly run after the request reaches that threshold expires it if it is still in that status. The automation applies only to **Awaiting customer documents**.

## Decisions and first-week monitoring

| Owner | Timing | Handoff detail |
| --- | --- | --- |
| Elena, Product | May 8 at 12:00 UTC | Decide whether already-open requests are in scope. Some have already spent seven or more days awaiting documents and could expire at launch if included, requiring customers to submit a new request. |
| Nia, Communications | May 9 at 15:00 UTC | Decide whether expiry also triggers an email. Communications will update the launch tracker with the decision. The portal displays **Expired** either way. |
| Operations | Each weekday of the first week at 16:00 UTC | Check the exception queue and log mismatches in the launch tracker. |
