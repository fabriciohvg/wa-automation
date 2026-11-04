# normalizeMessageContent

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages.ts:788`

```ts
function normalizeMessageContent(content: undefined | null | IMessage): undefined | IMessage
```

Normalizes ephemeral, view once messages to regular message content
Eg. image messages in ephemeral messages, in view once messages etc.
