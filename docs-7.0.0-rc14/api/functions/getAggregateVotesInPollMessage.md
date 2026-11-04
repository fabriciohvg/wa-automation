# getAggregateVotesInPollMessage

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/messages.ts:936`

```ts
function getAggregateVotesInPollMessage(msg: Pick<WAMessage, "message" | "pollUpdates">, meId?: string): VoteAggregation[]
```

Aggregates all poll updates in a poll.

## Parameters

- `msg: Pick<WAMessage, "message" | "pollUpdates">` — the poll creation message
- `meId?: string` — your jid
- returns — A list of options & their voters
