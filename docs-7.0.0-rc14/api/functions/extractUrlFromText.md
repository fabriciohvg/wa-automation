# extractUrlFromText

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages.ts:90`

```ts
function extractUrlFromText(text: string): undefined | string
```

Uses a regex to test whether the string contains a URL, and returns the URL if it does.

## Parameters

- `text: string` — eg. hello https://google.com
- returns — the URL, eg. https://google.com
