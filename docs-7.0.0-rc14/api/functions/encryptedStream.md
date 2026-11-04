# encryptedStream

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages-media.ts:385`

```ts
function encryptedStream(media: WAMediaUpload, mediaType: "ppic" | "product" | "image" | "video" | "sticker" | "thumbnail-document" | "audio" | "thumbnail-image" | "biz-cover-photo" | "thumbnail-video" | "thumbnail-link" | "gif" | "md-app-state" | "md-msg-hist" | "document" | "ptt" | "product-catalog-image" | "payment-bg-image" | "ptv", __namedParameters: EncryptedStreamOptions = {}): Promise<{ encFilePath: string; fileEncSha256: NonSharedBuffer; fileLength: number; fileSha256: NonSharedBuffer; mac: Buffer<ArrayBuffer>; mediaKey: NonSharedBuffer; originalFilePath: undefined | string; }>
```
