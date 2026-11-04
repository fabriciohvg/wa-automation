# URLGenerationOptions

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Utils/link-preview.ts:15`

```ts
type URLGenerationOptions = object
```

## Type declaration

- `fetchOpts: object`
  - `fetchOpts.headers?: HeadersInit`
  - `fetchOpts.proxyUrl?: string`
  - `fetchOpts.timeout: number` — Timeout in ms
- `logger?: ILogger`
- `thumbnailWidth: number`
- `uploadImage?: WAMediaUploadFunction`
