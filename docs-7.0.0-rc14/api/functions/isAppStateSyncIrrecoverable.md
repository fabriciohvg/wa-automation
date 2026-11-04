# isAppStateSyncIrrecoverable

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/chat-utils.ts:159`

```ts
function isAppStateSyncIrrecoverable(error: any, attempts: number): boolean
```

Determines if an app state sync error is unrecoverable.
TypeError indicates a WASM crash; otherwise we give up after MAX_SYNC_ATTEMPTS.
Missing keys are NOT checked here — they are handled separately as "Blocked".
