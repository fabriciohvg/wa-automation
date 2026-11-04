# getNextPreKeys

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/signal.ts:225`

```ts
function getNextPreKeys(__namedParameters: AuthenticationState, count: number): Promise<{ preKeys: {}; update: Partial<AuthenticationCreds>; }>
```

get the next N keys for upload or processing

## Parameters

- `__namedParameters: AuthenticationState`
- `count: number` — number of pre-keys to get or generate
