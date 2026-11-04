# fetchLatestBaileysVersion

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/generics.ts:239`

```ts
function fetchLatestBaileysVersion(options: RequestInit = {}): Promise<{ error: undefined; isLatest: boolean; version: WAVersion; } | { error: unknown; isLatest: boolean; version: WAVersion; }>
```

utility that fetches latest baileys version from the master branch.
Use to ensure your WA connection is always on the latest version
