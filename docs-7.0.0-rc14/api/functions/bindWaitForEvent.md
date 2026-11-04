# bindWaitForEvent

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/generics.ts:205`

```ts
function bindWaitForEvent<T>(ev: BaileysEventEmitter, event: T): (check, timeoutMs?) => Promise<void>
```

Type params: `T extends keyof BaileysEventMap`

## Returns

- `Parameters`
  - `check` — (`u`) => `Promise`<`undefined` | `boolean`>
  - `timeoutMs?` — `number`
- `Returns` — `Promise`<`void`>
