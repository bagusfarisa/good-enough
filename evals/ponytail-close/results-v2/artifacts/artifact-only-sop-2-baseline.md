# Rotate the Billing Portal API key

## Prerequisites

- Admin access to the Billing Portal
- Access to the production secrets manager

## Procedure

1. In the Billing Portal, go to **Settings > API Keys** and generate a new key.
2. In the production secrets manager, set `BILLING_API_KEY` to the new key and trigger a rolling restart.
3. After the restart, check `/health/billing`. Proceed to step 4 only if it returns `200 OK`.
   - If it returns `401 Unauthorized`, restore `BILLING_API_KEY` to the previous key, alert On-Call Payments, and stop before revoking either key.
4. Revoke the old key in the Billing Portal.

## Completion check

Confirm the old key shows as revoked in the Billing Portal and `/health/billing` still returns `200 OK`.
