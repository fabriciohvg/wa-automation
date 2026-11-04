# makeWASocket

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Socket/index.ts:6`

```ts
function makeWASocket(config: UserFacingSocketConfig): object
```

## Returns

- `addChatLabel: (jid: string, labelId: string) => Promise<void>` — Adds label for the chats
- `addLabel: (jid: string, labels: LabelActionBody) => Promise<void>` — Adds label
- `addMessageLabel: (jid: string, messageId: string, labelId: string) => Promise<void>` — Adds label for the message
- `addOrEditContact: (jid: string, contact: IContactAction) => Promise<void>` — Add or Edit Contact
- `addOrEditQuickReply: (quickReply: QuickReplyAction) => Promise<void>` — Add or Edit Quick Reply
- `appPatch: (patchCreate: WAPatchCreate) => Promise<void>`
- `appStatePatchMutex: object`
  - `appStatePatchMutex.mutex(code: () => T | Promise<T>) => Promise<T>`
    - Type params: `T`
- `assertSessions: (jids: string[], force?: boolean) => Promise<boolean>`
- `authState: object`
  - `authState.creds: AuthenticationCreds`
  - `authState.keys: SignalKeyStoreWithTransaction`
- `chatModify: (mod: ChatModification, jid: string) => Promise<void>`

  modify a chat -- mark unread, read etc.
  lastMessages must be sorted in reverse chronologically
  requires the last messages till the last message received; required for archive & unread

- `cleanDirtyBits: (type: "account_sync" | "groups", fromTimestamp?: string | number) => Promise<void>`
- `communityAcceptInvite: (code: string) => Promise<undefined | string>`
- `communityAcceptInviteV4: (...args: [string | WAMessageKey, IGroupInviteMessage]) => Promise<any>` — accept a CommunityInviteMessage
- `communityCreate: (subject: string, body: string) => Promise<null | GroupMetadata>`
- `communityCreateGroup: (subject: string, participants: string[], parentCommunityJid: string) => Promise<null | GroupMetadata>`
- `communityFetchAllParticipating: () => Promise<{}>`
- `communityFetchLinkedGroups: (jid: string) => Promise<{ communityJid: string; isCommunity: boolean; linkedGroups: object[]; }>`
- `communityGetInviteInfo: (code: string) => Promise<GroupMetadata>`
- `communityInviteCode: (jid: string) => Promise<undefined | string>`
- `communityJoinApprovalMode: (jid: string, mode: "on" | "off") => Promise<void>`
- `communityLeave: (id: string) => Promise<void>`
- `communityLinkGroup: (groupJid: string, parentCommunityJid: string) => Promise<void>`
- `communityMemberAddMode: (jid: string, mode: "all_member_add" | "admin_add") => Promise<void>`
- `communityMetadata: (jid: string) => Promise<GroupMetadata>`
- `communityParticipantsUpdate: (jid: string, participants: string[], action: ParticipantAction) => Promise<object[]>`
- `communityRequestParticipantsList: (jid: string) => Promise<object[]>`
- `communityRequestParticipantsUpdate: (jid: string, participants: string[], action: "reject" | "approve") => Promise<object[]>`
- `communityRevokeInvite: (jid: string) => Promise<undefined | string>`
- `communityRevokeInviteV4: (communityJid: string, invitedJid: string) => Promise<boolean>` — revoke a v4 invite for someone
  - param `communityJid: string` — community jid
  - param `invitedJid: string` — jid of person you invited
  - returns — true if successful
- `communitySettingUpdate: (jid: string, setting: "announcement" | "locked" | "not_announcement" | "unlocked") => Promise<void>`
- `communityToggleEphemeral: (jid: string, ephemeralExpiration: number) => Promise<void>`
- `communityUnlinkGroup: (groupJid: string, parentCommunityJid: string) => Promise<void>`
- `communityUpdateDescription: (jid: string, description?: string) => Promise<void>`
- `communityUpdateSubject: (jid: string, subject: string) => Promise<void>`
- `createCallLink: (type: "video" | "audio", event?, timeoutMs?: number) => Promise<undefined | string>`
  - param `event?`
    - `startTime` — `number`
- `createParticipantNodes: (recipientJids: string[], message: IMessage, extraAttrs?, dsmMessage?: IMessage) => Promise<{ nodes: BinaryNode[]; shouldIncludeDeviceIdentity: boolean; }>`
- `devicesMutex: object`
  - `devicesMutex.mutex(code: () => T | Promise<T>) => Promise<T>`
    - Type params: `T`
- `digestKeyBundle: () => Promise<void>`
- `end: (error: undefined | Error) => Promise<void>`
- `ev: BaileysBufferableEventEmitter`
- `executeUSyncQuery: (usyncQuery: USyncQuery) => Promise<undefined | USyncQueryResult>`
- `fetchAccountReachoutTimelock: () => Promise<ReachoutTimelockState>` — Fetches your account's standing when it comes to restrictions.
  - returns — Returns the state of the restrictions.
- `fetchBlocklist: () => Promise<(undefined | string)[]>`
- `fetchDisappearingDuration: (...jids: string[]) => Promise<undefined | USyncQueryResultList[]>`
- `fetchMessageHistory: (count: number, oldestMsgKey: WAMessageKey, oldestMsgTimestamp: number | Long) => Promise<string>`
- `fetchNewChatMessageCap: () => Promise<NewChatMessageCapInfo>` — Fetches your account's new chat limits.
  - returns — Returns the quota and the usage.
- `fetchPrivacySettings: (force: boolean = false) => Promise<{}>`
- `fetchStatus: (...jids: string[]) => Promise<undefined | USyncQueryResultList[]>`
- `generateMessageTag: () => string`
- `getBotListV2: () => Promise<BotListInfo[]>`
- `getBusinessProfile: (jid: string) => Promise<void | WABusinessProfile>`
- `getCatalog: (__namedParameters: GetCatalogOptions) => Promise<{ nextPageCursor: undefined | string; products: Product[]; }>`
- `getCollections: (jid?: string, limit?: number = 51) => Promise<{ collections: CatalogCollection[]; }>`
- `getMediaHost: () => string`
- `getOrderDetails: (orderId: string, tokenBase64: string) => Promise<OrderDetails>`
- `getUSyncDevices: (jids: string[], useCache: boolean, ignoreZeroDevices: boolean) => Promise<DeviceWithJid[]>` — Fetch all the devices we've to send a message to
- `groupAcceptInvite: (code: string) => Promise<undefined | string>`
- `groupAcceptInviteV4: (...args: [string | WAMessageKey, IGroupInviteMessage]) => Promise<any>` — accept a GroupInviteMessage
- `groupCreate: (subject: string, participants: string[]) => Promise<GroupMetadata>`
- `groupFetchAllParticipating: () => Promise<{}>`
- `groupGetInviteInfo: (code: string) => Promise<GroupMetadata>`
- `groupInviteCode: (jid: string) => Promise<undefined | string>`
- `groupJoinApprovalMode: (jid: string, mode: "on" | "off") => Promise<void>`
- `groupLeave: (id: string) => Promise<void>`
- `groupMemberAddMode: (jid: string, mode: "all_member_add" | "admin_add") => Promise<void>`
- `groupMetadata: (jid: string) => Promise<GroupMetadata>`
- `groupParticipantsUpdate: (jid: string, participants: string[], action: ParticipantAction) => Promise<object[]>`
- `groupRequestParticipantsList: (jid: string) => Promise<object[]>`
- `groupRequestParticipantsUpdate: (jid: string, participants: string[], action: "reject" | "approve") => Promise<object[]>`
- `groupRevokeInvite: (jid: string) => Promise<undefined | string>`
- `groupRevokeInviteV4: (groupJid: string, invitedJid: string) => Promise<boolean>` — revoke a v4 invite for someone
  - param `groupJid: string` — group jid
  - param `invitedJid: string` — jid of person you invited
  - returns — true if successful
- `groupSettingUpdate: (jid: string, setting: "announcement" | "locked" | "not_announcement" | "unlocked") => Promise<void>`
- `groupToggleEphemeral: (jid: string, ephemeralExpiration: number) => Promise<void>`
- `groupUpdateDescription: (jid: string, description?: string) => Promise<void>`
- `groupUpdateSubject: (jid: string, subject: string) => Promise<void>`
- `issuePrivacyTokens: (jids: string[], timestamp?: number) => Promise<any>`
- `logger: ILogger = config.logger`
- `logout: (msg?: string) => Promise<void>` — logout & invalidate connection
- `messageMutex: object`
  - `messageMutex.mutex(code: () => T | Promise<T>) => Promise<T>`
    - Type params: `T`
- `messageRetryManager: null | MessageRetryManager`
- `newsletterAdminCount: (jid: string) => Promise<number>`
- `newsletterChangeOwner: (jid: string, newOwnerJid: string) => Promise<void>`
- `newsletterCreate: (name: string, description?: string) => Promise<NewsletterMetadata>`
- `newsletterDelete: (jid: string) => Promise<void>`
- `newsletterDemote: (jid: string, userJid: string) => Promise<void>`
- `newsletterFetchMessages: (jid: string, count: number, since: number, after: number) => Promise<any>`
- `newsletterFollow: (jid: string) => Promise<unknown>`
- `newsletterMetadata: (type: "invite" | "jid", key: string) => Promise<null | NewsletterMetadata>`
- `newsletterMute: (jid: string) => Promise<unknown>`
- `newsletterReactMessage: (jid: string, serverId: string, reaction?: string) => Promise<void>`
- `newsletterRemovePicture: (jid: string) => Promise<unknown>`
- `newsletterSubscribers: (jid: string) => Promise<{ subscribers: number; }>`
- `newsletterUnfollow: (jid: string) => Promise<unknown>`
- `newsletterUnmute: (jid: string) => Promise<unknown>`
- `newsletterUpdate: (jid: string, updates: NewsletterUpdate) => Promise<unknown>`
- `newsletterUpdateDescription: (jid: string, description: string) => Promise<unknown>`
- `newsletterUpdateName: (jid: string, name: string) => Promise<unknown>`
- `newsletterUpdatePicture: (jid: string, content: WAMediaUpload) => Promise<unknown>`
- `notificationMutex: object`
  - `notificationMutex.mutex(code: () => T | Promise<T>) => Promise<T>`
    - Type params: `T`
- `onUnexpectedError: (err: Error | Boom<any>, msg: string) => void` — log & process any unexpected errors
- `onWhatsApp: (...phoneNumber: string[]) => Promise<undefined | object[]>`
- `placeholderResendCache: CacheStore`
- `presenceSubscribe: (toJid: string) => Promise<void>`
  - param `toJid: string` — the jid to subscribe to
- `productCreate: (create: ProductCreate) => Promise<Product>`
- `productDelete: (productIds: string[]) => Promise<{ deleted: number; }>`
- `productUpdate: (productId: string, update: ProductUpdate) => Promise<Product>`
- `profilePictureUrl: (jid: string, type: "image" | "preview", timeoutMs?: number) => Promise<undefined | string>`

  fetch the profile picture of a user/group
  type = "preview" for a low res picture
  type = "image for the high res picture"

- `query: (node: BinaryNode, timeoutMs?: number) => Promise<any>` — send a query, and wait for its response. auto-generates message ID if not provided
- `readMessages: (keys: WAMessageKey[]) => Promise<void>` — Bulk read messages. Keys can be from different chats & participants
- `receiptMutex: object`
  - `receiptMutex.mutex(code: () => T | Promise<T>) => Promise<T>`
    - Type params: `T`
- `refreshMediaConn: (forceGet: boolean = false) => Promise<MediaConnInfo>`
- `registerSocketEndHandler: (handler: (error) => void | Promise<void>) => void`
- `rejectCall: (callId: string, callFrom: string) => Promise<void>`
- `relayMessage: (jid: string, message: IMessage, __namedParameters: MessageRelayOptions) => Promise<string>`
- `removeChatLabel: (jid: string, labelId: string) => Promise<void>` — Removes label for the chat
- `removeContact: (jid: string) => Promise<void>` — Remove Contact
- `removeCoverPhoto: (id: string) => Promise<any>`
- `removeMessageLabel: (jid: string, messageId: string, labelId: string) => Promise<void>` — Removes label for the message
- `removeProfilePicture: (jid: string) => Promise<void>` — remove the profile picture for yourself or a group
- `removeQuickReply: (timestamp: string) => Promise<void>` — Remove Quick Reply
- `requestPairingCode: (phoneNumber: string, customPairingCode?: string) => Promise<string>`
- `requestPlaceholderResend: (messageKey: WAMessageKey, msgData?: Partial<WAMessage>) => Promise<undefined | string>`
- `resyncAppState: (...args: [readonly ("critical_unblock_low" | "regular_high" | "regular_low" | "critical_block" | "regular")[], boolean]) => Promise<void>`
- `rotateSignedPreKey: () => Promise<void>`
- `sendMessage: (jid: string, content: AnyMessageContent, options: MiscMessageGenerationOptions = {}) => Promise<undefined | WAMessage>`
- `sendMessageAck: (node: BinaryNode, errorCode?: number) => Promise<void>`
- `sendNode: (frame: BinaryNode) => Promise<void>` — send a binary node
- `sendPeerDataOperationMessage: (pdoMessage: IPeerDataOperationRequestMessage) => Promise<string>`
- `sendPresenceUpdate: (type: WAPresence, toJid?: string) => Promise<void>`
- `sendRawMessage: (data: Uint8Array | Buffer<ArrayBufferLike>) => Promise<void>` — send a raw buffer
- `sendReceipt: (jid: string, participant: undefined | string, messageIds: string[], type: MessageReceiptType) => Promise<void>`

  generic send receipt function
  used for receipts of phone call, read, delivery etc.

- `sendReceipts: (keys: WAMessageKey[], type: MessageReceiptType) => Promise<void>` — Correctly bulk send receipts to multiple chats, participants
- `sendRetryRequest: (node: BinaryNode, forceIncludeKeys: boolean = false) => Promise<void>`
- `sendUnifiedSession: () => Promise<void>`
- `sendWAMBuffer: (wamBuffer: Buffer) => Promise<any>`
- `serverProps: object`
  - `serverProps.lidTrustedTokenIssueToLid: boolean = false` — AB prop 14303: issue tctokens to LID instead of PN. WA Web default: false.
  - `serverProps.privacyTokenOn1to1: boolean = true` — AB prop 10518: gate tctoken on 1:1 messages. Default true (safe: avoids 463).
  - `serverProps.profilePicPrivacyToken: boolean = true` — AB prop 9666: gate tctoken on profile picture IQs. WA Web default: true.
- `signalRepository: SignalRepositoryWithLIDStore`
- `star: (jid: string, messages: object[], star: boolean) => Promise<void>` — Star or Unstar a message
- `subscribeNewsletterUpdates: (jid: string) => Promise<null | { duration: string; }>`
- `type: "md"`
- `updateBlockStatus: (jid: string, action: "block" | "unblock") => Promise<void>`
- `updateBussinesProfile: (args: UpdateBussinesProfileProps) => Promise<any>`
- `updateCallPrivacy: (value: WAPrivacyCallValue) => Promise<void>`
- `updateCoverPhoto: (photo: WAMediaUpload) => Promise<number>`
- `updateDefaultDisappearingMode: (duration: number) => Promise<void>`
- `updateDisableLinkPreviewsPrivacy: (isPreviewsDisabled: boolean) => Promise<void>` — Enable/Disable link preview privacy, not related to baileys link preview generation
- `updateGroupsAddPrivacy: (value: WAPrivacyGroupAddValue) => Promise<void>`
- `updateLastSeenPrivacy: (value: WAPrivacyValue) => Promise<void>`
- `updateMediaMessage: (message: WAMessage) => Promise<WAMessage>`
- `updateMemberLabel: (jid: string, memberLabel: string) => Promise<string>` — Update Member Label
- `updateMessagesPrivacy: (value: WAPrivacyMessagesValue) => Promise<void>`
- `updateOnlinePrivacy: (value: WAPrivacyOnlineValue) => Promise<void>`
- `updateProfileName: (name: string) => Promise<void>`
- `updateProfilePicture: (jid: string, content: WAMediaUpload, dimensions?) => Promise<void>` — update the profile picture for yourself or a group
  - param `dimensions?`
    - `height` — `number`
    - `width` — `number`
- `updateProfilePicturePrivacy: (value: WAPrivacyValue) => Promise<void>`
- `updateProfileStatus: (status: string) => Promise<void>` — update the profile status for yourself
- `updateReadReceiptsPrivacy: (value: WAReadReceiptsValue) => Promise<void>`
- `updateServerTimeOffset: (__namedParameters: BinaryNode) => void`
- `updateStatusPrivacy: (value: WAPrivacyValue) => Promise<void>`
- `uploadPreKeys: (count: number = MIN_PREKEY_COUNT) => Promise<void>` — generates and uploads a set of pre-keys to the server
- `uploadPreKeysToServerIfRequired: () => Promise<void>`
- `upsertMessage: (...args: [WAMessage, MessageUpsertType]) => Promise<void>`
- `user: undefined | Contact`
- `userDevicesCache: PossiblyExtendedCacheStore | NodeCache<JidWithDevice[]>`
- `waitForConnectionUpdate: (check: (u) => Promise<undefined | boolean>, timeoutMs?: number) => Promise<void>` — Waits for the connection to WA to reach a state
- `waitForMessage: <T>(msgId: string, timeoutMs: timeout after which the promise will reject) => Promise<undefined | T>` — Wait for a message with a certain tag to be received
  - param `msgId: string` — the message tag to await
  - param `timeoutMs: timeout after which the promise will reject` — `undefined` | `number`
  - Type params: `T`
- `waitForSocketOpen: () => Promise<void>`
- `wamBuffer: BinaryInfo = publicWAMBuffer`
- `waUploadToServer: WAMediaUploadFunction`
- `ws: WebSocketClient`
