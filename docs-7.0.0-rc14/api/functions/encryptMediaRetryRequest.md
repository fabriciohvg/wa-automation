# encryptMediaRetryRequest

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages-media.ts:908`

```ts
function encryptMediaRetryRequest(key: WAMessageKey, mediaKey: Uint8Array | Buffer<ArrayBufferLike>, meId: string): BinaryNode
```

Generate a binary node that will request the phone to re-upload the media & return the newly uploaded URL
