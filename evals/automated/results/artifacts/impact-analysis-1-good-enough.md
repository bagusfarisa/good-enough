# Return request expiry launch impact

Returns in **Awaiting customer documents** will expire after seven calendar days in that status. The clock starts when the request enters the status. Customers will see **Expired** in the portal and can submit a new return request. The expired request stays closed.

## Launch decisions

| Owner | Open decision | Why it matters |
|---|---|---|
| Product | Will the rule apply to requests already open on launch day? | The decision determines whether Operations should expect requests already awaiting documents to expire under the new rule. |
| Communications | Will customers receive an expiry email? | Support needs to know whether to mention an email when explaining what customers can expect. The portal will show **Expired** either way. |

## Impact by request status

| Status | Today | After launch | Team impact |
|---|---|---|---|
| Awaiting customer documents | The request stays open indefinitely unless someone closes it. | An in-scope request expires after seven calendar days in this status. | Operations uses the status-entry date to determine when expiry is due. Support explains the expired status and how to submit a new request. |
| Internal review | The request stays open indefinitely unless someone closes it. | The expiry rule does not apply. | Operations continues its current review process. |
| Completed or cancelled | The record is already completed or cancelled. | The record retains its current status. | No action is needed. |

**Example.** R-82 was created nine days ago and entered **Awaiting customer documents** two days ago. If it is in scope, it has five calendar days left before expiry.
