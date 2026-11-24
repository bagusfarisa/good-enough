# May warehouse dispatch pilot approval brief

**Decision requested from the COO:** Reserve up to **$4,800 for Atlas** and record the decision in the normal decision register. The working group recommends a **May 18** start if both launch gates pass by their deadlines. The funding reservation and launch clearance are separate decisions.

The pilot covers the North warehouse weekday morning shift for two weeks. It tests a routing check for assignments that can be missed when the queue changes close to shift handover. Shift leaders keep manual review in place until launch and retain it as the fallback during the pilot.

## Launch gates

| Gate | Owner and deadline | Pass condition |
|---|---|---|
| Manual override drill | Priya, Safety · May 14 at 12:00 UTC | A shift leader can restore the manual dispatch queue within 10 minutes. |
| East-facing scanner feed test | Luis, Integrations · May 15 at 16:00 UTC | Every scan in the sample reaches Atlas exactly once. |

Each owner must explicitly approve their gate by the deadline. If either gate fails or misses its deadline, the warehouse continues manual dispatch.

## Options

| Option | Pilot cost | What it means for May 18 |
|---|---:|---|
| **Atlas** | **$4,800** | Can start May 18 if both gates clear. Exports the required timestamped audit log. |
| Beacon | $3,200 | Can export the required audit log starting June 8, so it misses the May 18 start requirement. |
| Continue manual dispatch | No pilot fee | Keeps the current process in place without the proposed routing check. |

## Checkpoint and continuation

At the next checkpoint, review both gate outcomes, pilot cost, audit coverage, and the decisions due after the pilot.

After two weeks, compare missed assignments during the pilot with the two preceding weeks. Continue only if missed assignments fall by at least **20%** and the audit log has **no gaps**. Any broader rollout requires a separate COO approval.
