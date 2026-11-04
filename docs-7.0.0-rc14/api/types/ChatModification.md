# ChatModification

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Chat.ts:88`

```ts
type ChatModification = { archive: boolean; lastMessages: LastMessageList; } | { pushNameSetting: string; } | { pin: boolean; } | { mute: number | null; } | { clear: boolean; lastMessages: LastMessageList; } | { deleteForMe: { deleteMedia: boolean; key: WAMessageKey; timestamp: number; }; } | { star: { messages: object[]; star: boolean; }; } | { lastMessages: LastMessageList; markRead: boolean; } | { delete: true; lastMessages: LastMessageList; } | { contact: IContactAction | null; } | { disableLinkPreviews: IPrivacySettingDisableLinkPreviewsAction; } | { addLabel: LabelActionBody; } | { addChatLabel: ChatLabelAssociationActionBody; } | { removeChatLabel: ChatLabelAssociationActionBody; } | { addMessageLabel: MessageLabelAssociationActionBody; } | { removeMessageLabel: MessageLabelAssociationActionBody; } | { quickReply: QuickReplyAction; }
```

## Type declaration

- union member: `{ archive: boolean; lastMessages: LastMessageList; }`
- `archive: boolean`
- `lastMessages: LastMessageList`
- union member: `{ pushNameSetting: string; }`
- `pushNameSetting: string`
- union member: `{ pin: boolean; }`
- `pin: boolean`
- union member: `{ mute: number | null; }`
- `mute: number | null` — mute for duration, or provide timestamp of mute to remove
- union member: `{ clear: boolean; lastMessages: LastMessageList; }`
- `clear: boolean`
- `lastMessages: LastMessageList`
- union member: `{ deleteForMe: { deleteMedia: boolean; key: WAMessageKey; timestamp: number; }; }`
- `deleteForMe: object`
  - `deleteForMe.deleteMedia: boolean`
  - `deleteForMe.key: WAMessageKey`
  - `deleteForMe.timestamp: number`
- union member: `{ star: { messages: object[]; star: boolean; }; }`
- `star: object`
  - `star.messages: object[]`
  - `star.star: boolean`
- union member: `{ lastMessages: LastMessageList; markRead: boolean; }`
- `lastMessages: LastMessageList`
- `markRead: boolean`
- union member: `{ delete: true; lastMessages: LastMessageList; }`
- `delete: true`
- `lastMessages: LastMessageList`
- union member: `{ contact: IContactAction | null; }`
- `contact: IContactAction | null`
- union member: `{ disableLinkPreviews: IPrivacySettingDisableLinkPreviewsAction; }`
- `disableLinkPreviews: IPrivacySettingDisableLinkPreviewsAction`
- union member: `{ addLabel: LabelActionBody; }`
- `addLabel: LabelActionBody`
- union member: `{ addChatLabel: ChatLabelAssociationActionBody; }`
- `addChatLabel: ChatLabelAssociationActionBody`
- union member: `{ removeChatLabel: ChatLabelAssociationActionBody; }`
- `removeChatLabel: ChatLabelAssociationActionBody`
- union member: `{ addMessageLabel: MessageLabelAssociationActionBody; }`
- `addMessageLabel: MessageLabelAssociationActionBody`
- union member: `{ removeMessageLabel: MessageLabelAssociationActionBody; }`
- `removeMessageLabel: MessageLabelAssociationActionBody`
- union member: `{ quickReply: QuickReplyAction; }`
- `quickReply: QuickReplyAction`
