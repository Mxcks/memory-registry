# agent-run-ledger v1

What it is: a logging contract for automated agent runs. Every run appends one legible record to a JSONL ledger: what it was asked, what it did, what it cost, how it ended.

Why it exists: scheduled agents fail silently. Without a ledger, a wrong run is invisible until the damage surfaces. With one, any incident is explainable from the ledger in under an hour.

## Install

1. Copy this folder into your project.
2. Create your ledger file (for example `ledger.jsonl`) wherever your runs can append to it.
3. Give your agent the contract: "Append your run entry per CONTRACT.md before finishing. A run without a ledger entry is an incomplete run."
4. Run `python3 validate_ledger.py ledger.jsonl` on a schedule (or in CI) to catch malformed entries early.

## File layout

- `README.md` (this file)
- `CONTRACT.md` (required fields, the two tiers, rules)
- `validate_ledger.py` (checks every line for required fields; exit 0 = clean)

## The short version

- One JSON object per line (JSONL). Append-only; a correction is a new entry that references the earlier `run_id`.
- Required on every entry: `run_id`, `job_id`, `started_at`, `model`, `inputs_summary`, `tokens_in`, `tokens_out`, `cost_usd`, `outcome` (ok / failed / degraded), `notes`.
- Multi-step runs add a parent entry plus one span entry per step, linked with `parent_run_id`.
- Keep personal data out: summarize inputs, never paste secrets or full private messages.
