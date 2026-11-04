# downloadEncryptedContent

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages-media.ts:553`

```ts
function downloadEncryptedContent(downloadUrl: string, __namedParameters: MediaDecryptionKeyInfo, __namedParameters: MediaDownloadOptions = {}): Promise<Transform>
```

Decrypts and downloads an AES256-CBC encrypted file given the keys.
Assumes the SHA256 of the plaintext is appended to the end of the ciphertext
