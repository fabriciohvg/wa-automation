# MessageContentGenerationOptions

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:369`

```ts
type MessageContentGenerationOptions = MediaGenerationOptions & object
```

## Type declaration

- `getCallLink?: (type: "audio" | "video", event?) => Promise<string | undefined>`
  - param `event?`
    - `startTime` — `number`
- `getProfilePicUrl?: (jid: string, type: "image" | "preview") => Promise<string | undefined>`
- `getUrlInfo?: (text: string) => Promise<WAUrlInfo | undefined>`
- `jid?: string`
