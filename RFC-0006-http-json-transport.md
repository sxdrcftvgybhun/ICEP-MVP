# RFC-0006: HTTP+JSON Transport Profile

**Status:** Draft  
**Category:** Standards Track  
**Version:** 1.0  
**Author:** Tokligence (Initial Steward)

---

## 1. Abstract

This RFC defines an optional HTTP+JSON transport profile for ICEP. It specifies
canonical REST-style endpoints, request/response conventions, and content
requirements for exchanging ICEP artifacts.

This profile is intended for interoperability across implementations. It does
not replace other transports such as gRPC, message queues, or append-only logs.

---

## 2. Scope

This profile covers:

- HTTP endpoints for core ICEP artifacts
- JSON encoding requirements (ICEP-JSON)
- Event log append and read operations
- Error and idempotency conventions

Authentication and authorization are out of scope.

---

## 3. Content Types

Clients MUST send ICEP artifacts as JSON documents conforming to the relevant
schemas in `schemas/`.

- Requests and responses MUST use `Content-Type: application/json`.
- Servers MUST validate payloads using ICEP-JSON schemas.
- Each payload MUST include a `kind` field.

Implementations MAY also support `application/icep+json`, but this is optional.

---

## 4. Resource Endpoints (Normative)

All endpoints are rooted at `/v1`.

### 4.1 Intents

- `POST /v1/intents`
  - Body: `schemas/intent.json`
  - Response: `201 Created` with the stored intent

- `GET /v1/intents/{intent_id}`
  - Response: `200 OK` with the intent

### 4.2 Constraints

- `POST /v1/constraints`
  - Body: `schemas/constraint.json`
  - Response: `201 Created` with the stored constraint

- `GET /v1/constraints/{constraint_id}`
  - Response: `200 OK` with the constraint

### 4.3 Candidate World-States

- `POST /v1/world-states`
  - Body: `schemas/world_state.json`
  - Response: `201 Created` with the stored world-state

- `GET /v1/world-states/{state_id}`
  - Response: `200 OK` with the world-state

### 4.4 Evidence

- `POST /v1/evidence`
  - Body: `schemas/evidence.json`
  - Response: `201 Created` with the stored evidence

- `GET /v1/evidence/{evidence_id}`
  - Response: `200 OK` with the evidence

### 4.5 Arbitration

- `POST /v1/arbitrations`
  - Body: `schemas/arbitration.json`
  - Response: `201 Created` with the stored decision

- `GET /v1/arbitrations/{decision_id}`
  - Response: `200 OK` with the arbitration decision

---

## 5. Event Log Endpoints (Normative)

ICEP event logs provide append-only audit trails.

### 5.1 Append Events

- `POST /v1/event-streams/{stream_id}/events`
  - Content-Type: `application/x-ndjson`
  - Body: NDJSON, each line validated by `schemas/event.json`
  - Response: `202 Accepted` if appended

Servers MAY also accept a single JSON event payload with
`Content-Type: application/json`.

### 5.2 Read Events

- `GET /v1/event-streams/{stream_id}/events?after={event_id}`
  - Accept: `application/x-ndjson`
  - Response: `200 OK` with NDJSON events in order

---

## 6. Idempotency (Normative)

Clients SHOULD supply `Idempotency-Key` for all POST requests.

If a request is retried with the same key and identical payload, the server
MUST return the original response. If the payload differs, the server MUST
return `409 Conflict`.

---

## 7. Error Format (Normative)

Errors MUST return JSON with the following structure:

```json
{
  "error": {
    "code": "invalid_payload",
    "message": "Intent validation failed",
    "details": ["intent_id is required"]
  }
}
```

Suggested HTTP status codes:

- `400 Bad Request`: malformed JSON
- `401 Unauthorized`: authentication failure
- `403 Forbidden`: authorization failure
- `404 Not Found`: missing resource
- `409 Conflict`: idempotency or state conflict
- `422 Unprocessable Entity`: schema validation failure

---

## 8. Examples

### 8.1 Create Intent

```
POST /v1/intents
Content-Type: application/json
Idempotency-Key: I-2025-0001

{ ... intent payload ... }
```

### 8.2 Append Event Log

```
POST /v1/event-streams/ICEP-LOG-1/events
Content-Type: application/x-ndjson

{...event...}
{...event...}
```

---

## 9. Security Considerations

This profile does not define authentication or authorization. Implementations
SHOULD use secure transports (TLS) and external identity systems.

Authorities and commit authorization are handled by protocols such as AAP.

---

## 10. Conformance

An implementation may claim compliance with RFC-0006 if it:

- Implements the required endpoints
- Validates payloads against ICEP-JSON schemas
- Supports NDJSON event log append/read
- Enforces idempotency semantics

---

## 11. References

- `schemas/intent.json`
- `schemas/constraint.json`
- `schemas/world_state.json`
- `schemas/evidence.json`
- `schemas/arbitration.json`
- `schemas/event.json`
