# AnyMessageContent

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:289`

```ts
type AnyMessageContent = AnyRegularMessageContent | { force: boolean; forward: WAMessage; } | { delete: WAMessageKey; } | { disappearingMessagesInChat: boolean | number; } | { limitSharing: boolean; }
```

## Type declaration

- union member: `AnyRegularMessageContent`
- union member: `{ force: boolean; forward: WAMessage; }`
- `force?: boolean`
- `forward: WAMessage`
- union member: `{ delete: WAMessageKey; }`
- `delete: WAMessageKey` — Delete your message or anyone's message in a group (admin required)
- union member: `{ disappearingMessagesInChat: boolean | number; }`
- `disappearingMessagesInChat: boolean | number`
- union member: `{ limitSharing: boolean; }`
- `limitSharing: boolean`
