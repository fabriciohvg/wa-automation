# proto.Message.IHistorySyncNotification

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Protobuf interface · all fields optional and nullable (`null` omitted below)

## Properties

- `chunkOrder?: number`
- `directPath?: string`
- `encHandle?: string`
- `fileEncSha256?: Uint8Array`
- `fileLength?: number | Long`
- `fileSha256?: Uint8Array`
- `fullHistorySyncOnDemandRequestMetadata?: IFullHistorySyncOnDemandRequestMetadata`
- `initialHistBootstrapInlinePayload?: Uint8Array`
- `mediaKey?: Uint8Array`
- `messageAccessStatus?: IHistorySyncMessageAccessStatus`
- `oldestMsgInChunkTimestampSec?: number | Long`
- `originalMessageId?: string`
- `peerDataRequestSessionId?: string`
- `progress?: number`
- `syncType?: HistorySyncType`
