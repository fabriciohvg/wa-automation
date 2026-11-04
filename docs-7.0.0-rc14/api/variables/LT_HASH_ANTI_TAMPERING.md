# LT_HASH_ANTI_TAMPERING

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Variable · source `src/Utils/lt-hash.ts:8`

```ts
const LT_HASH_ANTI_TAMPERING: LTHashAntiTampering
```

LT Hash is a summation based hash algorithm that maintains the integrity of a piece of data
over a series of mutations. You can add/remove mutations and it'll return a hash equal to
if the same series of mutations was made sequentially.
