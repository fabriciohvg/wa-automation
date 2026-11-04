# aesDecrypt

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/crypto.ts:86`

```ts
function aesDecrypt(buffer: Uint8Array, key: Uint8Array): Buffer<ArrayBuffer>
```

decrypt AES 256 CBC; where the IV is prefixed to the buffer
