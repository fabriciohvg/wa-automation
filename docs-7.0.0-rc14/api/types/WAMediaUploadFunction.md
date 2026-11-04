# WAMediaUploadFunction

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:349`

```ts
type WAMediaUploadFunction = (encFilePath: string, opts) => Promise<{ directPath: string; fbid: number; mediaUrl: string; meta_hmac: string; ts: number; }>
```

## Parameters

- `encFilePath: string`
- `opts`
  - `fileEncSha256B64` — `string`
  - `mediaType` — `MediaType`
  - `timeoutMs?` — `number`
