# HISTORY_SYNC_PAUSED_TIMEOUT_MS

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Variable · source `src/Defaults/index.ts:138`

```ts
const HISTORY_SYNC_PAUSED_TIMEOUT_MS: 120000 = 120_000
```

120s timeout for history sync stall detection, same as WA Web's handleChunkProgress / restartPausedTimer (g = 120)
