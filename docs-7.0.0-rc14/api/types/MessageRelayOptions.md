# MessageRelayOptions

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:315`

```ts
type MessageRelayOptions = MinimalRelayOptions & object
```

## Type declaration

- `additionalAttributes?: object` — additional attributes to add to the WA binary node
  - Index Signature: `[_: string]: string`
- `additionalNodes?: BinaryNode[]`
- `participant?: object` — only send to a specific participant; used when a message decryption fails for a single user
  - `participant.count: number`
  - `participant.jid: string`
- `statusJidList?: string[]` — jid list of participants for status@broadcast
- `useUserDevicesCache?: boolean` — should we use the devices cache, or fetch afresh from the server; default assumed to be "true"
