# downloadMediaMessage

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages.ts:1047`

```ts
function downloadMediaMessage<Type>(message: WAMessage, type: Type, options: MediaDownloadOptions, ctx?: DownloadMediaMessageContext): Promise<Type extends "buffer" ? Buffer<ArrayBufferLike> : Transform>
```

Downloads the given message. Throws an error if it's not a media message

Type params: `Type extends "buffer" | "stream"`
