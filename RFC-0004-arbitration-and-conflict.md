# RFC-0004: Arbitration and Conflict Resolution

**Status:** Draft  
**Category:** Standards Track  
**Version:** 1.0  
**Author:** Tokligence (Initial Steward)

---

## 1. Abstract

This RFC defines the arbitration semantics used by ICEP to resolve conflicts
between parallel futures and to select an accepted world-state transition.

---

## 2. Arbitration (Normative)

An arbiter is responsible for accepting or rejecting candidate futures based on
constraints and evidence.

An arbiter MUST accept a candidate future only if:

- All `must` constraints pass
- Required evidence is present and valid
- A deterministic conflict policy selects the candidate

Arbitration decisions MUST be recorded immutably and be auditable.

### 2.1 JSON Encoding

ICEP-JSON defines the canonical JSON representation for arbitration decisions
in `schemas/arbitration.json`.

Implementations claiming ICEP-JSON compliance MUST validate arbitration
payloads against this schema.

---

## 3. Conflict Detection (Normative)

An implementation MUST detect conflicts between intents using at least one of
these signals:

- Overlapping scope (paths, modules, interfaces)
- Incompatible constraints (mutually exclusive invariants)
- Divergent base states (incompatible ancestry)

If conflicts are detected, the arbiter MUST record them in the arbitration
record with a reason string.

---

## 4. Deterministic Conflict Policy (Normative)

If multiple candidates satisfy constraints, the arbiter MUST apply a
pre-defined deterministic policy.

Examples include:

- Highest priority constraint wins
- Earliest declared intent wins
- Explicit priority tag wins

The chosen policy and parameters MUST be recorded in the arbitration decision
for auditability.

---

## 5. Accepted State (Normative)

An accepted state MUST reference a concrete `state_ref` that can be materialized
or handed off to an authority protocol such as AAP.

Acceptance does not imply authorization to commit changes.

---

## 6. Conformance

An implementation may claim compliance with RFC-0004 if it:

- Enforces deterministic arbitration
- Records arbitration decisions with `schemas/arbitration.json`
- Detects and records conflicts

---

## 7. References

- `schemas/arbitration.json`
