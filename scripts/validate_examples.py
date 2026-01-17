#!/usr/bin/env python3
"""Validate ICEP example payloads against ICEP-JSON schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
    from jsonschema.exceptions import ValidationError
    from referencing import Registry
    from referencing.jsonschema import DRAFT202012
except ImportError:  # pragma: no cover - dependency hint
    print("Missing dependency: jsonschema")
    print("Install with: pip install jsonschema")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLES_DIR = ROOT / "examples"

EXAMPLE_SCHEMA_MAP = {
    "intent.json": "intent.json",
    "constraint.json": "constraint.json",
    "world_state.json": "world_state.json",
    "evidence.json": "evidence.json",
    "arbitration.json": "arbitration.json",
}

JSONL_SCHEMA_MAP = {
    "event-log.jsonl": "event.json",
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


def validate_instance(instance: object, schema_path: Path, registry: Registry) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator(schema, registry=registry).validate(instance)


def validate_json_file(example_path: Path, schema_name: str, registry: Registry) -> None:
    instance = json.loads(example_path.read_text(encoding="utf-8"))
    schema_path = SCHEMA_DIR / schema_name
    validate_instance(instance, schema_path, registry)


def validate_jsonl_file(example_path: Path, schema_name: str, registry: Registry) -> None:
    schema_path = SCHEMA_DIR / schema_name
    with example_path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            instance = json.loads(line)
            validate_instance(instance, schema_path, registry)


def main() -> int:
    registry = load_registry()
    failures = 0

    for example_name, schema_name in EXAMPLE_SCHEMA_MAP.items():
        example_path = EXAMPLES_DIR / example_name
        try:
            validate_json_file(example_path, schema_name, registry)
            print(f"OK  {example_name}")
        except FileNotFoundError:
            print(f"SKIP {example_name} (missing)")
        except ValidationError as exc:
            failures += 1
            print(f"FAIL {example_name}: {exc.message}")

    for example_name, schema_name in JSONL_SCHEMA_MAP.items():
        example_path = EXAMPLES_DIR / example_name
        try:
            validate_jsonl_file(example_path, schema_name, registry)
            print(f"OK  {example_name}")
        except FileNotFoundError:
            print(f"SKIP {example_name} (missing)")
        except ValidationError as exc:
            failures += 1
            print(f"FAIL {example_name}: {exc.message}")

    if failures:
        print(f"Validation failures: {failures}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
