# debouncedTimeout

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/generics.ts:108`

```ts
function debouncedTimeout(intervalMs: number = 1000, task?: () => void): object
```

## Returns

- `cancel: () => void`
- `setInterval: (newInterval: number) => number`
- `setTask: (newTask: () => void) => () => void`
  - returns:
    - `Returns` — `void`
- `start: (newIntervalMs?: number, newTask?: () => void) => void`
