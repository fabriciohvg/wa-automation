# getMediaKeys

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages-media.ts:96`

```ts
function getMediaKeys(buffer: undefined | null | string | Uint8Array, mediaType: "ppic" | "product" | "image" | "video" | "sticker" | "thumbnail-document" | "audio" | "thumbnail-image" | "biz-cover-photo" | "thumbnail-video" | "thumbnail-link" | "gif" | "md-app-state" | "md-msg-hist" | "document" | "ptt" | "product-catalog-image" | "payment-bg-image" | "ptv"): Promise<MediaDecryptionKeyInfo>
```

generates all the keys required to encrypt/decrypt & sign a media message
