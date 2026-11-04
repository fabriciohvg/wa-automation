# MiscMessageGenerationOptions

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:327`

```ts
type MiscMessageGenerationOptions = MinimalRelayOptions & object
```

## Type declaration

- `backgroundColor?: string` — backgroundcolor for status
- `broadcast?: boolean` — if it is broadcast
- `ephemeralExpiration?: number | string` — disappearing messages settings
- `font?: number` — font type for status
- `mediaUploadTimeoutMs?: number` — timeout for media upload to WA server
- `quoted?: WAMessage` — the message you want to quote
- `statusJidList?: string[]` — jid list of participants for status@broadcast
- `timestamp?: Date` — optional, if you want to manually set the timestamp of the message
