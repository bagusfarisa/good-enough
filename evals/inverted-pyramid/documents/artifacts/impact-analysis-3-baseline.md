# Launch impact analysis: Return request expiry

After launch, a return request in **Awaiting customer documents** will expire after seven calendar days in that status. Today, open requests stay open indefinitely unless someone closes them.

## What changes for customers

The seven-day clock starts when the request enters **Awaiting customer documents**. A request’s creation date has no effect on its expiry date. When the request expires, the portal shows **Expired**. The customer can submit a new request, and the expired request stays closed.

Requests in **Internal review** are unaffected. Completed and cancelled records remain untouched.

**Example:** R-82 was created nine days ago and entered **Awaiting customer documents** two days ago. If R-82 is in scope, it has **five calendar days left** in that status before expiry.

## Impact by team

| Team | Launch impact |
| --- | --- |
| Support | Explain why the portal shows **Expired** and guide customers through submitting a new request. Use the date the request entered **Awaiting customer documents** when explaining the expiry timing. |
| Operations | Plan for requests in **Awaiting customer documents** to close after seven calendar days. The launch-day impact on the existing queue depends on Product’s decision about requests already open. |
| Product | Decide whether requests already open on launch day are in scope so Support and Operations can explain and apply the rollout consistently. |

## Open launch decisions

| Owner | Decision |
| --- | --- |
| Product | Will the expiry rule apply to requests already open on launch day? |
| Communications | Will customers receive an email when their request expires? The portal will show **Expired** regardless of the email decision. |
