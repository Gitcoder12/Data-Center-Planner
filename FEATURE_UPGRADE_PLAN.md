# Data-Center-Planner — Feature Upgrade Plan

## Objective

A small planning prototype that checks whether a proposed data-centre layout fits a set of resource and temperature assumptions.

## P0 — truthful, deterministic model

- [ ] Label every random temperature and capacity value as synthetic; make simulation seeds reproducible.
- [ ] Validate configuration schema, units, numeric ranges and required fields before scoring.

## P1 — explainable planning

- [ ] Document thermal/structural/resource formulas and make thresholds configurable.
- [ ] Add deterministic tests for boundary cases, missing fields and invalid units.

## P2 — evidence and real data integration

- [ ] Add measured-vs-simulated data adapters only with documented sensor provenance.
- [ ] Benchmark layouts against known synthetic scenarios and sensitivity tests.

## Contributor work packages

1. Config schema and input validation.
2. Thermal/resource scoring specification.
3. Deterministic tests with fixed seeds and known expected results.
4. Measured data adapter with source provenance and failure behavior.

## Definition of done

- [ ] Inputs have units and ranges.
- [ ] Synthetic data is labelled and deterministic.
- [ ] Score rationale and thresholds are inspectable.
- [ ] Outputs are advisory; no engineering certification is implied.
