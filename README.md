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

## Examples Used
- Checking rack power capacity before placing servers
- Evaluating thermal and structural constraints in a data hall
- Comparing alternative rack layouts under resource limits


---

## Comparison with Existing Open-Source Projects

Data-Center-Planner is described as a layout-planning prototype that checks rack placement against thermal, structural and resource constraints. The following projects provide adjacent data-centre simulation and optimization references.

| Project | Established focus | Relationship to Data-Center-Planner |
|---|---|---|
| [OpenDC](https://github.com/atlarge-research/opendc) | Data-centre simulation for infrastructure and workload research | A broader simulation environment; Data-Center-Planner's documented scope is a more focused rack/layout constraint and optimization tool. |
| [CloudSim](https://github.com/Cloudslab/cloudsim) | Modelling and simulation of cloud-computing infrastructure and resource allocation | A cloud-resource simulation framework; Data-Center-Planner emphasizes physical rack/site constraints rather than cloud workload scheduling alone. |
| [Google OR-Tools](https://github.com/google/or-tools) | Constraint programming, routing and combinatorial optimization | A mature optimization toolkit; Data-Center-Planner packages a domain-specific rack-layout problem and evaluation rules. |

### Where Data-Center-Planner is different
- **Physical-layout constraints:** the concept brings rack capacity, thermal and structural checks into one planning workflow.
- **Optimization-oriented layout:** the current design uses an optimizer to explore alternative rack placements under configured limits.
- **Arbitrary-environment intent:** the stated goal is to support configurable site constraints rather than one fixed data-hall template.

### Where established projects are stronger
OpenDC and CloudSim have broader simulation models and research ecosystems; OR-Tools offers mature constraint-solving methods. The current implementation audit found a hard-coded 80 kW threshold that can disagree with configurable planner capacity, plus missing input validation and reproducibility controls.

### Engineering evidence and limitations
Use one validated configuration for all constraints, seed stochastic optimization, and test boundary cases and constraint satisfaction. Record units, sensor/source data and assumptions. Treat outputs as planning aids, not structural, electrical, thermal or regulatory certification. This is a scope comparison, not an optimization-quality benchmark.
