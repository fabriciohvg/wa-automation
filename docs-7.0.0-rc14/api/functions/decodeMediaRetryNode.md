# decodeMediaRetryNode

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages-media.ts:950`

```ts
function decodeMediaRetryNode(node: BinaryNode): object
```

## Returns

- `error?: Boom<any>`
- `key: WAMessageKey`
- `media?: object`
  - `media.ciphertext: Uint8Array`
  - `media.iv: Uint8Array`
