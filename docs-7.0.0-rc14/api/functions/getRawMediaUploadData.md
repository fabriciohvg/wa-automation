# getRawMediaUploadData

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages-media.ts:54`

```ts
function getRawMediaUploadData(media: WAMediaUpload, mediaType: "ppic" | "product" | "image" | "video" | "sticker" | "thumbnail-document" | "audio" | "thumbnail-image" | "biz-cover-photo" | "thumbnail-video" | "thumbnail-link" | "gif" | "md-app-state" | "md-msg-hist" | "document" | "ptt" | "product-catalog-image" | "payment-bg-image" | "ptv", logger?: ILogger): Promise<{ fileLength: number; filePath: string; fileSha256: NonSharedBuffer; }>
```
