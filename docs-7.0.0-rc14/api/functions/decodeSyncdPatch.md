# decodeSyncdPatch

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/chat-utils.ts:320`

```ts
function decodeSyncdPatch(msg: ISyncdPatch, name: "critical_unblock_low" | "regular_high" | "regular_low" | "critical_block" | "regular", initialState: LTHashState, getAppStateSyncKey: FetchAppStateSyncKey, onMutation: (mutation) => void, validateMacs: boolean): Promise<{ hash: Buffer<ArrayBuffer>; indexValueMap: {}; }>
```
