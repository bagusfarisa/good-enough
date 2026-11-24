# Returns expiry rollout | Support launch-day handoff

**Launch May 12 at 09:00 UTC.** Before briefing the team, confirm whether Product has approved expiry for requests already open at launch and check the launch tracker for the email decision. Until Product decides, already-open requests stay out of the automation. Tell affected customers to upload documents to their current request.

| Launch decision | Owner and deadline | What Support should do |
|---|---|---|
| Whether expiry applies to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | Confirm the scope with Elena. If she includes these requests, customers whose requests have already spent seven or more calendar days in **Awaiting customer documents** could have their requests expire at launch and need to submit a new one. |
| Whether expiry sends an email | Nia, Communications · May 9 at 15:00 UTC | Check the launch tracker for Nia’s decision before telling customers to expect an email. The portal shows **Expired** either way. |

## What to tell customers

- **The request is still open and awaiting documents.** Ask the customer to upload documents to their current request. If the documents arrive before expiry, the request leaves **Awaiting customer documents** and continues as usual.
- **The portal shows Expired.** Tell the customer to submit a new return request in the portal. The original request stays closed.

## How to check when a request expires

For requests opened after launch, count seven calendar days from when the request entered **Awaiting customer documents**. The next hourly run expires the request if it is still in that status. The automation leaves requests in all other statuses alone.

During the first week, Operations will check the exception queue each weekday at 16:00 UTC and log mismatches in the launch tracker.
