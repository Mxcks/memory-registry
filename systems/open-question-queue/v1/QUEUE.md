# queue.jsonl schema

One JSON object per line. Append-only: new questions are added as new lines,
closed questions are updated in place by id.

| Field | Meaning |
|---|---|
| `id` | Q-1, Q-2, ... assigned in order |
| `asked_at` | ISO-8601 timestamp of when the question was asked |
| `chat` | where it was asked: main, side, email, anything you use |
| `question` | the question, verbatim |
| `context` | why it matters, one line |
| `status` | `open`, `answered`, or `skipped` |
| `last_nudged_at` | timestamp of the last digest that included it, or null |
| `nudge_count` | how many digests have included it |
| `resolved_at` | timestamp of when it was closed, or null |

## Lifecycle

`add` creates an open question. `done` marks it answered. `skip` marks it
skipped. Both closing commands set `resolved_at`.

## Rules

- Log the question the moment you ask it. Close it the moment the user answers.
- The digest is the re-ask: never duplicate a nudge in chat.
- Never re-ask a closed question.
- A question is due for the digest when it is still open, was asked more than
  6 hours ago, and was last nudged more than 20 hours ago (or never nudged).
  Tune those thresholds to your user.
