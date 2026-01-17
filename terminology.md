# Terminology

This document defines the core terminology used by the Intent and Constraint
Evolution Protocol (ICEP).

The purpose of this terminology is not academic precision, but conceptual
clarity. ICEP introduces terms that replace legacy coordination abstractions
that do not scale to multi-agent systems.

---

## World-State

World-State refers to the externally observable condition of a system.

This includes, but is not limited to:

- Source code
- Configuration files
- Infrastructure definitions
- Data schemas
- Runtime behavior
- Deployment topology
- Authorization boundaries

ICEP treats code as a projection of world-state, not the world-state itself.

---

## World-State Graph

A World-State Graph is an immutable graph of valid world-states connected by
proposed transitions.

- Each node is a complete candidate world-state
- Each edge is an intent that proposes a transition

ICEP reasons about evolution across this graph, not across branches.

---

## World-State Transition

A World-State Transition is any change that moves the system from one valid
world-state to another.

ICEP evaluates transitions through constraints, evidence, and arbitration.

---

## Agent

An Agent is an autonomous or semi-autonomous system capable of proposing
world-state transitions or evaluating evidence.

Agents are execution entities, not authorities.

---

## Intent

An Intent is a declarative statement of a desired world-state transition.

An intent SHOULD include:

- Scope (what parts of the world-state are touched)
- Desired outcome (what should change)
- Expected properties (what must remain true)
- Risk signals (where conflicts are likely)

---

## Change-Set

A Change-Set is an immutable artifact that represents the concrete
modifications needed to produce a candidate world-state from a base state.

Change-Sets are referenced by digest or URI and are used by simulation engines.

---

## Scope

Scope declares the intended impact surface of an intent, such as affected
paths, modules, or interfaces.

Scope is used for early conflict detection and arbitration.
Scope MAY be global when an intent or constraint applies to the entire system.

---

## Intent Declaration

An Intent Declaration is the concrete artifact that records an intent in the
world-state graph or intent log.

Intent Declarations are immutable once recorded.

---

## Intent Log

An Intent Log is an append-only record of declared intents and their evaluation
outcomes.

The intent log provides traceability for arbitration decisions.

---

## Constraint / Invariant

A Constraint (or Invariant) is a rule that MUST hold before and after a
world-state transition.

Examples:

- No plaintext secrets in source control
- Authentication layer must not depend on application layer
- Latency budget must remain under 50 ms

Violating a constraint invalidates a candidate future.

---

## Evidence

Evidence is any artifact that supports the claim that an intent satisfies all
constraints.

Examples:

- Test results
- Static analysis reports
- Security scans
- Formal proofs
- Simulation outcomes

---

## Simulation (Counterfactual)

A Simulation is a counterfactual evaluation of a candidate future world-state.

Simulations produce evidence and can be executed by agents in parallel.

---

## Parallel Future

A Parallel Future is a candidate world-state produced by an intent that has not
been accepted or rejected.

ICEP allows many parallel futures to exist at the same time.

---

## Event Log

An Event Log is an append-only record of ICEP events (intent declarations,
evidence attachments, arbitration decisions, and accepted states).

Event logs provide auditability and deterministic replay.

---

## Arbiter

An Arbiter is the authority-neutral component that selects an accepted
world-state transition based on constraints and evidence.

The arbiter does not interpret intent semantics, only compliance.

---

## Accepted State

An Accepted State is a world-state that has passed constraints, evidence checks,
and arbitration.

Acceptance does not imply authorization to materialize changes.

---

## Conflict

A Conflict is a situation where multiple intents cannot all be satisfied in a
single world-state under the current constraints.

ICEP resolves conflicts through arbitration and constraint priority.

---

# Terminology Stability

Terminology defined in this document is considered normative for ICEP.

Any implementation or discussion of ICEP MUST adhere to these definitions to
remain compatible with the protocol.
