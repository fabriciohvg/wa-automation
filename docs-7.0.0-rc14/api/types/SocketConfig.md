# SocketConfig

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Socket.ts:33`

```ts
type SocketConfig = object
```

## Type declaration

- `agent?: Agent` — proxy agent
- `appStateMacVerification: object` — verify app state MACs
  - `appStateMacVerification.patch: boolean`
  - `appStateMacVerification.snapshot: boolean`
- `auth: AuthenticationState` — provide an auth state object to maintain the auth state
- `browser: WABrowserDescription` — override browser config
- `cachedGroupMetadata: (jid: string) => Promise<GroupMetadata | undefined>` — cached group metadata, use to prevent redundant requests to WA & speed up msg sending
- `callOfferCache?: CacheStore` — cache to store call offers
- `connectTimeoutMs: number` — Fails the connection if the socket times out in this interval
- `countryCode: string` — alphanumeric country code (USA -> US) for the number used
- `customUploadHosts: MediaConnInfo["hosts"]` — custom upload hosts to upload media to
- `defaultQueryTimeoutMs: number | undefined` — Default timeout for queries, undefined for no timeout
- `emitOwnEvents: boolean` — should events be emitted for actions done by this socket connection
- `enableAutoSessionRecreation: boolean` — Enable automatic session recreation for failed messages
- `enableRecentMessageCache: boolean` — Enable recent message caching for retry handling
- `fetchAgent?: Agent` — agent used for fetch requests -- uploading/downloading media
- `fireInitQueries: boolean` — Should baileys fire init queries automatically, default true
- `generateHighQualityLinkPreview: boolean`

  generate a high quality link preview,
  entails uploading the jpegThumbnail to WA

- `getMessage: (key: WAMessageKey) => Promise<IMessage | undefined>`

  fetch a message from your store
  implement this so that messages failed to send
  (solves the "this message can take a while" issue) can be retried

- `keepAliveIntervalMs: number` — ping-pong interval for WS connection
- `linkPreviewImageThumbnailWidth: number` — width for link preview images
- `logger: ILogger` — logger
- `makeSignalRepository: (auth: SignalAuthState, logger: ILogger, pnToLIDFunc?: (jids) => Promise<LIDMapping[] | undefined>) => SignalRepositoryWithLIDStore`
- `markOnlineOnConnect: boolean` — marks the client as online whenever the socket successfully connects
- `maxMsgRetryCount: number` — max retry count
- `mediaCache?: CacheStore` — provide a cache to store media, so does not have to be re-uploaded
- `mobile?: boolean` — should baileys use the mobile api instead of the multi device api
  - Deprecated:
    This feature has been removed

- `msgRetryCounterCache?: CacheStore`

  map to store the retry counts for failed messages;
  used to determine whether to retry a message or not

- `options: RequestInit` — options for HTTP fetch requests
- `patchMessageBeforeSending: (msg: IMessage, recipientJids?: string[]) => Promise<PatchedMessageWithRecipientJID[] | PatchedMessageWithRecipientJID> | PatchedMessageWithRecipientJID[] | PatchedMessageWithRecipientJID` — Optionally patch the message before sending out
- `placeholderResendCache?: CacheStore` — cache to track placeholder resends
- `printQRInTerminal?: boolean` — should the QR be printed in the terminal
  - Deprecated:
    This feature has been removed

- `pushName?: string` — Initial pushName carried in the registration ClientPayload (used by mock servers for deterministic phone assignment).
- `qrTimeout?: number` — time to wait for the generation of the next QR in ms
- `retryRequestDelayMs: number` — time to wait between sending new retry requests
- `shouldIgnoreJid: (jid: string) => boolean | undefined`

  Returns if a jid should be ignored,
  no event for that jid will be triggered.
  Messages from that jid will also not be decrypted

- `shouldSyncHistoryMessage: (msg: IHistorySyncNotification) => boolean` — manage history processing with this control; by default will sync up everything
- `syncFullHistory: boolean` — Should Baileys ask the phone for full history, will be received async
- `transactionOpts: TransactionCapabilityOptions` — transaction capability options for SignalKeyStore
- `userDevicesCache?: PossiblyExtendedCacheStore` — provide a cache to store a user's device list
- `version: WAVersion` — version to connect with
- `waWebSocketUrl: string | URL` — the WS url to connect to WA
