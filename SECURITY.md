# Security

This repository contains an Agent definition and local validation tooling. It
does not require API keys and must not contain credentials, private
conversations, brokerage data, or production data.

Report suspected security issues privately through this repository's GitHub
security advisory feature.

When integrating the Agent into a host:

- keep model, search, finance-data, and tool credentials outside the repository;
- require explicit authority for transactions, external writes, and irreversible actions;
- obtain dated primary sources for specific securities and current financial decisions;
- never send private financial records into public fixtures;
- preserve the downside, no-guarantee, and specialist-review boundaries in `agent/RUNTIME.md`.
