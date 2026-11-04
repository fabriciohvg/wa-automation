# getAggregateResponsesInEventMessage

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages.ts:992`

```ts
function getAggregateResponsesInEventMessage(msg: Pick<WAMessage, "eventResponses">, meId?: string): ResponseAggregation[]
```

Aggregates all event responses in an event message.

## Parameters

- `msg: Pick<WAMessage, "eventResponses">` — the event creation message
- `meId?: string` — your jid
- returns — A list of response types & their responders
