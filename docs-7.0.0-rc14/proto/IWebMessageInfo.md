# proto.IWebMessageInfo

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Protobuf interface · all fields optional and nullable (`null` omitted below)

## Properties

- `agentId?: string`
- `bizPrivacyStatus?: BizPrivacyStatus`
- `botMessageInvokerJid?: string`
- `botTargetId?: string`
- `broadcast?: boolean`
- `clearMedia?: boolean`
- `commentMetadata?: ICommentMetadata`
- `duration?: number`
- `ephemeralDuration?: number`
- `ephemeralOffToOn?: boolean`
- `ephemeralOutOfSync?: boolean`
- `ephemeralStartTimestamp?: number | Long`
- `eventAdditionalMetadata?: IEventAdditionalMetadata`
- `eventResponses?: IEventResponse[]`
- `finalLiveLocation?: ILiveLocationMessage`
- `futureproofData?: Uint8Array`
- `groupHistoryBundleInfo?: IGroupHistoryBundleInfo`
- `groupHistoryIndividualMessageInfo?: IGroupHistoryIndividualMessageInfo`
- `ignore?: boolean`
- `interactiveMessageAdditionalMetadata?: IInteractiveMessageAdditionalMetadata`
- `is1PBizBotMessage?: boolean`
- `isGroupHistoryMessage?: boolean`
- `isMentionedInStatus?: boolean`
- `isSupportAiMessage?: boolean`
- `keepInChat?: IKeepInChat`
- `key?: IMessageKey`
- `labels?: string[]`
- `mediaCiphertextSha256?: Uint8Array`
- `mediaData?: IMediaData`
- `message?: IMessage`
- `messageAddOns?: IMessageAddOn[]`
- `messageC2STimestamp?: number | Long`
- `messageSecret?: Uint8Array`
- `messageStubParameters?: string[]`
- `messageStubType?: StubType`
- `messageTimestamp?: number | Long`
- `multicast?: boolean`
- `newsletterServerId?: number | Long`
- `originalSelfAuthorUserJidString?: string`
- `participant?: string`
- `paymentInfo?: IPaymentInfo`
- `photoChange?: IPhotoChange`
- `pinInChat?: IPinInChat`
- `pollAdditionalMetadata?: IPollAdditionalMetadata`
- `pollUpdates?: IPollUpdate[]`
- `premiumMessageInfo?: IPremiumMessageInfo`
- `pushName?: string`
- `quarantinedMessage?: IQuarantinedMessage`
- `quotedPaymentInfo?: IPaymentInfo`
- `quotedStickerData?: IMediaData`
- `reactions?: IReaction[]`
- `reportingTokenInfo?: IReportingTokenInfo`
- `revokeMessageTimestamp?: number | Long`
- `starred?: boolean`
- `status?: Status`
- `statusAlreadyViewed?: boolean`
- `statusMentionMessageInfo?: IStatusMentionMessage`
- `statusMentions?: string[]`
- `statusMentionSources?: string[]`
- `statusPsa?: IStatusPSA`
- `supportAiCitations?: ICitation[]`
- `targetMessageId?: IMessageKey`
- `urlNumber?: boolean`
- `urlText?: boolean`
- `userReceipt?: IUserReceipt[]`
- `verifiedBizName?: string`
