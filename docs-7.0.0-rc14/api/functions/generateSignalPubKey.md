# generateSignalPubKey

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/crypto.ts:11`

```ts
function generateSignalPubKey(pubKey: Uint8Array | Buffer<ArrayBufferLike>): Uint8Array | Buffer<ArrayBufferLike>
```

prefix version byte to the pub keys, required for some curve crypto functions
