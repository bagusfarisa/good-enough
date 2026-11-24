# COO decision brief: May warehouse dispatch pilot

**Decision requested:** Reserve up to **$4,800** for Atlas. Record the funding decision in the decision register. Launch on **May 18** only if both gate owners explicitly approve by their deadlines.

## Recommendation

Pilot Atlas for two weeks on the weekday morning shift at the North warehouse. Queue changes near shift handover can cause missed route assignments. Atlas can start May 18 and export the required timestamped audit log. Beacon costs $3,200 but cannot export the required log until June 8. Continuing manual dispatch avoids a pilot fee and leaves the proposed routing check untested.

## Launch gates

| Gate | Owner | Approval deadline | Pass criterion |
|---|---|---|---|
| Manual override drill | Priya, Safety | May 14, 12:00 UTC | A shift leader restores the manual dispatch queue within 10 minutes. |
| East-facing scanner feed test | Luis, Integrations | May 15, 16:00 UTC | Every scan in the sample reaches Atlas exactly once. |

Shift leaders keep manual review in place until launch and available as a fallback during the pilot. If either gate fails or lacks explicit approval by its deadline, continue manual dispatch.

## Checkpoint and continuation

At the next checkpoint, review both gate results, cost, audit coverage, and the decisions due after the pilot.

After two weeks, compare missed assignments with the two weeks before launch. Continue only if missed assignments fall by **at least 20%** and the audit log has **no gaps**. Any broader rollout requires separate COO approval.
