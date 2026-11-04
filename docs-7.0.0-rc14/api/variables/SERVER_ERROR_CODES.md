# SERVER_ERROR_CODES

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Variable · source `src/Utils/decode-wa-message.ts:86`

```ts
const SERVER_ERROR_CODES: object
```

Server-side error codes returned in ack stanzas (server → client) that we
currently have dedicated handlers for. Extend as more handlers are added.
Distinct from the client-side NackReason enum (WAWebCreateNackFromStanza).

## Type declaration

- `readonly MessageAccountRestriction: "463" = '463'`

  1:1 message missing privacy token (tctoken). Usually means the account is
  restricted: WhatsApp blocks starting new chats but preserves existing ones,
  since established chats already carry a tctoken.

- `readonly SmaxInvalid: "479" = '479'` — Stanza validation failure (SMAX_INVALID) — likely stale device session
