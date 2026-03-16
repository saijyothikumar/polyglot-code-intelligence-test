# Polyglot Code Intelligence Test Repo

Synthetic, intentionally flawed repository to stress-test code indexing, dependency graphing, and AI code analysis tools.

## Contents
- Backend (Python): auth, users, payments, jobs services; shared utils/models; intentional circular imports, unused/dead code.
- Frontend (TypeScript/React): components, pages, API shims calling simulated backend transport.
- Scripts: deploy stub, migrations, seed data, Go healthcheck.
- Configs: YAML/TOML/env/logging samples.
- Data: SQL schema/seed plus JSON fixtures.
- Tests: pytest suites hitting backend services.
- Experiments: messy Python/Java scripts for clustering noise.
- Multi-language extras: Go, Java, C snippets for parser coverage.

## Known Intentional Issues
- Circular imports (helpers, circular_a/b), missing/incorrect imports, unused imports.
- Architectural violations (controllers reaching repositories, cross-service imports).
- Dead code paths and unreferenced modules (deprecated_utils, unused_service).
- Weak security (MD5 hashing), globals for wiring, lax error handling.

## How to Run Examples
- Backend demo: `python backend/main.py`
- Seed/migrate: `python scripts/migrate_db.py` then `python scripts/seed_data.py`
- Deploy stub: `bash scripts/deploy.sh` (non-production)
- Frontend: static files only; uses `frontend/api/transport.ts` to simulate network.
- Tests: `pytest tests` (expected to surface intentional quirks).

## Purpose
Use this repo to benchmark:
- Dependency resolution across languages and layers
- Detection of dead code, unused imports, and missing modules
- Architecture conformance vs. documented expectations (see ARCHITECTURE.md, docs/*)
- Clustering accuracy with noisy experiments and mixed-language files

## Maintenance
Update docs/architecture_overview.md, docs/api_design.md, and ARCHITECTURE.md whenever new scenarios are added so expected vs. actual graphs stay aligned.

# Example Queries

Questions AI systems should attempt:

1. Detect circular dependencies
2. Identify dead code
3. Find unused imports
4. Build dependency graph
5. Trace cross-language references
