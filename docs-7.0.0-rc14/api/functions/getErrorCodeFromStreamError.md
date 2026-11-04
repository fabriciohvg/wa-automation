# getErrorCodeFromStreamError

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/generics.ts:364`

```ts
function getErrorCodeFromStreamError(node: BinaryNode): object
```

Stream errors generally provide a reason, map that to a baileys DisconnectReason

## Returns

- `reason: string`
- `statusCode: number`
