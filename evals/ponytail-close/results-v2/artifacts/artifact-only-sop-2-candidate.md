# Rotate the Billing API key

## Prerequisites

- Admin access to the Billing Portal
- Access to the production secrets manager

## Procedure

1. In the Billing Portal, go to **Settings → API Keys** and generate a new key.
2. Replace `BILLING_API_KEY` in the production secrets manager with the new key and trigger a rolling restart.
3. After the restart, check `/health/billing`. Proceed to step 4 only if it returns `200 OK`. If it returns `401 Unauthorized`, restore the previous key in the secrets manager, trigger a rolling restart to apply it, alert On-Call Payments, and stop before revoking either key.
4. Revoke the old key in the Billing Portal.

## Completion check

Confirm that the old key is revoked in the Billing Portal and `/health/billing` still returns `200 OK`.
