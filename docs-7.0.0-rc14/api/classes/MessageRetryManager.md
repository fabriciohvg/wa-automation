# MessageRetryManager

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Class · source `src/Utils/message-retry-manager.ts:65`

## Constructors

- `new MessageRetryManager(logger: ILogger, maxMsgRetryCount: number): MessageRetryManager`

## Methods

- `addRecentMessage(to: string, id: string, message: IMessage): void` — Add a recent message to the cache for retry handling
- `cancelPendingPhoneRequest(messageId: string): void` — Cancel pending phone request
- `clear(): void`
- `deleteBaseKey(addr: string, msgId: string): void`
- `getRecentMessage(to: string, id: string): undefined | RecentMessage` — Get a recent message from the cache
- `getRetryCount(messageId: string): number` — Get retry count for a message
- `hasExceededMaxRetries(messageId: string): boolean` — Check if message has exceeded maximum retry attempts
- `hasSameBaseKey(addr: string, msgId: string, baseKey: Uint8Array): boolean`
- `incrementRetryCount(messageId: string): number` — Increment retry counter for a message
- `isMacError(errorCode: undefined | RetryReason): boolean` — Check if an error code indicates a MAC failure
- `markRetryFailed(messageId: string): void` — Mark retry as failed
- `markRetrySuccess(messageId: string): void` — Mark retry as successful
- `parseRetryErrorCode(errorAttr: undefined | string): undefined | RetryReason`

  Parse error code from retry receipt's retry node.
  Returns undefined if no error code is present.

- `saveBaseKey(addr: string, msgId: string, baseKey: Uint8Array): void`
- `schedulePhoneRequest(messageId: string, callback: () => void, delay: number = PHONE_REQUEST_DELAY): void` — Schedule a phone request with delay
- `shouldRecreateSession(jid: string, hasSession: boolean, errorCode?: RetryReason): object`

  Check if a session should be recreated based on retry count, history, and error code.
  MAC errors (codes 4 and 7) trigger immediate session recreation regardless of timeout.

  - returns:
    - `reason: string`
    - `recreate: boolean`
