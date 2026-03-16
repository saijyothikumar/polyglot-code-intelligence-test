# Architecture Contract

## Expected Dependency Rules
- Frontend depends on backend via API boundaries only (simulated in frontend/api/*).
- Backend services depend on shared utilities and models; controllers -> services -> repositories -> models.
- Scripts depend on backend modules for migrations, seeding, and demo deploy.
- Tests may directly import services and repositories for coverage.
- Experiments are allowed to violate boundaries to create noisy graphs.

## Observed Deliberate Deviations
- Globals and singletons used in backend/__init__.py and app.py.
- Circular service touch-points (auth -> payments -> jobs) kept to stress analyzers.
- Dead code and unused imports remain intentionally.

## Guidance
- When adding new scenarios, update docs/architecture_overview.md and docs/api_design.md to keep expected vs. actual architecture aligned.
- Note any new boundary crossings so tooling comparisons remain meaningful.

## Defect Scenario Checklist
- Basic defects: unused imports, incorrect/missing imports (auth_repository, payments_service, users_repository).
- Architectural violations: controllers calling repositories directly (auth_controller, payments_controller); cross-service imports (payments_service -> AuthService, users_service -> AuthService).
- Edge cases: circular imports (circular_a/b), dynamic/conditional import in helpers.py.
- Dead code: unused_service.py, deprecated_utils.py, unused helper methods (users_service._admin_reset_user).
- Multi-language noise: Go (scripts/healthcheck.go), Java (experiments/LegacyJobRunner.java), C (backend/shared/legacy_helper.c).
- Data/config coverage: YAML, TOML, env.example, SQL schema/seed, JSON fixtures.
