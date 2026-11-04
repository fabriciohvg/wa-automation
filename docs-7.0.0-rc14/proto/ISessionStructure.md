# proto.ISessionStructure

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Protobuf interface · all fields optional and nullable (`null` omitted below)

## Properties

- `aliceBaseKey?: Uint8Array`
- `localIdentityPublic?: Uint8Array`
- `localRegistrationId?: number`
- `needsRefresh?: boolean`
- `pendingKeyExchange?: IPendingKeyExchange`
- `pendingPreKey?: IPendingPreKey`
- `previousCounter?: number`
- `receiverChains?: IChain[]`
- `remoteIdentityPublic?: Uint8Array`
- `remoteRegistrationId?: number`
- `rootKey?: Uint8Array`
- `senderChain?: IChain`
- `sessionVersion?: number`
