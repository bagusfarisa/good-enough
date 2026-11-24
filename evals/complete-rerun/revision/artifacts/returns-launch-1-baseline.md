# Returns expiry launch-day Support handoff

**Launch is May 12 at 09:00 UTC.** At handoff, confirm whether Product approved applying expiry to requests already open at launch. While that decision is pending, those requests stay outside the automation. Tell affected customers their current request stays open and they can upload documents there. Ask customers to start a new request only after their original request has expired.

## What Support should tell customers

| Request status | Support guidance |
| --- | --- |
| Already open at launch, with the Product decision pending | “Your current request is still open. You can upload your documents there.” |
| Awaiting customer documents and still open | Direct the customer to upload documents to their current request. If the documents arrive before expiry, the request leaves this status and continues as usual. |
| Expired | “Your original request is closed and will stay closed. You can submit a new return request through the portal.” The portal displays **Expired** whether or not an email is sent. |

## How expiry works

The automation checks hourly and applies only to requests in **Awaiting customer documents**. Count seven calendar days from the time the request enters that status. For requests opened after launch, the next hourly run after the seven-day threshold expires the request if it is still in that status.

## Decisions and first-week monitoring

| Owner | Deadline or schedule | What Support needs to know |
| --- | --- | --- |
| Elena, Product | May 8 at 12:00 UTC | Confirm whether requests already open at launch are in scope. If included, requests already at or past seven days in **Awaiting customer documents** could expire on the first run. |
| Nia, Communications | May 9 at 15:00 UTC | Check the launch tracker for Nia’s decision on whether expiry also sends a customer email. |
| Operations | Each weekday at 16:00 UTC during the first week | Operations checks the exception queue and logs mismatches in the launch tracker. |
