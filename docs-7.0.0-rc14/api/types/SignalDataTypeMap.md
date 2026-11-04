# SignalDataTypeMap

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Auth.ts:74`

```ts
type SignalDataTypeMap = object
```

## Type declaration

- `app-state-sync-key: IAppStateSyncKeyData`
- `app-state-sync-version: LTHashState`
- `device-list: string[]`
- `identity-key: Uint8Array`
- `lid-mapping: string`
- `pre-key: KeyPair`
- `sender-key: Uint8Array`
- `sender-key-memory: object`
  - Index Signature: `[jid: string]: boolean`
- `session: Uint8Array`
- `tctoken: object`
  - `tctoken.senderTimestamp?: number`
  - `tctoken.timestamp?: string`
  - `tctoken.token: Buffer`
