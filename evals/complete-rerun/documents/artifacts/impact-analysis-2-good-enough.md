# Return requests expire after seven days awaiting customer documents

After launch, an in-scope return request will expire after seven calendar days in **Awaiting customer documents**. The clock starts when the request enters that status. The customer will see **Expired** in the portal and can submit a new return request. The expired request stays closed.

## Decisions for the launch discussion

| Owner | Open decision | Why it matters |
|---|---|---|
| Product | Does the rule apply to requests already open on launch day? | Support and Operations need the answer before applying the seven-day rule to existing requests. |
| Communications | Will customers receive an expiry email? | Support needs to know whether to mention an email when explaining what customers will see. The portal will show **Expired** either way. |

## Impact by request status

| Status | Today | After launch | Team action |
|---|---|---|---|
| Awaiting customer documents | Stays open indefinitely unless someone closes it. | In-scope requests expire after seven calendar days in this status. | Operations uses the status entry date to determine time remaining. Support explains how to submit a new return request after expiry. |
| Internal review | Stays open indefinitely unless someone closes it. | The expiry rule does not apply. | Operations continues the existing review process. |
| Completed or cancelled | Records are already closed. | Existing records stay as they are. | No action needed. |

**Example.** R-82 was created nine days ago and entered **Awaiting customer documents** two days ago. If it is in scope, it has five calendar days left before expiry. If it is already open on launch day, Product’s decision determines whether the rule applies.
