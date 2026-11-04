# PollMessageOptions

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:137`

```ts
type PollMessageOptions = object
```

## Type declaration

- `messageSecret?: Uint8Array` — 32 byte message secret to encrypt poll selections
- `name: string`
- `selectableCount?: number`
- `toAnnouncementGroup?: boolean`
- `values: string[]`
