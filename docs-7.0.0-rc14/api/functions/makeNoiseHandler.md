# makeNoiseHandler

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/noise-handler.ts:52`

```ts
function makeNoiseHandler(__namedParameters): object
```

## Parameters

- `__namedParameters`
  - `keyPair` — `KeyPair`
  - `logger` — `ILogger`
  - `NOISE_HEADER` — `Uint8Array`
  - `routingInfo?` — `Buffer`<`ArrayBufferLike`>

## Returns

- `authenticate: (data: Uint8Array) => void`
- `decodeFrame: (newData: Uint8Array | Buffer<ArrayBufferLike>, onFrame: (buff) => void) => Promise<void>`
- `decrypt: (ciphertext: Uint8Array) => Uint8Array`
- `encodeFrame: (data: Uint8Array | Buffer<ArrayBufferLike>) => Buffer<ArrayBuffer>`
- `encrypt: (plaintext: Uint8Array) => Uint8Array`
- `finishInit: () => Promise<void>`
- `mixIntoKey: (data: Uint8Array) => void`
- `processHandshake: (__namedParameters: HandshakeMessage, noiseKey: KeyPair) => Uint8Array`
