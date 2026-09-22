# The single-digest nudge

One digest per day, not one nudge per question.

1. Collect the due questions: still open, asked more than 6 hours ago, last
   nudged more than 20 hours ago (or never nudged). `q due` returns them as JSON.
2. Send ONE message listing all of them, in plain language.
3. Mark each included question: `last_nudged_at` = now, `nudge_count` + 1.
4. Stop when the user answers or skips. The digest does the re-asking, so the
   assistant never repeats itself in conversation.

The queue does not care how the message goes out. Adapt the send step to your
channel: email, Slack, Telegram, push notification. Keep it to one digest a day;
the point is a single predictable moment, not a stream of pings.
