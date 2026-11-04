# IdentityChangeResult

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Utils/identity-change-handler.ts:6`

```ts
type IdentityChangeResult = { action: "no_identity_node"; } | { action: "invalid_notification"; } | { action: "skipped_companion_device"; device: number; } | { action: "skipped_self_primary"; } | { action: "debounced"; } | { action: "skipped_offline"; } | { action: "skipped_no_session"; } | { action: "session_refreshed"; } | { action: "session_refresh_failed"; error: unknown; }
```
