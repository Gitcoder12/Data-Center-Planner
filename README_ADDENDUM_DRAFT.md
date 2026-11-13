# Data-Center-Planner — README Explanation Draft

## In plain language

A small planning prototype that checks whether a proposed data-centre layout fits a set of resource and temperature assumptions.

## What the current tool does

The planner reads a configuration, evaluates a small set of capacity/thermal assumptions and produces an advisory result. Some values are generated for simulation rather than measured from a real facility.

## Technical explanation

Current implementation includes a small Python planner and sample configuration. The audit found temperature values generated with random.uniform(-2, 2), so they are synthetic, not live sensor measurements. The README's broad 'safety approval' language must not be read as engineering certification.

Document the configuration schema, units, formulae, random seed, threshold decisions and output format. Include a sample configuration with expected output.

## Limitations and safety

A simulation does not inspect a real building, rack, cooling loop, power feed or structural design. The result is not safety certification, commissioning approval or a substitute for qualified engineering review.

## Contributing

See FEATURE_UPGRADE_PLAN.md and CONTRIBUTING.md.
