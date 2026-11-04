# SyncState

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Enum · source `src/Types/State.ts:4`

## Enumeration Members

- `AwaitingInitialSync: 1` — Pending notifications received. Buffering events until we decide whether to sync or not.
- `Connecting: 0` — The socket is connecting, but we haven't received pending notifications yet.
- `Online: 3` — Initial sync is complete, or was skipped. The socket is fully operational and events are processed in real-time.
- `Syncing: 2` — The initial app state sync (history, etc.) is in progress. Buffering continues.
