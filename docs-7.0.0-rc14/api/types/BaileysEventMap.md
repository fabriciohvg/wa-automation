# BaileysEventMap

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Events.ts:20`

```ts
type BaileysEventMap = object
```

## Type declaration

- `blocklist.set: object`
  - `blocklist: string[]`
- `blocklist.update: object`
  - `blocklist: string[]`
  - `type: "add" | "remove"`
- `call: WACallEvent[]` — Receive an update on a call, including when the call was received, rejected, accepted
- `chats.delete: string[]` — delete chats with given ID
- `chats.lock: object` — Settings and actions sync events
  - `id: string`
  - `locked: boolean`
- `chats.update: ChatUpdate[]` — update the given chats
- `chats.upsert: Chat[]` — upsert chats
- `connection.update: Partial<ConnectionState>` — connection state has been updated -- WS closed, opened, connecting etc.
- `contacts.update: Partial<Contact>[]`
- `contacts.upsert: Contact[]`
- `creds.update: Partial<AuthenticationCreds>` — credentials updated -- some metadata, keys or something
- `group-participants.update: object` — apply an action to participants in a group
  - `action: ParticipantAction`
  - `author: string`
  - `authorPn?: string`
  - `authorUsername?: string`
  - `id: string`
  - `participants: GroupParticipant[]`
- `group.join-request: object`
  - `action: RequestJoinAction`
  - `author: string`
  - `authorPn?: string`
  - `authorUsername?: string`
  - `id: string`
  - `method: RequestJoinMethod`
  - `participant: string`
  - `participantPn?: string`
- `group.member-tag.update: object`
  - `groupId: string`
  - `label: string`
  - `messageTimestamp?: number`
  - `participant: string`
  - `participantAlt?: string`
- `groups.update: Partial<GroupMetadata>[]`
- `groups.upsert: GroupMetadata[]`
- `labels.association: object`
  - `association: LabelAssociation`
  - `type: "add" | "remove"`
- `labels.edit: Label`
- `lid-mapping.update: LIDMapping`
- `message-capping.update: NewChatMessageCapInfo`
- `message-receipt.update: MessageUserReceiptUpdate[]`
- `messages.delete: { keys: WAMessageKey[]; } | { all: true; jid: string; }`
- `messages.media-update: object[]`
- `messages.reaction: object[]` — message was reacted to. If reaction was removed -- then "reaction.text" will be falsey
- `messages.update: WAMessageUpdate[]`
- `messages.upsert: object`

  add/update the given messages. If they were received while the connection was online,
  the update will have type: "notify"
  if requestId is provided, then the messages was received from the phone due to it being unavailable

  - `messages: WAMessage[]`
  - `requestId?: string`
  - `type: MessageUpsertType`
- `messaging-history.set: object` — set chats (history sync), everything is reverse chronologically sorted
  - `chats: Chat[]`
  - `chunkOrder?: number | null`
  - `contacts: Contact[]`
  - `isLatest?: boolean`
  - `lidPnMappings?: LIDMapping[]`
  - `messages: WAMessage[]`
  - `pastParticipants?: IPastParticipants[] | null`
  - `peerDataRequestSessionId?: string | null`
  - `progress?: number | null`
  - `syncType?: HistorySyncType | null`
- `messaging-history.status: object` — signals history sync milestones (completion or stall) per sync type
  - `explicit: boolean`

    progress === 100 was received from the server.
    when false, completion was inferred via timeout (no more chunks arriving).

  - `status: "complete" | "paused"` — the status of this sync phase
  - `syncType: HistorySyncType` — which sync phase this status refers to
- `newsletter-participants.update: object`
  - `action: string`
  - `author: string`
  - `id: string`
  - `new_role: string`
  - `user: string`
- `newsletter-settings.update: object`
  - `id: string`
  - `update: any`
- `newsletter.reaction: object` — Newsletter-related events
  - `id: string`
  - `reaction: object`
    - `code?: string`
    - `count?: number`
    - `removed?: boolean`
  - `server_id: string`
- `newsletter.view: object`
  - `count: number`
  - `id: string`
  - `server_id: string`
- `presence.update: object` — presence of contact in a chat updated
  - `id: string`
  - `presences: object`
    - Index Signature: `[participant: string]: PresenceData`
- `settings.update: { setting: "unarchiveChats"; value: boolean; } | { setting: "locale"; value: string; } | { setting: "disableLinkPreviews"; value: IPrivacySettingDisableLinkPreviewsAction; } | { setting: "timeFormat"; value: ITimeFormatAction; } | { setting: "privacySettingRelayAllCalls"; value: IPrivacySettingRelayAllCalls; } | { setting: "statusPrivacy"; value: IStatusPrivacyAction; } | { setting: "notificationActivitySetting"; value: NotificationActivitySetting; } | { setting: "channelsPersonalisedRecommendation"; value: IPrivacySettingChannelsPersonalisedRecommendationAction; }`
