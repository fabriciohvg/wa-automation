# decryptPollVote

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/process-message.ts:239`

```ts
function decryptPollVote(vote: IPollEncValue, ctx: PollContext): PollVoteMessage
```

Decrypt a poll vote

## Parameters

- `vote: IPollEncValue` — encrypted vote
- `ctx: PollContext` — additional info about the poll required for decryption
- returns — list of SHA256 options
