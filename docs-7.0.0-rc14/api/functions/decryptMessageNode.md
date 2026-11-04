# decryptMessageNode

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/decode-wa-message.ts:264`

```ts
function decryptMessageNode(stanza: BinaryNode, meId: string, meLid: string, repository: SignalRepositoryWithLIDStore, logger: ILogger): object
```

## Returns

- `author: string`
- `category: undefined | string = stanza.attrs.category`
- `fullMessage: WAMessage`
- `decrypt() => Promise<void>`
