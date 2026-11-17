# Data-Center-Planner — India region and site planning

## Scope

This repository combines an existing rack/layout prototype with a published cloud-region inventory and a transparent site-screening methodology. It must not imply that cloud-region pins are individual data-centre buildings.

## Published India cloud footprints

See data/cloud_regions_india.json. The entries are sourced from official provider documentation:

- AWS India: Mumbai and Hyderabad regions; Delhi and Kolkata Local Zones. AWS lists three Availability Zones for each India region.
- Google Cloud: Mumbai (asia-south1) and Delhi (asia-south2).
- Azure: Central India (Pune), India South Central (Hyderabad), South India (Chennai) and West India (Mumbai). Availability-zone support differs by region; service support may differ further.

Sources: [AWS India](https://aws.amazon.com/local/india/), [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/), [Google Cloud locations](https://cloud.google.com/about/locations/), [Azure India regions](https://learn.microsoft.com/en-in/azure/reliability/regions-list).

**Map precision:** use city/region-level pins only. Cloud providers do not publish exact building addresses for every facility; do not invent exact coordinates or claim to map individual buildings.

## Site-planning layers

1. Power: available capacity, grid reliability, tariff, backup generation, renewable mix.
2. Cooling: dry-bulb/wet-bulb climate, cooling design, water stress and heat extremes.
3. Connectivity: diverse fibre paths, carrier choice, latency and route concentration.
4. Hazards: flood, seismic, cyclone, heat, fire and water risks.
5. Operations: land, permits, workforce, access, maintenance and supply chain.
6. Compliance: sovereignty, residency, sectoral requirements and customer obligations.

## Decision model

Keep published facts, measured site data and user assumptions in separate fields. Report missing values rather than substituting zero. Use a weighted multi-criteria score with sensitivity analysis; no score is an engineering certification. A human engineering review is required before site selection.

## Rack optimization

The rack optimizer now accepts an explicit power capacity and seeded random generator. Fitness and the rack evaluator can share one capacity value; identical seeds reproduce the same plan. It is a heuristic layout aid, not a structural, electrical or thermal certification.

Run the standard-library tests with:

    python -m unittest discover -s tests -v
