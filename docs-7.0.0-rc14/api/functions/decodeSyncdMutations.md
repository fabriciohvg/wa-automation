# decodeSyncdMutations

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/chat-utils.ts:228`

```ts
function decodeSyncdMutations(msgMutations: (ISyncdMutation | ISyncdRecord)[], initialState: LTHashState, getAppStateSyncKey: FetchAppStateSyncKey, onMutation: (mutation) => void, validateMacs: boolean): Promise<{ hash: Buffer<ArrayBuffer>; indexValueMap: {}; }>
```
