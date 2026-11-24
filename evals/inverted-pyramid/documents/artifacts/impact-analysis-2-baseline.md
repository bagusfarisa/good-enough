# Return request expiry — launch impact analysis

After launch, a return request in **Awaiting customer documents** will expire after seven calendar days in that status. The clock starts when the request enters the status. Today, an open request stays open indefinitely unless someone closes it.

## What happens to return requests

| Request status | Behavior after launch |
|---|---|
| Awaiting customer documents | After seven calendar days in the status, the portal shows **Expired**. The customer can submit a new return request, and the expired request stays closed. |
| Internal review | The expiry rule does not apply. |
| Completed or cancelled | Existing records remain unchanged. |

**Example.** R-82 was created nine days ago and entered **Awaiting customer documents** two days ago. It has five calendar days left before expiry if it is in scope at launch.

## Team impact

| Team | Launch impact |
|---|---|
| Support | Explain what **Expired** means, how to submit a new return request, and that the expired request stays closed. |
| Operations | Use the date the request entered **Awaiting customer documents** to determine when it expires. Product’s launch-day decision determines whether the rule applies to requests already open. |
| Product | Decide whether requests already open on launch day fall under the expiry rule. That decision determines which existing requests can expire. |

## Open launch decisions

| Owner | Decision |
|---|---|
| Product | Will the rule apply to requests already open on launch day? |
| Communications | Will customers receive an email when a request expires? |
