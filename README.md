# Intent and Constraint Evolution Protocol (ICEP)

Intent and Constraint Evolution Protocol (ICEP) is an open coordination-plane
protocol that defines how multiple agents evolve a shared world-state through
intents, constraints, evidence, simulation, and arbitration.

ICEP addresses a fundamental problem in multi-agent systems:

> When many agents act in parallel, coordination must be state-based and
> constraint-driven, not conversation-driven.

---

## Why ICEP Exists

Agent systems can now propose changes faster than humans can coordinate them.
Traditional workflows rely on tickets, branches, and reviews to serialize work.
That model breaks down when:

- Multiple agents operate on the same system at the same time
- Intent conflicts are discovered too late
- Communication replaces verifiable coordination

ICEP replaces conversation-centric coordination with explicit state evolution.

---

## What ICEP Is

ICEP is:

- A protocol, not a product
- A coordination plane, not a workflow
- A world-state evolution model, not a messaging format

ICEP defines:

- How agents declare intents
- How constraints are applied and verified
- How simulations produce evidence
- How an arbiter selects an accepted future

---

## What ICEP Is Not

ICEP is not:

- An agent communication protocol
- A human authority or governance model
- A CI/CD replacement
- A consensus or voting system
- A productivity tool

For details, see `non-goals.md`.

---

## Core Concepts

ICEP introduces a small set of agent-native primitives:

- World-State Graph
- Intent Declaration
- Constraint / Invariant
- Evidence
- Simulation (Counterfactual)
- Parallel Futures
- Arbiter
- Accepted State

These terms are defined in `terminology.md`.

---

## Design Principles

ICEP is built on the following principles:

1. State before communication
2. Constraints are system physics
3. Parallel futures over serialized branches
4. Verification over negotiation
5. Deterministic arbitration

Any implementation that violates these principles is not ICEP-compliant.

---

## Protocol Overview

ICEP defines a minimal set of protocol primitives:

- DECLARE (Intent)
- CONSTRAIN (Invariant binding)
- EVIDENCE (Proof and simulation results)
- SIMULATE (Counterfactual evaluation)
- ARBITRATE (Conflict resolution)
- ACCEPT (Selected world-state transition)

ICEP-compliant systems MUST enforce a lifecycle similar to:

DRAFT -> DECLARED -> SIMULATED -> EVALUATED -> ACCEPTED
                                   |
                                REJECTED

ICEP ends at ACCEPTED. Materialization of changes is out of scope and is
typically governed by an authority protocol such as AAP.

---

## Relationship to AAP

ICEP and AAP are complementary:

- AAP governs who is allowed to authorize transitions
- ICEP governs how transitions are evaluated and selected

ICEP assumes intent legitimacy is enforced by an authority protocol.

---

## Governance Model

ICEP is an open protocol.

- This repository hosts the specification
- Tokligence acts as the initial steward
- Protocol changes are proposed via RFCs

---

## Reference Implementation

ICEP intentionally separates specification from implementation.

A reference implementation may be hosted in a separate repository:

- ../ICEP

---

## RFCs

- RFC-0001: Intent and Constraint Evolution Protocol (ICEP)
- RFC-0002: Intent Declaration
- RFC-0003: Constraints and Evidence
- RFC-0004: Arbitration and Conflict Resolution
- RFC-0005: Event Log
- RFC-0006: HTTP+JSON Transport Profile

## Schemas (ICEP-JSON)

Canonical JSON schemas live in `schemas/`:

- `schemas/common.json`
- `schemas/intent.json`
- `schemas/constraint.json`
- `schemas/world_state.json`
- `schemas/evidence.json`
- `schemas/arbitration.json`
- `schemas/event.json`

Examples are in `examples/`.

## Validation

Validate example payloads against the schemas:

```
python scripts/validate_examples.py
```

Requires the `jsonschema` package.

## Status

- Current Status: Draft
- Initial RFC: RFC-0001
- License: Apache 2.0

---

## Contributing

ICEP evolves through clarity, not velocity.

Before contributing:

1. Read `terminology.md`
2. Read `non-goals.md`
3. Understand the constraint model

Contributions that dilute the evolution model will not be accepted.

---

## Closing Note

ICEP does not attempt to make agents communicate better.

It ensures that as agent execution scales, shared systems evolve through
constraints, evidence, and arbitration rather than conversation.
