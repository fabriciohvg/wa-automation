# getUrlInfo

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/link-preview.ts:33`

```ts
function getUrlInfo(text: string, opts: URLGenerationOptions = ...): Promise<undefined | WAUrlInfo>
```

Given a piece of text, checks for any URL present, generates link preview for the same and returns it
Return undefined if the fetch failed or no URL was found

## Parameters

- `text: string` — first matched URL in text
- `opts: URLGenerationOptions = ...`
- returns — the URL info required to generate link preview
