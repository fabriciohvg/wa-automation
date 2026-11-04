# aesDecryptGCM

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/crypto.ts:63`

```ts
function aesDecryptGCM(ciphertext: Uint8Array, key: Uint8Array, iv: Uint8Array, additionalData: Uint8Array): Buffer<ArrayBuffer>
```

decrypt AES 256 GCM;
where the auth tag is suffixed to the ciphertext
