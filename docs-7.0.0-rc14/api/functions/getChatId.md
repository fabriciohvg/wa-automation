# getChatId

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/process-message.ts:191`

```ts
function getChatId(__namedParameters: WAMessageKey): string
```

Get the ID of the chat from the given key.
Typically -- that'll be the remoteJid, but for broadcasts, it'll be the participant
