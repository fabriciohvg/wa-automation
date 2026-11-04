# SignalKeyStoreWithTransaction

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Auth.ts:98`

```ts
type SignalKeyStoreWithTransaction = SignalKeyStore & object
```

## Type declaration

- `isInTransaction: () => boolean`
- `transaction(exec: () => Promise<T>, key: string) => Promise<T>`
  - Type params: `T`
