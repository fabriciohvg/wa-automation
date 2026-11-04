# SignalDataSet

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Auth.ts:87`

```ts
type SignalDataSet = { [T in keyof SignalDataTypeMap]?: (id: string) => null | SignalDataTypeMap[T] }
```
