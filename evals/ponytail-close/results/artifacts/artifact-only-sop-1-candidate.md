# Rotate the production Billing API key

## Prerequisites

- Admin access to the Billing Portal
- Access to the production secrets manager

## Procedure

1. In the Billing Portal, go to **Settings → API Keys** and generate a new key.
2. Update `BILLING_API_KEY` in the production secrets manager with the new key and trigger a rolling restart. Keep the previous key available for rollback.
3. After the restart, check `/health/billing`. Proceed to step 4 only if it returns `200 OK`.
   - If it returns `401`, restore the previous value of `BILLING_API_KEY`, trigger a rolling restart to apply it, and alert On-Call Payments. Leave both keys active.
4. Revoke the old key in the Billing Portal.

## Completion check

Confirm that the old key is revoked in the Billing Portal and that `/health/billing` still returns `200 OK`.
