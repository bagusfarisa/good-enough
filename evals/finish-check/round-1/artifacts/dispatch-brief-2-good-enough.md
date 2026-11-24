# May 18 warehouse dispatch pilot approval

**Decision for the COO:** Reserve up to **$4,800 for Atlas** for a two-week pilot on the weekday morning shift at the North warehouse. Record the decision in the normal decision register. Launch on May 18 only if both owners approve their launch gates by the deadlines below. If either gate fails or misses its approval deadline, continue manual dispatch.

## Launch gates

| Gate | Owner and approval deadline | Pass criterion |
|---|---|---|
| Manual override drill | Priya, Safety · May 14 at 12:00 UTC | A shift leader restores the manual dispatch queue within 10 minutes. |
| East-facing scanner feed test | Luis, Integrations · May 15 at 16:00 UTC | Every scan in the sample reaches Atlas exactly once. |

Shift leaders keep manual review in place until launch and available as the fallback throughout the pilot.

## Options

Dispatch can miss route assignments when the queue changes near shift handover. The pilot tests whether a routing check reduces those misses.

| Option | Pilot cost | May 18 start and audit coverage |
|---|---:|---|
| **Atlas** | **$4,800** | Can start May 18 if both gates clear. Exports a timestamped audit log. |
| Beacon | $3,200 | Can export the required audit log starting June 8, after the required launch date. |
| Manual dispatch | No pilot fee | Can continue immediately. Leaves the handover risk in place without the proposed routing check. |

## Decision after the pilot

Compare missed assignments during the two-week pilot with the preceding two weeks. Continue only if missed assignments fall by **at least 20%** and the audit log has **no gaps**. Any broader rollout requires separate COO approval.

At the next checkpoint, review both gate outcomes, cost, audit coverage, and the decisions due after the pilot.
