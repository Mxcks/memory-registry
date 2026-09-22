# Agent Run Logging Contract (v1)

Purpose: every agent run leaves one legible record, so a silent-wrong run
becomes a one-trace explanation. No new vendor, no new infrastructure: plain
JSONL on your machine. If a run produces these fields, any incident must be
explainable from the ledger in under an hour.

## Ledger

- Location: your choice (for example `./ledger.jsonl`)
- Format: one JSON object per line (JSONL). Append-only. Never rewrite
  history; a correction is a new entry whose `notes` references the earlier
  `run_id`.

## Required fields (every entry)

- `run_id`: stable unique id for this run (job id + scheduled instant + suffix)
- `job_id`: the job id
- `started_at`: ISO-8601 timestamp
- `model`: model name and version
- `inputs_summary`: what the run was asked to do, one line
- `tokens_in`, `tokens_out`: token counts (0 when not applicable)
- `cost_usd`: estimated cost, best effort (0 when unknown)
- `outcome`: one of `ok`, `failed`, `degraded`
- `notes`: free text: what happened, anomalies, feedback for the next run

## Conditional fields

- `retrieval`: array of `{source, score, excerpt}`. Required when retrieval used.
- `tool_calls`: array of `{tool, args_summary, result_summary, error}`.
  Required when tools used.
- `parent_run_id`: required on span entries (links span to its parent run).

## Two tiers

- **Single-shot jobs** (one LLM call, no tools, no retrieval, no state):
  append ONE entry with the required fields above.
- **Multi-step loops** (tools, retrieval, or autonomy): append a parent entry
  (overall `outcome`, plus `span_count`) and one span entry per step. Each span
  carries its own inputs, tool call or retrieval result, tokens, and outcome,
  and links back with `parent_run_id`. Spans carry the input and output that
  moved through them, not just a duration.

## Rules

1. Every worker appends its entry or entries to the ledger BEFORE finishing.
   A run without a ledger entry is an incomplete run.
2. Keep personal data out: summarize inputs; never paste secrets, credentials,
   tokens, or full private messages.
3. Omit nothing to save space: a missing required field fails validation.
