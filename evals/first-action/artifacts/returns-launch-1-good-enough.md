# Returns expiry launch-day handoff for Support

**Launch is May 12 at 09:00 UTC.** Before briefing the team, check the launch tracker for the Product decision on requests already open at launch and the Communications decision on expiry emails.

- **Requests already open at launch.** While Elena’s decision is pending, these requests stay out of the automation. Tell affected customers their current request stays open and they can upload documents there. Ask them to continue with that request.
- **Requests that have expired.** The portal shows **Expired** whether or not an email is sent. Tell customers they can submit a new return request in the portal. The original request stays closed.

## When a request expires

The rule applies only to requests in **Awaiting customer documents**. Count seven calendar days from when the request entered that status. For requests opened after launch, the next hourly run at or after the seven-day mark expires the request if it is still in that status. If documents arrive before expiry, the request leaves that status and continues as usual.

## Launch decisions and first-week monitoring

| Item | Owner and timing | What Support needs to know |
|---|---|---|
| Apply the rule to requests already open at launch | Elena, Product · May 8 at 12:00 UTC | If included, requests that have already spent seven or more calendar days in **Awaiting customer documents** could expire on the first run. Once expired, the customer must submit a new request to continue. |
| Send an email when a request expires | Nia, Communications · May 9 at 15:00 UTC | Communications will record the decision in the launch tracker. |
| Review rollout exceptions | Operations · Each weekday of the first week at 16:00 UTC | Operations will check the exception queue and log mismatches in the launch tracker. |
