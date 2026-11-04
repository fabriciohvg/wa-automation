# CacheStore

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Socket.ts:13`

```ts
type CacheStore = object
```

## Type declaration

- `close?: () => void`
- `del(key: string) => number | boolean | void | Promise<void>` — delete a key from the cache
- `flushAll() => void | Promise<void>` — flush all data
- `get(key: string) => undefined | T | Promise<T>` — get a cached key and change the stats
  - Type params: `T`
- `set(key: string, value: T) => number | boolean | void | Promise<void>` — set a key in the cache
  - Type params: `T`
