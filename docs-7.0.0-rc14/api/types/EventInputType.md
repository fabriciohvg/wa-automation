# EventInputType

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/WAM/constants.ts:22879`

```ts
type EventInputType = { [key in Event["name"]]: { globals: (x: string) => Value; props: { [k in keyof EventByName<key>["props"]]: Value } } } & object
```
