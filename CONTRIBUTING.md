# Contributing

This repository is synthetic and intentionally contains defects. When adding scenarios:
- Keep new defects documented in ARCHITECTURE.md and docs/architecture_overview.md.
- Avoid fixing intentional bugs unless explicitly requested.
- Prefer small, focused additions that stress dependency graphs or language parsing.
- Update repo-map and codebase intention when structure changes.

## Workflow
1. Branch or fork.
2. Add scenario with minimal footprint.
3. Update docs and repo-map.
4. Run pytest (failures may be expected if introducing defects—note them in PR).
