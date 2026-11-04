# aesEncryptGCM

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/crypto.ts:53`

```ts
function aesEncryptGCM(plaintext: Uint8Array, key: Uint8Array, iv: Uint8Array, additionalData: Uint8Array): Buffer<ArrayBuffer>
```

encrypt AES 256 GCM;
where the tag tag is suffixed to the ciphertext
