# AISDF Release Readiness

## Current release posture
This repository is a substantial specification and validation foundation. It is not a hosted runtime, certified agent platform or production-proven software delivery system.

## Mandatory public-release decisions
- Select and apply an OSI-compatible license if open-source distribution is intended; obtain appropriate legal review for project needs.
- Identify maintainers and configure a monitored security disclosure contact.
- Review third-party assets, trademarks, dependencies and attribution.
- Confirm contribution, governance and release authority.

## Technical gates
- Repository validator passes.
- All JSON Schemas pass Draft 2020-12 meta-validation.
- Valid and invalid fixtures are tested against each schema.
- Markdown links resolve.
- CI runs on a clean checkout.
- At least one reference project completes the lifecycle with reproducible evidence.
- Adapter claims are backed by exact tool/version/plan/environment evidence.

## Claims policy
Do not advertise a numeric 10/10 or production readiness as a verified fact. Publish the evaluation rubric, evidence, limitations and date instead.
