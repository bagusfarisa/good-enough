# Returns expiry rollout cross-functional working brief

## Project context

The returns lifecycle project is intended to reduce the number of stalled cases in the queue while giving customers another route to submit documentation. The portal and internal queue are separate surfaces. Support, Product, Communications, and Operations discussed the change at the launch checkpoint. This brief records the checkpoint decisions and the items that remain open.

The launch is May 12 at 09:00 UTC. The automation checks eligible requests hourly. It does not touch requests that are in any other status. In the first week Operations will check the exception queue each weekday at 16:00 UTC and log mismatches in the launch tracker.

## Portal treatment

The customer portal will display Expired when the automation closes a request. A customer can submit a new return request from the portal. An expired request stays closed. There is no plan to reopen the original request. The Communications owner, Nia, will decide by May 9 at 15:00 UTC whether expiry also sends an email. The portal label applies either way. Communications will update the launch tracker after deciding.

## Release criteria

The Product owner, Elena, will decide by May 8 at 12:00 UTC whether the rule applies to requests already open at launch. Any request in the historic queue that has already spent at least 10 calendar days in Awaiting customer documents would meet the expiry threshold at launch. Closing such a request at launch would immediately force the customer to start again. Until Elena decides, keep already-open requests out of the automation. Support should tell affected customers their current request stays open and they can upload documents there. Support must not tell them to start over while that decision is pending.

## Calculation rules

A request enters the eligible population when it enters Awaiting customer documents. Count 10 calendar days from entry into that status. If documents arrive before expiry, the request leaves that status and continues as usual. For requests opened after launch that reach the threshold, the next hourly run expires the request. The rule applies only to the Awaiting customer documents status.

## Summary for the launch meeting

The teams have prepared the new expiry rules for the portal and queue. Product will decide the scope for old requests, and Communications will decide how to announce expiry. Operations will track rollout problems. Returning customers can use the portal to start again when a request has expired.
