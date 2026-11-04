# BufferedEventData

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Events.ts:146`

```ts
type BufferedEventData = object
```

## Type declaration

- `chatDeletes: Set<string>`
- `chatUpdates: object`
  - Index Signature: `[jid: string]: Partial<IConversation & object & object>`
- `chatUpserts: object`
  - Index Signature: `[jid: string]: Chat`
- `contactUpdates: object`
  - Index Signature: `[jid: string]: Partial<Contact>`
- `contactUpserts: object`
  - Index Signature: `[jid: string]: Contact`
- `groupUpdates: object`
  - Index Signature: `[jid: string]: Partial<GroupMetadata>`
- `historySets: object`
  - `historySets.chats: object`
    - Index Signature: `[jid: string]: Chat`
  - `historySets.chunkOrder?: number | null`
  - `historySets.contacts: object`
    - Index Signature: `[jid: string]: Contact`
  - `historySets.empty: boolean`
  - `historySets.isLatest: boolean`
  - `historySets.messages: object`
    - Index Signature: `[uqId: string]: WAMessage`
  - `historySets.pastParticipants?: IPastParticipants[]`
  - `historySets.peerDataRequestSessionId?: string`
  - `historySets.progress?: number | null`
  - `historySets.syncType?: HistorySyncType`
- `messageDeletes: object`
  - Index Signature: `[key: string]: WAMessageKey`
- `messageReactions: object`
  - Index Signature: `[key: string]: object`
- `messageReceipts: object`
  - Index Signature: `[key: string]: object`
- `messageUpdates: object`
  - Index Signature: `[key: string]: WAMessageUpdate`
- `messageUpserts: object`
  - Index Signature: `[key: string]: object`
