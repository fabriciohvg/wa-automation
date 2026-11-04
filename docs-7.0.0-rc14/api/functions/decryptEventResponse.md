# decryptEventResponse

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/process-message.ts:269`

```ts
function decryptEventResponse(response: IPollEncValue, ctx: EventContext): EventResponseMessage
```

Decrypt an event response

## Parameters

- `response: IPollEncValue` — encrypted event response
- `ctx: EventContext` — additional info about the event required for decryption
- returns — event response message
