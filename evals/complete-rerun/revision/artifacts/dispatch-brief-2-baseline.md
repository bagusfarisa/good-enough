# May warehouse dispatch pilot

## Decision for the COO

**Reserve up to $4,800 for Atlas. Authorize launch on May 18 only if both launch gates below receive explicit approval by their deadlines.** If either gate fails or misses its deadline, continue manual dispatch. Record the decision in the normal decision register.

The pilot will run for two weeks on the weekday morning shift at the North warehouse. It will test a routing check for assignments that can be missed when the queue changes close to shift handover. Shift leaders will keep manual review in place until launch and available as the fallback throughout the pilot.

## Options

| Option | Pilot cost | Trade-off |
|---|---:|---|
| **Atlas** | **$4,800** | Can start May 18 and exports the required timestamped audit log. |
| Beacon | $3,200 | Can export the required audit log starting June 8, after the May 18 start requirement. |
| Continue manual dispatch | $0 pilot fee | Leaves the warehouse without the proposed routing check. |

## Launch gates

| Gate | Owner and deadline | Evidence required for approval |
|---|---|---|
| Manual override drill | Priya, Safety · May 14 at 12:00 UTC | A shift leader restores the manual dispatch queue within 10 minutes. |
| East-facing scanner feed test | Luis, Integrations · May 15 at 16:00 UTC | Every scan in the sample reaches Atlas exactly once. |

## Checkpoint and continuation

At the next checkpoint, review both gate results, cost, audit coverage, and the decisions due after the pilot.

After two weeks, compare the number of missed assignments with the preceding two weeks. Continue only if missed assignments fell by at least 20% and the audit log has no gaps. Any broader rollout requires a separate COO approval.
