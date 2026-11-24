# COO decision brief: May warehouse dispatch pilot

**Decision requested.** Reserve up to **$4,800** for the Atlas pilot. The working group recommends Atlas for a **May 18** start if both launch gates pass by their deadlines. Record the COO’s funding decision in the normal decision register. Launch authorization depends on both gate approvals.

The pilot covers the **North warehouse weekday morning shift for two weeks**. It tests whether a routing check reduces missed assignments when the queue changes near shift handover. Shift leaders continue manual review until launch and keep it available as the fallback during the pilot.

## Launch gates

| Gate | Owner and deadline | Required result |
|---|---|---|
| Manual override drill | Priya, Safety · May 14 at 12:00 UTC | A shift leader can restore the manual dispatch queue within 10 minutes. |
| East-facing scanner feed test | Luis, Integrations · May 15 at 16:00 UTC | Every scan in the sample reaches Atlas exactly once. |

Each owner must explicitly approve their gate by the deadline. If either gate fails or lacks approval at its deadline, continue manual dispatch.

## Options

| Option | Pilot cost | Trade-off |
|---|---:|---|
| Atlas | $4,800 | Can start May 18 if both gates pass and can export a timestamped audit log. |
| Beacon | $3,200 | Can export the required audit log starting June 8, after the required May 18 start. |
| Continue manual dispatch | No pilot fee | The warehouse continues without the proposed routing check. |

## Checkpoint and continuation

At the next checkpoint, review both gate results, pilot cost, audit coverage, and the decisions needed after the pilot.

After two weeks, compare missed assignments during the pilot with the two preceding weeks. Continue only if missed assignments fall by **at least 20%** and the audit log has **no gaps**. Any broader rollout requires separate COO approval.
