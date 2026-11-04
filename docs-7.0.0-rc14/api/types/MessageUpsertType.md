# MessageUpsertType

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:382`

```ts
type MessageUpsertType = "append" | "notify"
```

Type of message upsert
1. notify => notify the user, this message was just received
2. append => append the message to the chat history, no notification required
