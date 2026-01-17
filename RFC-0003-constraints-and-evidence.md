# RFC-0003: Constraints and Evidence

**Status:** Draft  
**Category:** Standards Track  
**Version:** 1.0  
**Author:** Tokligence (Initial Steward)

---

## 1. Abstract

This RFC defines the ICEP constraint model, evidence requirements, and
simulation outputs used to validate candidate world-states.

---

## 2. Constraint Model (Normative)

A constraint is an invariant that MUST hold before and after a world-state
transition.

Constraints MUST include:

- A unique `constraint_id`
- A declared `scope`
- A `severity` (must, should, may)
- A formal `logic` description

Constraints SHOULD include evidence requirements to make validation objective
and machine-verifiable.

### 2.1 JSON Encoding

ICEP-JSON defines the canonical JSON representation for constraints in
`schemas/constraint.json`.

Implementations claiming ICEP-JSON compliance MUST validate constraints
against this schema.

---

## 3. Evidence (Normative)

Evidence is any artifact that supports the claim that an intent satisfies
constraints.

Evidence MUST:

- Bind to a specific `intent_id`
- Reference both `base_state` and `candidate_state`
- Provide per-constraint evaluations
- Include immutable artifact references or digests

Evidence MAY include simulation metadata, test outputs, or formal proofs.

### 3.1 JSON Encoding

ICEP-JSON defines the canonical JSON representation for evidence in
`schemas/evidence.json`.

Implementations claiming ICEP-JSON compliance MUST validate evidence against
this schema.

---

## 4. Simulation (Normative)

Simulations are counterfactual evaluations run against a candidate world-state.

If any constraint lists a required evidence type, a simulation or check MUST
produce corresponding evidence before arbitration.

Simulation metadata SHOULD include environment, timing, and artifact references
for auditability.

---

## 5. Evidence Binding and Replay Prevention

Evidence MUST be bound to the candidate world-state it evaluates.

Implementations SHOULD:

- Use digests for artifacts
- Store evidence in append-only logs
- Reject evidence that targets a different `state_ref`

---

## 6. Conformance

An implementation may claim compliance with RFC-0003 if it:

- Validates constraints with `schemas/constraint.json`
- Validates evidence with `schemas/evidence.json`
- Enforces binding between evidence, intents, and candidate states

---

## 7. References

- `schemas/constraint.json`
- `schemas/evidence.json`
