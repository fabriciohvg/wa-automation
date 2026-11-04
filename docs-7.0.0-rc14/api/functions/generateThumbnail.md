# generateThumbnail

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages-media.ts:328`

```ts
function generateThumbnail(file: string, mediaType: "image" | "video", options): Promise<{ originalImageDimensions: undefined | { height: number; width: number; }; thumbnail: undefined | string; }>
```

generates a thumbnail for a given media, if required

## Parameters

- `file: string`
- `mediaType: "image" | "video"`
- `options`
  - `logger?` — `ILogger`
