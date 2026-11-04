# PossiblyExtendedCacheStore

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Socket.ts:25`

```ts
type PossiblyExtendedCacheStore = CacheStore & object
```

## Type declaration

- `mdel?: (keys: string[]) => void | Promise<void> | number | boolean`
- `mget?: <T>(keys: string[]) => Promise<Record<string, T | undefined>>`
  - Type params: `T`
- `mset?: <T>(entries: object[]) => Promise<void> | void | number | boolean`
  - Type params: `T`
