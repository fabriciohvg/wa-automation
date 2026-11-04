# MediaGenerationOptions

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:354`

```ts
type MediaGenerationOptions = object
```

## Type declaration

- `backgroundColor?: string`
- `font?: number`
- `logger?: ILogger`
- `mediaCache?: CacheStore` — cache media so it does not have to be uploaded again
- `mediaTypeOverride?: MediaType`
- `mediaUploadTimeoutMs?: number`
- `options?: RequestInit`
- `upload: WAMediaUploadFunction`
