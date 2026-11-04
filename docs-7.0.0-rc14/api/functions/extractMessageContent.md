# extractMessageContent

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages.ts:824`

```ts
function extractMessageContent(content: undefined | null | IMessage): undefined | IMessage
```

Extract the true message content from a message
Eg. extracts the inner message from a disappearing message/view once message
