# decodeMessageNode

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/decode-wa-message.ts:141`

```ts
function decodeMessageNode(stanza: BinaryNode, meId: string, meLid: string): object
```

Decode the received node as a message.

## Returns

- `author: string`
- `fullMessage: WAMessage`
- `sender: string`
- `Note` — this will only parse the message, not decrypt it
