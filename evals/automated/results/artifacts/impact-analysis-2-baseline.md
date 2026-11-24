# Impact analysis · Expiry while awaiting customer documents

After launch, in-scope returns will expire after **seven calendar days in Awaiting customer documents**. Today, open return requests stay open indefinitely unless someone closes them. Product still needs to decide whether the rule applies to requests already open on launch day.

## What changes for customers

| Request state | Behavior after launch |
|---|---|
| Awaiting customer documents | The seven-day clock starts when the request enters this status. |
| Expired | The portal shows **Expired**. The customer can submit a new request, and the expired request stays closed. |
| Internal review | The request continues through the existing review process. |
| Completed or cancelled | The existing records are preserved. |

**Example · R-82** was created nine days ago and entered Awaiting customer documents two days ago. It has **five calendar days left** if it is in scope. Use the date it entered that status to calculate the deadline.

## Impact by team

| Team | Launch impact |
|---|---|
| Support | Explain why the portal shows **Expired** and guide the customer through submitting a new return request. Use the date the request entered Awaiting customer documents when explaining the deadline. |
| Operations | Account for expiry when managing returns awaiting customer documents. Launch-day handling of already-open requests depends on Product’s decision. |
| Product | Decide whether already-open requests are in scope and confirm that decision with Support and Operations so they can handle launch-day cases consistently. |

## Open launch decisions

| Owner | Decision | Why it matters |
|---|---|---|
| Product | Will the rule apply to requests already open on launch day? | Determines whether requests such as R-82 are subject to the expiry clock. |
| Communications | Will customers receive an expiry email? | Determines whether customers get an email in addition to seeing **Expired** in the portal. |
