# Return request expiry impact analysis

After launch, return requests in **Awaiting customer documents** will expire after seven calendar days in that status. The clock starts when the request enters the status. Customers will see **Expired** in their portal and can submit a new request. The expired request stays closed.

**Launch-day decision.** Product still needs to decide whether the rule applies to requests already open on launch day. Operations needs that decision to determine whether existing requests in **Awaiting customer documents** are subject to expiry. Support needs it to answer questions about those requests.

## Impact by request status

| Request status | Today | After launch | Team action |
|---|---|---|---|
| Awaiting customer documents | The request stays open until someone closes it. | In-scope requests expire after seven calendar days in this status. The portal shows **Expired**. | Support explains how to submit a new request. Operations uses the status-entry date to determine when an in-scope request expires. |
| Internal review | The request stays open until someone closes it. | The request continues through the existing review process. | Operations continues the existing review process. |
| Completed or cancelled | The record is already closed. | The record retains its existing status. | No action required. |

**Example.** R-82 was created nine days ago and entered **Awaiting customer documents** two days ago. If it is in scope, it has five calendar days left before expiry.

## Launch decisions

| Owner | Open decision | Why it matters |
|---|---|---|
| Product | Does the rule apply to requests already open on launch day? | Determines which existing requests Operations should include and what Support tells those customers. |
| Communications | Will customers receive an expiry email? | Determines whether Support can tell customers to expect an email. The portal will show **Expired**. |
