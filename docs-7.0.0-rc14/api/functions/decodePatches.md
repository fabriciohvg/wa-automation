# decodePatches

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/chat-utils.ts:479`

```ts
function decodePatches(name: "critical_unblock_low" | "regular_high" | "regular_low" | "critical_block" | "regular", syncds: ISyncdPatch[], initial: LTHashState, getAppStateSyncKey: FetchAppStateSyncKey, options: RequestInit, minimumVersionNumber?: number, logger?: ILogger, validateMacs?: boolean = true): Promise<{ mutationMap: ChatMutationMap; state: LTHashState; }>
```
