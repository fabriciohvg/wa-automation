# RetryReason

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Enum · source `src/Utils/message-retry-manager.ts:43`

## Enumeration Members

- `AdvFailure: 12`
- `BadBroadcastEphemeralSetting: 10`
- `SignalErrorBadMac: 7` — Explicit MAC failure - session is definitely out of sync
- `SignalErrorFutureMessage: 6`
- `SignalErrorInvalidKey: 2`
- `SignalErrorInvalidKeyId: 3`
- `SignalErrorInvalidMessage: 4` — MAC verification failed - most common cause of decryption failures
- `SignalErrorInvalidMsgKey: 9`
- `SignalErrorInvalidSession: 8`
- `SignalErrorInvalidSignature: 5`
- `SignalErrorNoSession: 1`
- `StatusRevokeDelay: 13`
- `UnknownCompanionNoPrekey: 11`
- `UnknownError: 0`
