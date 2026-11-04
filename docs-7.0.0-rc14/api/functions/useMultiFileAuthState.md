# useMultiFileAuthState

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/use-multi-file-auth-state.ts:33`

```ts
function useMultiFileAuthState(folder: string): Promise<{ saveCreds: () => Promise<void>; state: AuthenticationState; }>
```

stores the full authentication state in a single folder.
Far more efficient than singlefileauthstate

Again, I wouldn't endorse this for any production level use other than perhaps a bot.
Would recommend writing an auth state for use with a proper SQL or No-SQL DB
