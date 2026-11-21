# AISDF Workforce

The workforce is a catalogue of specialist responsibilities, not a claim that every role is an autonomous agent. It includes team directories, human-readable role contracts and machine-readable worker manifests.

## Teams
- Product and research
- UX and design
- Architecture
- Frontend
- Mobile
- Backend
- Data and database
- AI/ML and agents
- Security
- Quality engineering
- Platform and operations
- Specialized engineering

## How routing works
A task declares a worker ID, action, dependencies, acceptance criteria, budget and approval requirement. The registry verifies the worker exists and that the requested action is permitted by its manifest. The runtime validates dependency DAGs and stores plan/audit records. Actual execution requires a separately configured adapter or human operator.

## Maturity
L1_DEFINED: role contract exists. L2_EXECUTABLE: runtime adapter can execute bounded tasks. L3_VERIFIED: contract and behavior tests pass. L4_OPERATIONAL: monitoring, recovery, security controls and production evidence exist. The bundled role catalogue is L1_DEFINED; the local control-plane primitives are executable. Do not conflate the two.
