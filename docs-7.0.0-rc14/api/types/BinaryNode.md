# BinaryNode

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/WABinary/types.ts:9`

```ts
type BinaryNode = object
```

the binary node WA uses internally for communication

this is manipulated soley as an object and it does not have any functions.
This is done for easy serialization, to prevent running into issues with prototypes &
to maintain functional code structure

## Type declaration

- `attrs: object`
  - Index Signature: `[key: string]: string`
- `content?: BinaryNode[] | string | Uint8Array`
- `tag: string`
