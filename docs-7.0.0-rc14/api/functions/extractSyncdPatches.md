# extractSyncdPatches

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/chat-utils.ts:354`

```ts
function extractSyncdPatches(result: BinaryNode, options: RequestInit): Promise<{ critical_block: { hasMorePatches: boolean; patches: ISyncdPatch[]; snapshot: ISyncdSnapshot; }; critical_unblock_low: { hasMorePatches: boolean; patches: ISyncdPatch[]; snapshot: ISyncdSnapshot; }; regular: { hasMorePatches: boolean; patches: ISyncdPatch[]; snapshot: ISyncdSnapshot; }; regular_high: { hasMorePatches: boolean; patches: ISyncdPatch[]; snapshot: ISyncdSnapshot; }; regular_low: { hasMorePatches: boolean; patches: ISyncdPatch[]; snapshot: ISyncdSnapshot; }; }>
```
