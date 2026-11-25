# Rotate the production Billing API key

## Prerequisites

- Admin access to the Billing Portal.
- Access to the production secrets manager.

## Procedure

1. In the Billing Portal, go to **Settings > API Keys** and generate a new key.
2. Set `BILLING_API_KEY` to the new key in the production secrets manager and trigger a rolling restart.
3. After the restart, check `/health/billing`.
   - If it returns `200 OK`, proceed to step 4.
   - If it returns `401`, restore the previous key in `BILLING_API_KEY`, trigger another rolling restart to apply it, and alert On-Call Payments. Stop the rotation before revoking any key.
   - For any other result, pause the rotation and keep the old key active.
4. Revoke the old key in the Billing Portal.

## Completion check

Confirm the old key is revoked in the Billing Portal and `/health/billing` still returns `200 OK`.
