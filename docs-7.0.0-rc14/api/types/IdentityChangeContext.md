# IdentityChangeContext

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Utils/identity-change-handler.ts:17`

```ts
type IdentityChangeContext = object
```

## Type declaration

- `assertSessions: (jids: string[], force?: boolean) => Promise<boolean>`
- `debounceCache: NodeCache<boolean>`
- `logger: ILogger`
- `meId: string | undefined`
- `meLid: string | undefined`
- `onBeforeSessionRefresh?: (jid: string) => void`

  Invoked right before `assertSessions` is called for an existing-session identity change.
  Used to kick off fire-and-forget side effects (e.g. tctoken re-issuance) in the same
  order WA Web does — i.e. before the E2E session is re-established.
  Must not throw; implementations are responsible for their own error handling.

- `validateSession: (jid: string) => Promise<{ exists: boolean; reason: string; }>`
