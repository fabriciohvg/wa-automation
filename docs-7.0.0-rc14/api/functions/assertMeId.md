# assertMeId

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/auth-utils.ts:351`

```ts
function assertMeId(creds: AuthenticationCreds): string
```

Returns the authenticated user's JID, or throws a Boom-401 if creds are not yet authenticated.
Use this anywhere we'd otherwise reach for `creds.me!.id` to fail fast with a descriptive error.
