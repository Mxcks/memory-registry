# provenance-memory v1

What it is: a small set of conventions that make an AI's long-term memory auditable. Every fact carries its provenance. Changed facts keep their history. Nothing is silently overwritten.

Why it exists: plain text memory rots. Facts change, nobody records what changed or why, and six months later nobody trusts the file. These conventions make memory a record you can audit, roll back, and trust.

## Install

1. Copy `MEMORY_CONVENTIONS.md` into your project.
2. Point your agent at it: add to your agent's standing instructions something like "When you write memory, follow MEMORY_CONVENTIONS.md."
3. Use whatever markdown files you already use as the memory store. One curated file plus dated daily notes works well; the conventions do not care about your file layout.

## File layout

- `README.md` (this file)
- `MEMORY_CONVENTIONS.md` (the conventions; this is the part your agent reads)

## The short version

- **Supersede, never silently overwrite.** Old facts stay, marked `[superseded YYYY-MM-DD: reason]`.
- **Provenance prefixes.** `observed:` the user said it. `inferred:` the agent concluded it. `confirmed:` the user verified it. `disputed:` it is contested.
- **Recurrence over importance.** Re-confirmed facts get `(×n)`. Three or more confirmations (×3+) means deletion-resistant.
- **TTL on time-bound facts.** `(expires YYYY-MM-DD)`, swept by an upkeep pass.
- **Live turns append only.** Restructuring happens in a separate offline pass, never mid-conversation.
- **Daily notes are append-only.** Corrections go on new lines.

Full detail, with examples, is in MEMORY_CONVENTIONS.md.
