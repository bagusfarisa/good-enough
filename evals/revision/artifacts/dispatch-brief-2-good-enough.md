# May warehouse dispatch pilot

**Decision requested:** Reserve up to **$4,800** for a two-week Atlas pilot at the North warehouse on the weekday morning shift, starting May 18. The working group recommends Atlas because it can meet the May 18 start date and export the required timestamped audit log.

**Launch condition:** Launch only if both owners explicitly approve their tests by the deadlines below. If either test fails or approval is late or missing, continue manual dispatch. Record the COO’s funding decision in the normal decision register.

## Launch gates

| Gate | Owner and deadline | Pass criterion |
|---|---|---|
| Manual override drill | Priya, Safety · May 14, 12:00 UTC | A shift leader restores the manual dispatch queue within 10 minutes. |
| East-facing scanner feed test | Luis, Integrations · May 15, 16:00 UTC | Every scan in the sample reaches Atlas exactly once. |

Shift leaders keep manual review in place until launch and retain it as the fallback during the pilot.

## Options considered

| Option | Pilot fee | Decision trade-off |
|---|---:|---|
| Atlas | $4,800 | Can start May 18 and export the required timestamped audit log. |
| Beacon | $3,200 | Can export the required audit log starting June 8, which misses the May 18 start requirement. |
| Continue manual dispatch | No pilot fee | Dispatch can still miss route assignments when the queue changes close to shift handover. The proposed routing check would remain unavailable. |

## Post-pilot decision

Compare missed route assignments during the two-week pilot with the two preceding weeks. Continue only if missed assignments fall by at least 20% and the audit log has no gaps. Any broader rollout requires a separate COO approval.

At the next checkpoint, review both gate outcomes, pilot cost, audit coverage, and the decisions due after the pilot.
