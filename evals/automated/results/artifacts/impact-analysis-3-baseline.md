# Return request expiry — launch impact analysis

Today, open return requests stay open until someone closes them. After launch, in-scope requests expire after seven calendar days in **Awaiting customer documents**. The seven days start when the request enters that status. The portal shows **Expired**, and the customer can submit a new return request. The expired request stays closed.

## Impact by team

| Team | What changes | Launch discussion |
| --- | --- | --- |
| Support | Customers who see **Expired** may ask how to continue their return. | Prepare guidance that explains the seven-day window and walks customers through submitting a new request. |
| Operations | In-scope requests in **Awaiting customer documents** can close automatically. Requests in **Internal review** are unaffected. Completed and cancelled records remain untouched. | Use the date the request entered **Awaiting customer documents** to determine how much time remains. Confirm which existing requests are in scope once Product decides. |
| Product | Applying the rule to requests already open on launch day would affect which customers can see **Expired** at rollout. | Decide whether to include requests already open on launch day. Coordinate with Communications on its separate decision about an expiry email. |

## Example

**R-82** was created nine days ago and entered **Awaiting customer documents** two days ago. If it is in scope, it has **five calendar days remaining** in that status.

## Open launch decisions

| Owner | Decision |
| --- | --- |
| Product | Will the rule apply to requests already open on launch day? |
| Communications | Will customers receive an email when a request expires? |
