# SignalRepositoryWithLIDStore

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Interface · source `src/Types/Signal.ts:82`

## Extends

- `SignalRepository`

## Properties

- `close?: () => void`
- `lidMapping: LIDMappingStore`

## Methods

- `decryptGroupMessage(opts: DecryptGroupSignalOpts): Promise<Uint8Array>`
- `decryptMessage(opts: DecryptSignalProtoOpts): Promise<Uint8Array>`
- `deleteSession(jids: string[]): Promise<void>`
- `encryptGroupMessage(opts: EncryptGroupMessageOpts): Promise<{ ciphertext: Uint8Array; senderKeyDistributionMessage: Uint8Array; }>`
- `encryptMessage(opts: EncryptMessageOpts): Promise<{ ciphertext: Uint8Array; type: "msg" | "pkmsg"; }>`
- `getSenderKeyDistributionMessage(opts: GetSenderKeyDistributionMessageOpts): Promise<Uint8Array>`
- `getSessionInfo(jid: string): Promise<null | { baseKey: Uint8Array; registrationId: number; }>`
- `hasSenderKey(opts: GetSenderKeyDistributionMessageOpts): Promise<boolean>`
- `injectE2ESession(opts: E2ESessionOpts): Promise<void>`
- `jidToSignalProtocolAddress(jid: string): string`
- `migrateSession(fromJid: string, toJid: string): Promise<{ migrated: number; skipped: number; total: number; }>`
- `processSenderKeyDistributionMessage(opts: ProcessSenderKeyDistributionMessageOpts): Promise<void>`
- `validateSession(jid: string): Promise<{ exists: boolean; reason: string; }>`
- `validateSession(jid: string): Promise<{ exists: boolean; reason: string; }>`
