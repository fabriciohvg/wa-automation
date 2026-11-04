# SignalRepository

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Signal.ts:58`

```ts
type SignalRepository = object
```

## Type declaration

- `decryptGroupMessage(opts: DecryptGroupSignalOpts) => Promise<Uint8Array>`
- `decryptMessage(opts: DecryptSignalProtoOpts) => Promise<Uint8Array>`
- `deleteSession(jids: string[]) => Promise<void>`
- `encryptGroupMessage(opts: EncryptGroupMessageOpts) => Promise<{ ciphertext: Uint8Array; senderKeyDistributionMessage: Uint8Array; }>`
- `encryptMessage(opts: EncryptMessageOpts) => Promise<{ ciphertext: Uint8Array; type: "pkmsg" | "msg"; }>`
- `getSenderKeyDistributionMessage(opts: GetSenderKeyDistributionMessageOpts) => Promise<Uint8Array>`
- `getSessionInfo(jid: string) => Promise<null | { baseKey: Uint8Array; registrationId: number; }>`
- `hasSenderKey(opts: GetSenderKeyDistributionMessageOpts) => Promise<boolean>`
- `injectE2ESession(opts: E2ESessionOpts) => Promise<void>`
- `jidToSignalProtocolAddress(jid: string) => string`
- `migrateSession(fromJid: string, toJid: string) => Promise<{ migrated: number; skipped: number; total: number; }>`
- `processSenderKeyDistributionMessage(opts: ProcessSenderKeyDistributionMessageOpts) => Promise<void>`
- `validateSession(jid: string) => Promise<{ exists: boolean; reason: string; }>`
- `validateSession(jid: string) => Promise<{ exists: boolean; reason: string; }>`
