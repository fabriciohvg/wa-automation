# extractE2ESessionFromRetryReceipt

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/signal.ts:92`

```ts
function extractE2ESessionFromRetryReceipt(receipt: BinaryNode): null | { identityKey: Uint8Array | Buffer<ArrayBufferLike>; preKey: undefined | { keyId: number; publicKey: Uint8Array; }; registrationId: number; signedPreKey: { keyId: number; publicKey: Uint8Array | Buffer<ArrayBufferLike>; signature: Uint8Array | Buffer<ArrayBufferLike>; }; }
```
