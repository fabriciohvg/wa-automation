# AnyRegularMessageContent

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:232`

```ts
type AnyRegularMessageContent = object & Mentionable & Contextable & Editable | AnyMediaMessageContent | { event: EventMessageOptions; } | object & Mentionable & Contextable & Editable | object & Contextable & Mentionable | { contacts: { contacts: IContactMessage[]; displayName: string; }; } | { location: WALocationMessage; } | { react: IReactionMessage; } | { buttonReply: ButtonReplyInfo; type: "template" | "plain"; } | { groupInvite: GroupInviteInfo; } | { listReply: Omit<IListResponseMessage, "contextInfo">; } | { pin: WAMessageKey; time: 86400 | 604800 | 2592000; type: Type; } | { body: string; businessOwnerJid: string; footer: string; product: WASendableProduct; } | SharePhoneNumber | RequestPhoneNumber & ViewOnce
```
