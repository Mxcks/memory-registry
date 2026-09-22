# open-question-queue v1

What it is: a small queue that makes sure no question your AI asks the user ever gets lost.

The problem: AI assistants ask questions constantly, in chat, in side threads, at odd hours. The user misses half of them. The assistant forgets it asked. Things stall.

How it works:

1. The moment the assistant asks a question that needs the user's answer, it logs it (`q add`).
2. The moment the user answers, it closes it (`q done Q-n`) or skips it (`q skip Q-n`).
3. Once a day, one digest lists everything still open. That digest is the re-ask. No duplicate nudges in chat, and never re-ask a closed question.

## Install

1. Copy this folder into your project.
2. Keep `queue.jsonl` where your agent can read and write it.
3. Put `bin/q` somewhere your agent can run it (it needs Node).
4. Tell your agent: "When you ask the user something that needs their answer, log it with `q add` immediately. When they answer, close it with `q done`."
5. Schedule one daily digest run. Adapt the pattern in `DIGEST.md` to your channel: email, Slack, push notification, whatever you use.

## File layout

- `README.md` (this file)
- `QUEUE.md` (schema, lifecycle, rules)
- `DIGEST.md` (the single-digest nudge pattern)
- `bin/q` (the CLI: add, list, done, skip, due)
- `queue.jsonl` (the queue itself; seeded with two examples, delete them)

## CLI quick reference

```
q add --question "..." --context "..." [--chat main]   # log a question
q list              # show open questions
q list --all        # show everything including closed
q done Q-3          # mark answered
q skip Q-4          # mark skipped
q due               # JSON of questions due for the next digest
```
