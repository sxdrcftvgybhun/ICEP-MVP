# RFC-0002: Intent Declaration

**Status:** Draft  
**Category:** Standards Track  
**Version:** 1.0  
**Author:** Tokligence (Initial Steward)

---

## 1. Abstract

This RFC defines the canonical Intent Declaration for ICEP and its JSON
encoding (ICEP-JSON). It specifies the required fields, validation rules, and
lifecycle expectations for intents and candidate world-states.

---

## 2. Scope

This RFC covers:

- Intent Declaration semantics
- Base world-state references
- Change-set references
- Scope declaration
- Candidate world-state production

Constraints, evidence, and arbitration are defined in other RFCs.

---

## 3. Intent Declaration (Normative)

An Intent Declaration is a declarative request to evolve a shared world-state.

An ICEP implementation MUST ensure that each intent:

- Has a globally unique `intent_id`
- Identifies the proposing `agent`
- References a concrete `base_state`
- Declares an explicit `scope`
- Is immutable once recorded

An intent MAY omit `change_set` at declaration time, but a `change_set` MUST be
attached before simulation or evidence collection begins.

### 3.1 JSON Encoding

ICEP-JSON defines the canonical JSON representation for intents in
`schemas/intent.json`.

Implementations claiming ICEP-JSON compliance MUST validate intent payloads
against this schema.

---

## 4. Base World-State (Normative)

`base_state` identifies the world-state that the intent proposes to evolve.
It MUST be a stable reference that can be retrieved for simulation.

Examples include:

- A git commit hash
- A snapshot artifact digest
- A URI to a state bundle

`base_state` is encoded using `world_state_ref` from `schemas/common.json`.

---

## 5. Change-Set Reference (Normative)

`change_set` is a reference to the concrete set of modifications that produce
a candidate future when applied to `base_state`.

The `change_set`:

- MUST be immutable
- MUST be content-addressable or digest-verified
- SHOULD be retrievable by simulation engines

`change_set` is encoded using `artifact_ref` from `schemas/common.json`.

---

## 6. Scope Declaration (Normative)

`scope` declares the intended impact surface of the intent.

It MUST include at least one of:

- `global`
- `paths`
- `modules`
- `interfaces`

Scope is used for early conflict detection and arbitration.

---

## 7. Candidate World-State (Normative)

When a `change_set` is applied to a `base_state`, the result is a candidate
world-state, represented by `schemas/world_state.json`.

A candidate world-state MUST:

- Reference the originating `intent_id`
- Record the resulting `state_ref`
- Be immutable once recorded

---

## 8. Examples

See:

- `examples/intent.json`
- `examples/world_state.json`

---

## 9. Security Considerations

Intent declarations are untrusted by default. Implementations MUST NOT accept
an intent as safe or valid without constraints, evidence, and arbitration.

---

## 10. Conformance

An implementation may claim compliance with RFC-0002 if it:

- Validates intents with `schemas/intent.json`
- Requires `base_state` and `scope`
- Enforces immutability and uniqueness of intent declarations

---

## 11. References

- `schemas/intent.json`
- `schemas/world_state.json`
