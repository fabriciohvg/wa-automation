# AccountSettings

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Auth.ts:41`

```ts
type AccountSettings = object
```

## Type declaration

- `defaultDisappearingMode?: Pick<IConversation, "ephemeralExpiration" | "ephemeralSettingTimestamp">` — the default mode to start new conversations with
- `unarchiveChats: boolean` — unarchive chats when a new message is received
