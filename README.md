# Memory Registry

A public registry of versioned AI memory systems by Macks Studios.

The idea is simple: your AI assistant works better when it remembers. These are the memory systems we actually run in production. Pick one, copy its folder, follow its README. No sign-up, no API, no vendor. Plain files.

## Systems

| System | Version | What it does |
|---|---|---|
| [provenance-memory](systems/provenance-memory/v1) | v1 | Durable memory with provenance: every fact says where it came from, and changed facts keep their history |
| [open-question-queue](systems/open-question-queue/v1) | v1 | Never lose a question your AI asks the user: a queue with a single daily digest nudge |
| [agent-run-ledger](systems/agent-run-ledger/v1) | v1 | Every automated run leaves one legible record, so a silent-wrong run becomes a one-trace explanation |

## Install

1. Pick a system above.
2. Copy its folder (for example `systems/provenance-memory/v1`) into your project.
3. Follow that system's README. Each one is self-contained.

## Versioning

- Each system lives in `systems/<name>/<version>/`. When a system changes in a way that affects behavior, we add a new version folder. Old versions stay put and keep working.
- `registry.json` is the index. It lists every system, its current version, and its path.
- We add versions, we do not rewrite them. If v1 of a system is in your project, it keeps behaving the same way.

## Roadmap

More systems land here as we build them. Check back; the `registry.json` index always shows what is current.

## License

MIT. Use these in your own products, commercial or otherwise. See [LICENSE](LICENSE).

---

Built by Macks Studios.
