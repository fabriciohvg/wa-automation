# proto.IHistorySync

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Protobuf interface · all fields optional and nullable (`null` omitted below)

## Properties

- `accounts?: IAccount[]`
- `aiWaitListState?: BotAIWaitListState`
- `callLogRecords?: ICallLogRecord[]`
- `chunkOrder?: number`
- `companionMetaNonce?: string`
- `conversations?: IConversation[]`
- `globalSettings?: IGlobalSettings`
- `pastParticipants?: IPastParticipants[]`
- `phoneNumberToLidMappings?: IPhoneNumberToLIDMapping[]`
- `progress?: number`
- `pushnames?: IPushname[]`
- `recentStickers?: IStickerMetadata[]`
- `shareableChatIdentifierEncryptionKey?: Uint8Array`
- `statusV3Messages?: IWebMessageInfo[]`
- `syncType?: HistorySyncType`
- `threadDsTimeframeOffset?: number`
- `threadIdUserSecret?: Uint8Array`
