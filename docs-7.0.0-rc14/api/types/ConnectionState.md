# ConnectionState

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/State.ts:17`

```ts
type ConnectionState = object
```

## Type declaration

- `connection: WAConnectionState` — connection is now open, connecting or closed
- `isNewLogin?: boolean` — is this a new login
- `isOnline?: boolean`

  if the client is shown as an active, online client.
  If this is false, the primary phone and other devices will receive notifs

- `lastDisconnect?: object` — the error that caused the connection to close
  - `lastDisconnect.date: Date`
  - `lastDisconnect.error: Boom | Error | undefined`
- `legacy?: object` — legacy connection options
  - `legacy.phoneConnected: boolean`
  - `legacy.user?: Contact`
- `qr?: string` — the current QR code
- `reachoutTimeLock?: ReachoutTimelockState` — When you are in this state, WhatsApp prevents outgoing messages and calls.
- `receivedPendingNotifications?: boolean` — has the device received all pending notifications while it was offline
