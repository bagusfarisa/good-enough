# Rotate the production Billing API key

## Prerequisites

- Admin access to the Billing Portal
- Access to the production secrets manager

## Procedure

1. In the Billing Portal, go to **Settings > API Keys** and generate a new key.
2. Replace `BILLING_API_KEY` in the production secrets manager with the new key and trigger a rolling restart.
3. After the restart, check `/health/billing`. Proceed only if it returns `200 OK`.
   - If it returns `401`, restore the previous value of `BILLING_API_KEY`, alert On-Call Payments, and stop. Leave both keys active.
4. In the Billing Portal, revoke the old key.

## Completion check

Confirm the old key is revoked in the Billing Portal and `/health/billing` still returns `200 OK`.
