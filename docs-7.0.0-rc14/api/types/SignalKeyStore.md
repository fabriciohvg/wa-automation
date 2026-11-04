# SignalKeyStore

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Auth.ts:91`

```ts
type SignalKeyStore = object
```

## Type declaration

- `clear()?() => Awaitable<void>` — clear all the data in the store
- `get(type: T, ids: string[]) => Awaitable<{}>`
  - Type params: `T extends keyof SignalDataTypeMap`
- `set(data: SignalDataSet) => Awaitable<void>`
