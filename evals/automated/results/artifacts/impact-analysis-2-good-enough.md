# Return request expiry — launch impact analysis

At launch, a return request in **Awaiting customer documents** will expire after seven calendar days in that status. Today, open return requests stay open indefinitely unless someone closes them. The seven-day clock starts when the request enters **Awaiting customer documents**. After expiry, the customer can submit a new request, and the expired request stays closed.

## Impact by case

| Case | Current behavior | Launch impact |
|---|---|---|
| **Awaiting customer documents** | The request stays open unless someone closes it. | The request expires after seven calendar days in the status. Operations should use the status entry date to determine when expiry is due. |
| **Expired request** | Requests do not expire automatically. | The customer sees **Expired** in the portal. Support should explain how to submit a new request. |
| **Internal review** | The request stays open unless someone closes it. | The existing handling continues. |
| **Completed or cancelled** | The record is already completed or cancelled. | These records retain their existing status. |

**Example:** R-82 was created nine days ago and entered **Awaiting customer documents** two days ago. It has five calendar days left before expiry if the rule applies to it.

## Open launch decisions

| Owner | Decision | Why it matters |
|---|---|---|
| Product | Will the rule apply to requests already open on launch day? | Support and Operations need to know whether existing requests such as R-82 are in scope. |
| Communications | Will customers receive an expiry email? | Support needs to know whether customers will receive an email as well as see **Expired** in the portal. |
