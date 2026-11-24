# Decision brief for the May warehouse dispatch pilot

**Decision requested.** Reserve up to **$4,800** for a two-week Atlas pilot starting **May 18**, limited to the **North warehouse weekday morning shift**. The working group recommends Atlas because it can meet the start date and export the required timestamped audit log. Record the funding decision in the normal decision register.

**Launch only if both owners approve their tests by the deadlines below.** The funding decision is separate from launch authorization. If either test fails or its deadline passes without explicit approval, continue manual dispatch, even if the other test passes.

| Launch gate | Owner | Approval deadline | Pass condition |
|---|---|---|---|
| Manual override drill | Priya, Safety | May 14 at 12:00 UTC | A shift leader restores the manual dispatch queue within 10 minutes. |
| East-facing scanner feed test | Luis, Integrations | May 15 at 16:00 UTC | Every scan in the sample reaches Atlas exactly once. |

Shift leaders keep manual review in place until the pilot starts. Manual review remains available as the fallback throughout the pilot.

## Options

Dispatch can miss a route assignment when the queue changes close to shift handover. The pilot tests whether a routing check reduces missed assignments.

| Option | Pilot fee | Trade-off |
|---|---:|---|
| Atlas | $4,800 | Can start May 18 and exports a timestamped audit log. Launch depends on both approvals above. |
| Beacon | $3,200 | Can export the required audit log starting June 8, so it misses the May 18 start requirement. |
| Continue manual dispatch | $0 | Avoids a pilot fee and leaves dispatch without the proposed routing check. |

## Checkpoint and post-pilot decision

At the next checkpoint, review both gate decisions, cost, audit coverage, and the criteria for continuing after the pilot.

After two weeks, compare missed assignments during the pilot with the two preceding weeks. Continue only if missed assignments fall by **at least 20%** and the audit log has **no gaps**. Any broader rollout requires a separate COO approval.
