"""ICEP-MVP CLI."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import ValidationError
    from referencing import Registry
    from referencing.jsonschema import DRAFT202012
except ImportError as exc:  # pragma: no cover - dependency hint
    raise SystemExit("Missing dependency: jsonschema") from exc

SCHEMA_DIR = Path(__file__).resolve().parent / "schemas"

KIND_TO_SCHEMA = {
    "intent": "intent.json",
    "constraint": "constraint.json",
    "evidence": "evidence.json",
    "world_state": "world_state.json",
    "arbitration": "arbitration.json",
    "event": "event.json",
}


def load_registry() -> Registry:
    registry = Registry()
    for schema_path in SCHEMA_DIR.glob("*.json"):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        resource = DRAFT202012.create_resource(schema)
        schema_id = schema.get("$id", schema_path.name)
        registry = registry.with_resource(schema_id, resource)
        registry = registry.with_resource(schema_path.name, resource)
        registry = registry.with_resource(str(schema_path.resolve().as_uri()), resource)
    return registry


def validate_instance(instance: object, schema_name: str, registry: Registry) -> None:
    schema_path = SCHEMA_DIR / schema_name
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator(schema, registry=registry).validate(instance)


def detect_schema_name(instance: dict) -> str:
    kind = instance.get("kind")
    if not kind:
        raise ValueError("Missing required field: kind")
    schema = KIND_TO_SCHEMA.get(kind)
    if not schema:
        raise ValueError(f"Unknown kind: {kind}")
    return schema


def validate_json(path: Path, registry: Registry, schema_override: str | None) -> None:
    instance = json.loads(path.read_text(encoding="utf-8"))
    schema_name = schema_override or detect_schema_name(instance)
    validate_instance(instance, schema_name, registry)


def validate_jsonl(path: Path, registry: Registry, schema_override: str | None) -> None:
    schema_name = schema_override or "event.json"
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            instance = json.loads(line)
            try:
                validate_instance(instance, schema_name, registry)
            except ValidationError as exc:
                raise ValidationError(f"Line {line_no}: {exc.message}") from exc


def cmd_validate(args: argparse.Namespace) -> int:
    registry = load_registry()
    path = Path(args.path)
    schema_override = args.schema
    if path.suffix == ".jsonl":
        validate_jsonl(path, registry, schema_override)
    else:
        validate_json(path, registry, schema_override)
    return 0


def cmd_event_log_append(args: argparse.Namespace) -> int:
    registry = load_registry()
    event_path = Path(args.event)
    log_path = Path(args.log)
    instance = json.loads(event_path.read_text(encoding="utf-8"))
    validate_instance(instance, "event.json", registry)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(instance, separators=(",", ":")) + "\n")
    return 0


def cmd_event_log_validate(args: argparse.Namespace) -> int:
    registry = load_registry()
    path = Path(args.log)
    validate_jsonl(path, registry, "event.json")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="icep", description="ICEP-MVP CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate an ICEP artifact or NDJSON event log",
    )
    validate_parser.add_argument("path", help="Path to JSON or JSONL payload")
    validate_parser.add_argument(
        "--schema",
        help="Override schema name (e.g. intent.json)",
    )
    validate_parser.set_defaults(func=cmd_validate)

    event_log_parser = subparsers.add_parser(
        "event-log",
        help="Operate on ICEP event logs",
    )
    event_log_sub = event_log_parser.add_subparsers(dest="event_cmd", required=True)

    append_parser = event_log_sub.add_parser("append", help="Append an event")
    append_parser.add_argument("--log", required=True, help="Path to log file")
    append_parser.add_argument("--event", required=True, help="Path to event JSON")
    append_parser.set_defaults(func=cmd_event_log_append)

    validate_log_parser = event_log_sub.add_parser(
        "validate", help="Validate an event log"
    )
    validate_log_parser.add_argument("--log", required=True, help="Path to log file")
    validate_log_parser.set_defaults(func=cmd_event_log_validate)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except ValidationError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    except (ValueError, FileNotFoundError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
