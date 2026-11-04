# isMissingKeyError

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/chat-utils.ts:150`

```ts
function isMissingKeyError(error: any): boolean
```

Check if an error is a missing app state sync key.
WA Web treats these as "Blocked" (waits for key arrival), not fatal.
In Baileys we retry with a snapshot which may use a different key.
