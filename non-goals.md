# Non-Goals of the Intent and Constraint Evolution Protocol (ICEP)

This document outlines what ICEP explicitly does not attempt to solve.

ICEP is intentionally narrow in scope.
Its strength lies in clarity, not completeness.

---

## ICEP Is Not an Agent Communication Protocol

ICEP does not define:

- How agents discover each other
- Message formats between agents
- Network transports or authentication

ICEP operates above communication layers.

---

## ICEP Is Not a Human Authority Protocol

ICEP does not define:

- Who is allowed to authorize changes
- Human override or accountability
- Decision legitimacy or audit policy

Those concerns belong to AAP.

---

## ICEP Is Not a Consensus or Voting System

ICEP does not require:

- Majority votes
- Byzantine consensus
- Agent negotiation or persuasion

ICEP resolves conflicts through constraints and arbitration.

---

## ICEP Is Not a CI/CD Replacement

ICEP does not replace:

- Build pipelines
- Test runners
- Deployment automation

ICEP consumes evidence produced by those systems.

---

## ICEP Is Not a Scheduling or Resource Manager

ICEP does not allocate:

- Compute resources
- Execution priorities
- Agent quotas

Those concerns are implementation-specific.

---

## ICEP Is Not a Code Quality System

ICEP does not:

- Enforce style guides
- Guarantee correctness
- Review code quality

ICEP only evaluates constraints and evidence.

---

## ICEP Is Not a Productivity Tool

ICEP does not aim to:

- Maximize velocity
- Eliminate human oversight
- Replace engineering judgment

ICEP prioritizes evolvability and conflict elimination.

---

## ICEP Is Not a Complete World Model

ICEP does not require:

- A universal data model
- A specific storage format
- A single system of record

ICEP defines semantics for evolution, not storage.

---

# Why These Non-Goals Matter

ICEP exists to answer a single question:

> How can multiple agents evolve the same system without direct coordination?

Anything that does not directly serve this question is intentionally excluded.

---

# Stability of Non-Goals

The non-goals defined in this document are considered foundational.

Future extensions to ICEP MUST NOT violate these constraints.
