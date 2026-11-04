# makeEventBuffer

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/event-buffer.ts:73`

```ts
function makeEventBuffer(logger: ILogger): BaileysBufferableEventEmitter
```

The event buffer logically consolidates different events into a single event
making the data processing more efficient.
