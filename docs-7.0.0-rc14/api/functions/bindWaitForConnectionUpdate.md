# bindWaitForConnectionUpdate

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/generics.ts:233`

```ts
function bindWaitForConnectionUpdate(ev: BaileysEventEmitter): (check, timeoutMs?) => Promise<void>
```

## Returns

- `Parameters`
  - `check` — (`u`) => `Promise`<`undefined` | `boolean`>
  - `timeoutMs?` — `number`
- `Returns` — `Promise`<`void`>
