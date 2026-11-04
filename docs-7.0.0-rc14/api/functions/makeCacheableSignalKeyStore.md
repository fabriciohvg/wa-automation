# makeCacheableSignalKeyStore

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/auth-utils.ts:37`

```ts
function makeCacheableSignalKeyStore(store: SignalKeyStore, logger?: ILogger, _cache?: CacheStore): SignalKeyStore
```

Adds caching capability to a SignalKeyStore

## Parameters

- `store: SignalKeyStore` — the store to add caching to
- `logger?: ILogger` — to log trace events
- `_cache?: CacheStore` — cache store to use
