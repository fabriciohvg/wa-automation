# generateOrGetPreKeys

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/signal.ts:53`

```ts
function generateOrGetPreKeys(creds: AuthenticationCreds, range: number): object
```

## Returns

- `lastPreKeyId: number`
- `newPreKeys: object`
  - Index Signature: `[id: number]: KeyPair`
- `preKeysRange: readonly [number, number]`
