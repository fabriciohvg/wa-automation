# processHistoryMessage

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/history.ts:47`

```ts
function processHistoryMessage(item: IHistorySync, logger?: ILogger): object
```

## Returns

- `chats: Chat[]`
- `contacts: Contact[]`
- `lidPnMappings: LIDMapping[]`
- `messages: WAMessage[]`
- `pastParticipants: undefined | null | IPastParticipants[] = item.pastParticipants`
- `progress: undefined | null | number = item.progress`
- `syncType: undefined | null | HistorySyncType = item.syncType`
