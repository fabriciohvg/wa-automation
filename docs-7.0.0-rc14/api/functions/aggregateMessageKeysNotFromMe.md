# aggregateMessageKeysNotFromMe

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages.ts:1017`

```ts
function aggregateMessageKeysNotFromMe(keys: WAMessageKey[]): object[]
```

Given a list of message keys, aggregates them by chat & sender. Useful for sending read receipts in bulk
