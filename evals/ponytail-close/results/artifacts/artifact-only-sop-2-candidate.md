# Rotate the production Billing API key

## Prerequisites

- Admin access to the Billing Portal
- Access to the production secrets manager

## Procedure

1. In the Billing Portal, go to **Settings → API Keys** and generate a new key.
2. Set `BILLING_API_KEY` to the new key in the production secrets manager and trigger a rolling restart.
3. After the restart, check `/health/billing` for `200 OK`. If it returns `401`, restore the previous value of `BILLING_API_KEY`, alert On-Call Payments, and stop before revoking any key. For any other result besides `200 OK`, stop and leave the old key active.
4. Once `/health/billing` returns `200 OK`, revoke the old key in the Billing Portal.

## Completion check

Confirm `/health/billing` still returns `200 OK` and the Billing Portal shows the old key as revoked.
