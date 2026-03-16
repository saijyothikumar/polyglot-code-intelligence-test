# API Design Notes

## Auth API (simulated)
- POST /auth/login -> tokens shaped like `token-<user>-<trace>`
- POST /auth/refresh -> `refresh-<token>`

## Users API (simulated)
- GET /users -> list users (id, email, disabled)
- GET /users/{id} -> returns masked_email alongside base fields

## Payments API (simulated)
- POST /payments/charge -> returns charge_id
- POST /payments/refund -> returns refund-<charge_id>

## Frontend Usage
- pages/loginPage.tsx uses loginForm -> authApi.login -> transport.simulateNetwork
- pages/dashboardPage.tsx uses userApi.listUsers -> transport.simulateNetwork

## Backend Expectations
- Controllers delegate to services; services call repositories and shared utils.
- Feature flags and settings loaded from configs (yaml/toml/env).

## Maintenance Note
- Keep this document in sync with any new endpoints or experimental APIs introduced during future test scenarios.
