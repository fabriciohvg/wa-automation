# assertMediaContent

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages.ts:1111`

```ts
function assertMediaContent(content: undefined | null | IMessage): IVideoMessage | IImageMessage | IAudioMessage | IDocumentMessage | IStickerMessage
```

Checks whether the given message is a media message; if it is returns the inner content
