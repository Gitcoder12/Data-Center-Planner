# Data-Center-Planner
A flexible data center layout tool that evaluates deployment safety across any arbitrary environment, checking local thermal, structural, and resources capacity thresholds before approving cluster architecture. 


## Run the planner locally

This repository currently provides a Python command-line demonstration, not a browser website.

```bash
git clone https://github.com/Gitcoder12/Data-Center-Planner.git
cd Data-Center-Planner
python main.py
```

Run the command from the repository root because `main.py` reads `config.json` using a relative path. The temperature readings printed by the demo are synthetic samples, not live sensor telemetry. The scores are heuristic planning outputs, not engineering or site-safety certification.

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

## Examples Used
- Checking rack power capacity before placing servers
- Evaluating thermal and structural constraints in a data hall
- Comparing alternative rack layouts under resource limits
