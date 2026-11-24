# Decision brief for the COO: May warehouse dispatch pilot

**Decision requested.** Reserve up to **$4,800** for a two-week Atlas pilot starting **May 18** at the North warehouse on the weekday morning shift. Record the funding decision in the normal decision register. Launch requires both owners to approve their tests by the deadlines below.

## Recommendation

Use Atlas to test whether a routing check reduces missed assignments when the dispatch queue changes close to shift handover.

| Option | Pilot cost | Basis for decision |
| --- | ---: | --- |
| Atlas | $4,800 | Can start May 18 and exports the required timestamped audit log. |
| Beacon | $3,200 | Can export the required audit log from June 8, after the May 18 start requirement. |
| Current manual process | No pilot fee | Dispatch continues without the proposed routing check. |

## Launch gates

| Gate | Accountable owner | Approval deadline | Pass criterion |
| --- | --- | --- | --- |
| Manual override drill | Priya, Safety | May 14, 12:00 UTC | A shift leader restores the manual dispatch queue within 10 minutes. |
| East-facing scanner feed test | Luis, Integrations | May 15, 16:00 UTC | Every scan in the sample reaches Atlas exactly once. |

If either test fails or its owner misses the approval deadline, the warehouse continues manual dispatch. Shift leaders keep manual review in place until launch and available as the fallback throughout the pilot.

## Checkpoint and continuation

At the next checkpoint, review both launch gates, pilot cost, audit coverage, and the decisions due after the pilot.

After two weeks, compare missed assignments during the pilot with the two preceding weeks. Continue only if missed assignments fall by **at least 20%** and the audit log has **no gaps**. Any broader rollout requires a separate COO approval.
