# Architecture Overview

## Modules
- Backend (Python): auth, users, payments, jobs, shared (utils, models)
- Frontend (TypeScript/React): components, pages, api
- Scripts: deploy.sh, migrate_db.py, seed_data.py
- Tests: pytest suites referencing backend services
- Experiments: messy scripts for clustering stress

## Relationships (intended vs. actual)
- Frontend depends on backend HTTP APIs (simulated via api/* and transport.ts).
- Backend controllers call services; services call repositories; repositories use models.
- Shared utilities (logger, helpers, models, security) are imported across backend modules.
- Scripts invoke backend modules (migrations, seed, deploy runner).
- Tests import backend.create_app and touch services directly.
- Experiments intentionally bypass architecture and import random modules to create loose edges.

## Known Architectural Quirks
- Globals used for wiring in backend/__init__.py and app.py.
- Circular touch-points: auth_service -> payments_service; payments_service -> jobs_service -> queue.
- Dead code and unused helpers left in place for static analysis.

## Maintenance Note
- Update these docs whenever new test scenarios or modules are added so expected architecture stays aligned with the evolving dependency graph.

## Defect Scenario Checklist (summary)
- Unused/incorrect/missing imports in services and repositories.
- Controllers bypassing services to hit repositories (auth_controller, payments_controller).
- Cross-service imports creating boundary violations (payments_service, users_service).
- Circular/dynamic imports (circular_a/b, helpers.py conditional import).
- Dead/unused modules (unused_service.py, deprecated_utils.py) and private dead methods.
- Mixed-language artifacts (Go/Java/C) to exercise parsers.
