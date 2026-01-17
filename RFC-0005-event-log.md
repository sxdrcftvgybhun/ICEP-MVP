# RFC-0005: Event Log

**Status:** Draft  
**Category:** Standards Track  
**Version:** 1.0  
**Author:** Tokligence (Initial Steward)

---

## 1. Abstract

This RFC defines the ICEP Event Log, an append-only record of protocol
artifacts that enables replication, audit, and deterministic arbitration.

---

## 2. Event Log Model (Normative)

An ICEP Event Log is a sequence of immutable event records.

Each event MUST:

- Have a unique `event_id`
- Declare an `event_type`
- Provide a timestamp
- Include either an embedded `payload` or a `payload_ref`

Events SHOULD chain using `prev_event_digest` to enable tamper detection.

### 2.1 JSON Encoding

ICEP-JSON defines the canonical JSON representation for events in
`schemas/event.json`.

Implementations claiming ICEP-JSON compliance MUST validate event payloads
against this schema.

---

## 3. Event Types (Normative)

ICEP defines these event types:

- INTENT_DECLARED
- CONSTRAINT_BOUND
- EVIDENCE_ATTACHED
- SIMULATION_REPORTED
- STATE_PRODUCED
- ARBITRATION_DECIDED
- STATE_ACCEPTED
- STATE_REJECTED

Implementations MAY define additional event types, but MUST NOT change the
semantics of the canonical types.

---

## 4. Log Format (Normative)

The canonical log format is newline-delimited JSON (NDJSON). Each line MUST be
a valid `event.json` object.

---

## 5. Conformance

An implementation may claim compliance with RFC-0005 if it:

- Records events as append-only entries
- Uses `schemas/event.json`
- Preserves event ordering and immutability

---

## 6. References

- `schemas/event.json`
- `examples/event-log.jsonl`
