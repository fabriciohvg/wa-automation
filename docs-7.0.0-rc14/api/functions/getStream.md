# getStream

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages-media.ts:304`

```ts
function getStream(item: WAMediaUpload, opts?: RequestInit & object): Promise<{ stream: Readable; type: "buffer"; } | { stream: Readable; type: "readable"; } | { stream: Readable; type: "remote"; } | { stream: ReadStream; type: "file"; }>
```
