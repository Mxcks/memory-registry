# Memory conventions (provenance-memory v1)

These conventions turn an AI's markdown memory files into an auditable record.
Teach them to your agent by adding them to its standing instructions.

## 1. Supersede, never silently overwrite

When a fact changes, keep the old line and mark it:

```
[superseded 2026-09-21: user moved to a new city] observed: user lives in Austin, TX
observed: user lives in Denver, CO
```

Invalidation with lineage beats deletion. You can always see what was believed
before and why it changed. The audit trail is the feature.

## 2. Provenance prefixes

Start every memory fact with where it came from:

- `observed:` the user stated it directly
- `inferred:` the agent's own conclusion from evidence. Agent-written memory
  starts as evidence, not instruction.
- `confirmed:` the user verified it
- `disputed:` it is contested or contradicted

Examples:

```
observed: user prefers evening check-ins
inferred: evening check-ins get faster replies (verify against reply timestamps)
confirmed: user wants plain-language summaries, no jargon
```

Only the user's confirmation promotes an inference to `confirmed`.

## 3. Recurrence over importance

When a fact is confirmed again, add a recurrence marker: `(×n)`.

```
observed: user prefers evening check-ins (×3)
```

A fact confirmed three or more times (×3+) is deletion-resistant: it survives
cleanups that drop low-signal entries. Do not score importance with a model on
every write. Recurrence is the importance signal.

## 4. TTL on time-bound facts

Time-bound facts get an expiry:

```
observed: trial of the analytics tool ends Friday (expires 2026-10-03)
```

An upkeep pass (manual or scheduled) sweeps expired facts: supersede them, do
not hard-delete, unless a right-to-be-forgotten request applies.

## 5. Live turns append only

During conversation, only append new facts or dated notes. All restructuring,
dedup, and consolidation happens in a separate offline pass. Mixing the two
degrades both: live turns stay fast and honest, cleanup stays deliberate.

## 6. Daily notes are append-only

Keep dated notes (for example `memory/2026-09-21.md`). Corrections go on new
lines. Never edit yesterday's log to change what happened.
