# ICEP-MVP

ICEP-MVP is a minimal reference implementation for the Intent and Constraint
Evolution Protocol (ICEP). It provides a validator for ICEP artifacts and a
simple event-log utility for experimentation.

- Canonical spec: https://github.com/tokligence/ICEP
- Companion authority protocol: https://github.com/tokligence/AAP
- Status: MVP / reference tooling

## Features

- Validate ICEP artifacts against ICEP-JSON schemas
- Validate NDJSON event logs
- Append validated events to an event log file

## Quickstart

Create a virtual environment and install in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Validate an artifact:

```bash
icep validate examples/intent.json
```

Validate an event log:

```bash
icep validate examples/event-log.jsonl
```

Append an event to a log:

```bash
icep event-log append --log logs/icep.jsonl --event examples/event.json
```

## Project Structure

```
.
├── icep_mvp/             # CLI + schema bundle
│   ├── schemas/          # ICEP-JSON schemas
│   └── cli.py            # Command-line entrypoint
├── examples/             # Sample artifacts
└── pyproject.toml        # Packaging metadata
```

## License

Apache-2.0
