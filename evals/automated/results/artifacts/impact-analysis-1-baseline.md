# Impact analysis: Return requests awaiting customer documents

After launch, an in-scope return request expires once it has spent seven calendar days in **Awaiting customer documents**. The customer sees **Expired** in the portal and can submit a new return request. The expired request stays closed.

## What changes

Today, open return requests stay open indefinitely unless someone closes them. Under the new rule, the seven-day countdown starts when a request enters **Awaiting customer documents**. Requests in **Internal review** are unaffected, and completed and cancelled records remain untouched.

**Example.** R-82 was created nine days ago and entered **Awaiting customer documents** two days ago. If R-82 is in scope, it has five calendar days left before expiry.

## Impact by team

| Team | Launch impact |
| --- | --- |
| **Support** | Explain what **Expired** means, when the seven-day countdown starts, and how to submit a new return request. Make clear that the expired request stays closed. |
| **Operations** | Expect requests to close automatically after seven calendar days in **Awaiting customer documents**. Use the date the request entered that status to determine when it expires. The impact on the launch-day backlog depends on Product’s scope decision. |
| **Product** | Decide whether the rule applies to requests already open on launch day. This determines whether customers with existing requests can see those requests expire under the new rule. |

## Open launch decisions

| Owner | Decision | Why it matters |
| --- | --- | --- |
| **Product** | Will the rule apply to requests already open on launch day? | Support and Operations need to know which existing requests can expire. |
| **Communications** | Will customers receive an expiry email? | The portal will show **Expired**. The email decision determines whether customers also receive an email when their request expires. |
