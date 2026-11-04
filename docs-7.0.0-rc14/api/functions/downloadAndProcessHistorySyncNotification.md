# downloadAndProcessHistorySyncNotification

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/history.ts:142`

```ts
function downloadAndProcessHistorySyncNotification(msg: IHistorySyncNotification, options: RequestInit, logger?: ILogger): Promise<{ chats: Chat[]; contacts: Contact[]; lidPnMappings: LIDMapping[]; messages: WAMessage[]; pastParticipants: undefined | null | IPastParticipants[]; progress: undefined | null | number; syncType: undefined | null | HistorySyncType; }>
```
