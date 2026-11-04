# decodeSyncdSnapshot

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/chat-utils.ts:422`

```ts
function decodeSyncdSnapshot(name: "critical_unblock_low" | "regular_high" | "regular_low" | "critical_block" | "regular", snapshot: ISyncdSnapshot, getAppStateSyncKey: FetchAppStateSyncKey, minimumVersionNumber: undefined | number, validateMacs: boolean = true, logger?: ILogger): Promise<{ mutationMap: ChatMutationMap; state: LTHashState; }>
```
