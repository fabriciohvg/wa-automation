# makeLtHashGenerator

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/chat-utils.ts:77`

```ts
function makeLtHashGenerator(__namedParameters: Pick<LTHashState, "hash" | "indexValueMap">): object
```

## Returns

- `finish: () => object`
  - returns:
    - `hash: Buffer<ArrayBuffer>`
    - `indexValueMap: object`
      - Index Signature: `[indexMacBase64: string]: object`
- `mix: (__namedParameters: Mac) => void`
