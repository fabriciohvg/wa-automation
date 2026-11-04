# Curve

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Variable · source `src/Utils/crypto.ts:14`

```ts
const Curve: object
```

## Type declaration

- `generateKeyPair: () => KeyPair`
- `sharedKey: (privateKey: Uint8Array, publicKey: Uint8Array) => Buffer<ArrayBuffer>`
- `sign: (privateKey: Uint8Array, buf: Uint8Array) => Uint8Array`
- `verify: (pubKey: Uint8Array, message: Uint8Array, signature: Uint8Array) => boolean`
