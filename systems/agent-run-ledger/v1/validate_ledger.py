#!/usr/bin/env python3
"""Validate a ledger.jsonl file against CONTRACT.md (agent-run-ledger v1).

Usage: python3 validate_ledger.py [ledger.jsonl]
Exits 0 if every non-blank line parses as JSON and carries all required fields.
Exits 1 naming the first offending line otherwise.
"""
import json
import sys

REQUIRED = [
    "run_id", "job_id", "started_at", "model", "inputs_summary",
    "tokens_in", "tokens_out", "cost_usd", "outcome", "notes",
]
VALID_OUTCOMES = {"ok", "failed", "degraded"}


def main():
    if len(sys.argv) < 2:
        print("usage: python3 validate_ledger.py <ledger.jsonl>")
        return 1
    path = sys.argv[1]
    try:
        f = open(path, encoding="utf-8")
    except OSError as e:
        print(f"FAIL: cannot open ledger: {e}")
        return 1
    checked = 0
    with f:
        for lineno, raw in enumerate(f, 1):
            line = raw.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"FAIL: line {lineno} is not valid JSON: {e}")
                return 1
            if not isinstance(entry, dict):
                print(f"FAIL: line {lineno} is not a JSON object")
                return 1
            missing = [k for k in REQUIRED if k not in entry]
            if missing:
                print(
                    f"FAIL: line {lineno} (run_id={entry.get('run_id')!r}) "
                    f"missing fields: {', '.join(missing)}"
                )
                return 1
            if entry["outcome"] not in VALID_OUTCOMES:
                print(f"FAIL: line {lineno} bad outcome: {entry['outcome']!r}")
                return 1
            checked += 1
    print(f"OK: {checked} entr{'y' if checked == 1 else 'ies'} valid in {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
