# BaileysEventEmitter

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Interface · source `src/Types/Events.ts:174`

## Methods

- `emit<T>(event: T, arg: BaileysEventMap[T]): boolean`
  - Type params: `T extends keyof BaileysEventMap`
- `off<T>(event: T, listener: (arg) => void): void`
  - Type params: `T extends keyof BaileysEventMap`
- `on<T>(event: T, listener: (arg) => void): void`
  - Type params: `T extends keyof BaileysEventMap`
- `removeAllListeners<T>(event: T): void`
  - Type params: `T extends keyof BaileysEventMap`
