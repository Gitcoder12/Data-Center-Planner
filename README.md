# Data-Center-Planner
A flexible data center layout tool that evaluates deployment safety across any arbitrary environment, checking local thermal, structural, and resources capacity thresholds before approving cluster architecture.

---

## Project handbook

- [Activity log](ACTIVITY_LOG.md) · [Feature upgrade plan](FEATURE_UPGRADE_PLAN.md)
- [Company and team fit](COMPANY_FIT.md) · [README explanation draft](README_ADDENDUM_DRAFT.md)
- [README quality checklist](README_QUALITY_CHECKLIST.md)
- [Contributing](CONTRIBUTING.md) · [Agent instructions](AGENTS.md) · [Agent skills](SKILLS.md)

## Understanding the project

### In plain language

A small planning prototype that checks whether a proposed data-centre layout fits a set of resource and temperature assumptions.

### Technical and research view

Current implementation includes a small Python planner and sample configuration. The audit found temperature values generated with random.uniform(-2, 2), so they are synthetic, not live sensor measurements. The README's broad 'safety approval' language must not be read as engineering certification.

Document the configuration schema, units, formulae, random seed, threshold decisions and output format. Include a sample configuration with expected output.

For future work, see [FEATURE_UPGRADE_PLAN.md](FEATURE_UPGRADE_PLAN.md), [ACTIVITY_LOG.md](ACTIVITY_LOG.md), [COMPANY_FIT.md](COMPANY_FIT.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
