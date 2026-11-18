# Data-Center-Planner
A flexible data center layout tool that evaluates deployment safety across any arbitrary environment, checking local thermal, structural, and resources capacity thresholds before approving cluster architecture. 


---

## AI-maintained project notes (secondary — 2026-11-13)

This section supplements the maintainer-authored README above; it does not replace or certify the original claims.

- The source tree and executed tests are the implementation source of truth. Planned features and draft PRs are not shipped functionality.
- Preserve original engineering inputs and data. Never silently replace real records with fabricated or synthetic examples; isolate and label fixtures.
- Record units, source, collection date, assumptions and validation protocol for engineering datasets and simulations.
- Verify setup, test results and technical claims against the exact current commit before public use.
- See [MODEL_AUDIT_ROUTER.md](MODEL_AUDIT_ROUTER.md) for independent review and data-integrity rules.

---

## Engineering Audit & Handover — 2026-11-17

**Reviewed commit:** `44b1402d5fd71312b199a27e9302fd5f3a2c27aa` (`main`). Static inspection covered `genetic_optimizer.py` and `planner.py`; tests were not executed.

### Confirmed findings
- `RackOptimizer._fitness()` hardcodes an 80 kW per-slot threshold, while `DataCenterRackPlanner` exposes a configurable `power_capacity_kw`. The optimizer can therefore disagree with the planner when configured capacity differs from 80 kW.
- The optimizer uses the global random generator without an injected seed, so results are not reproducible by configuration.
- The constructor does not validate `max_slots`, `population_size`, rack records, or power values. Empty/invalid configurations can fail during chromosome generation or mutation.
- Area/rack scoring uses simple fixed thresholds; it is a heuristic planning aid, not an engineering certification or site-suitability assessment.

### Next actions
1. Pass one validated power-capacity configuration into both optimizer and rack evaluator.
2. Inject a seeded random generator and validate population size, slot count, and rack schema.
3. Add tests for capacity boundaries, empty inputs, invalid data, reproducibility, and constraint satisfaction.

**Verification status:** static source inspection only; optimization quality, tests, and real facility data remain unverified.


---

## Branch Activity & Development History

**Audit date:** 2026-11-18 · **Comparison base:** `main`

| Branch | Difference from `main` | Observed work / changed paths |
|---|---:|---|
| `docs/portfolio-operating-kit-2026-11-13` | 5 ahead / 5 behind | Activity log, agent guidance, worklog, company-fit notes, contributor guide, feature plan and README support docs |
| `docs/project-status-2026-11-16-data-center-planner` | 1 / 2 | Project status snapshot: `PROJECT_STATUS.md` |
| `feat/region-site-planner` | 6 / 1 | India cloud-region dataset, site-planning docs, genetic optimizer, CI and optimizer tests |

### Open pull requests observed during this audit

- [PR #3 — project status snapshot](https://github.com/Gitcoder12/Data-Center-Planner/pull/3)

**Review note:** The site-planning branch changes optimization logic and regional input data. Validate source provenance, constraints and optimizer tests before merging. No branches have been merged or deleted by this documentation update.
