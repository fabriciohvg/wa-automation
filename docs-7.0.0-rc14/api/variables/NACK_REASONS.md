# NACK_REASONS

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Variable · source `src/Utils/decode-wa-message.ts:64`

```ts
const NACK_REASONS: object
```

NACK reason codes we send to the server (client → server)

## Type declaration

- `DBOperationFailed: number = 552`
- `InvalidHostedCompanionStanza: number = 493`
- `InvalidProtobuf: number = 491`
- `MessageDeletedOnPeer: number = 499`
- `MissingMessageSecret: number = 495`
- `ParsingError: number = 487`
- `SenderReachoutTimelocked: number = 463`
- `SignalErrorOldCounter: number = 496`
- `UnhandledError: number = 500`
- `UnrecognizedStanza: number = 488`
- `UnrecognizedStanzaClass: number = 489`
- `UnrecognizedStanzaType: number = 490`
- `UnsupportedAdminRevoke: number = 550`
- `UnsupportedLIDGroup: number = 551`
