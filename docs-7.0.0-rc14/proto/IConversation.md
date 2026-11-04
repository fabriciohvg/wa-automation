# proto.IConversation

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Protobuf interface · all fields optional and nullable (`null` omitted below)

## Properties

- `accountLid?: string`
- `archived?: boolean`
- `capiCreatedGroup?: boolean`
- `commentsCount?: number`
- `contactPrimaryIdentityKey?: Uint8Array`
- `conversationTimestamp?: number | Long`
- `createdAt?: number | Long`
- `createdBy?: string`
- `description?: string`
- `disappearingMode?: IDisappearingMode`
- `displayName?: string`
- `endOfHistoryTransfer?: boolean`
- `endOfHistoryTransferType?: EndOfHistoryTransferType`
- `ephemeralExpiration?: number`
- `ephemeralSettingTimestamp?: number | Long`
- `id?: string`
- `isDefaultSubgroup?: boolean`
- `isParentGroup?: boolean`
- `lastMsgTimestamp?: number | Long`
- `lidJid?: string`
- `lidOriginType?: string`
- `limitSharing?: boolean`
- `limitSharingInitiatedByMe?: boolean`
- `limitSharingSettingTimestamp?: number | Long`
- `limitSharingTrigger?: TriggerType`
- `locked?: boolean`
- `maibaAiThreadEnabled?: boolean`
- `markedAsUnread?: boolean`
- `mediaVisibility?: MediaVisibility`
- `messages?: IHistorySyncMsg[]`
- `muteEndTime?: number | Long`
- `name?: string`
- `newJid?: string`
- `notSpam?: boolean`
- `oldJid?: string`
- `parentGroupId?: string`
- `participant?: IGroupParticipant[]`
- `pHash?: string`
- `pinned?: number`
- `pnhDuplicateLidThread?: boolean`
- `pnJid?: string`
- `readOnly?: boolean`
- `shareOwnPn?: boolean`
- `support?: boolean`
- `suspended?: boolean`
- `systemMessageToInsert?: PrivacySystemMessage`
- `tcToken?: Uint8Array`
- `tcTokenSenderTimestamp?: number | Long`
- `tcTokenTimestamp?: number | Long`
- `terminated?: boolean`
- `unreadCount?: number`
- `unreadMentionCount?: number`
- `username?: string`
- `wallpaper?: IWallpaperSettings`
