# Rotate the Billing API key

## Prerequisites

- Admin access to the Billing Portal
- Access to the production secrets manager

## Procedure

1. In the Billing Portal, open **Settings > API Keys** and generate a new key.
2. Update `BILLING_API_KEY` in the production secrets manager with the new key and trigger a rolling restart.
3. After the restart, check `/health/billing`. Continue only if it returns `200 OK`. If it returns `401`, restore the previous key in the secrets manager, alert On-Call Payments, and stop before revoking either key.
4. In **Settings > API Keys**, revoke the old key.

## Completion check

Confirm that `/health/billing` returns `200 OK` and the Billing Portal shows the old key as revoked.
