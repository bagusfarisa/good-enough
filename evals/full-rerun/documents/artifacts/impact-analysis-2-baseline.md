# Impact analysis: Return request expiry

After launch, return requests in **Awaiting customer documents** expire after seven calendar days in that status. Two decisions remain open for the launch discussion: whether the rule applies to requests already open on launch day and whether customers receive an expiry email.

## What changes for customers

Today, open return requests stay open indefinitely unless someone closes them. Under the new rule, the seven-day clock starts when a request enters **Awaiting customer documents**. When it expires, the customer sees **Expired** in the portal. The expired request stays closed, and the customer can submit a new return request.

Requests in **Internal review** are unaffected. Completed and cancelled records remain untouched.

**Example:** R-82 was created nine days ago and entered **Awaiting customer documents** two days ago. If the rule applies to R-82, it has **five calendar days left** in that status.

## Impact by team

| Team | Launch impact |
| --- | --- |
| Support | Explain why the portal shows **Expired** and guide the customer through submitting a new return request. Use the date the request entered **Awaiting customer documents** when explaining the deadline. |
| Operations | Use time in **Awaiting customer documents** to identify requests approaching expiry. Which requests are eligible to expire at launch depends on Product’s decision about requests already open. |
| Product | Decide whether to apply the rule to requests already open on launch day. If those requests are in scope, a return that has already spent seven calendar days in **Awaiting customer documents** would meet the expiry threshold at launch. |

## Open launch decisions

| Owner | Decision | Why it matters |
| --- | --- | --- |
| Product | Will the rule apply to return requests already open on launch day? | Determines which existing requests can expire and which customers Support may hear from at launch. |
| Communications | Will customers receive an expiry email? | Determines whether customers receive a direct notification in addition to the **Expired** status in the portal. |
