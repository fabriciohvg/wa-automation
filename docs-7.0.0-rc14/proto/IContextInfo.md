# proto.IContextInfo

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Protobuf interface · all fields optional and nullable (`null` omitted below)

## Properties

- `actionLink?: IActionLink`
- `alwaysShowAdAttribution?: boolean`
- `botMessageSharingInfo?: IBotMessageSharingInfo`
- `businessMessageForwardInfo?: IBusinessMessageForwardInfo`
- `conversionData?: Uint8Array`
- `conversionDelaySeconds?: number`
- `conversionSource?: string`
- `ctwaPayload?: Uint8Array`
- `ctwaSignals?: string`
- `dataSharingContext?: IDataSharingContext`
- `disappearingMode?: IDisappearingMode`
- `entryPointConversionApp?: string`
- `entryPointConversionDelaySeconds?: number`
- `entryPointConversionExternalMedium?: string`
- `entryPointConversionExternalSource?: string`
- `entryPointConversionSource?: string`
- `ephemeralSettingTimestamp?: number | Long`
- `ephemeralSharedSecret?: Uint8Array`
- `expiration?: number`
- `externalAdReply?: IExternalAdReplyInfo`
- `featureEligibilities?: IFeatureEligibilities`
- `forwardedAiBotMessageInfo?: IForwardedAIBotMessageInfo`
- `forwardedNewsletterMessageInfo?: IForwardedNewsletterMessageInfo`
- `forwardingScore?: number`
- `forwardOrigin?: ForwardOrigin`
- `groupMentions?: IGroupMention[]`
- `groupSubject?: string`
- `isForwarded?: boolean`
- `isGroupStatus?: boolean`
- `isQuestion?: boolean`
- `isSampled?: boolean`
- `memberLabel?: IMemberLabel`
- `mentionedJid?: string[]`
- `nonJidMentions?: number`
- `pairedMediaType?: PairedMediaType`
- `parentGroupJid?: string`
- `participant?: string`
- `placeholderKey?: IMessageKey`
- `questionReplyQuotedMessage?: IQuestionReplyQuotedMessage`
- `quotedAd?: IAdReplyInfo`
- `quotedMessage?: IMessage`
- `quotedType?: QuotedType`
- `rankingVersion?: number`
- `remoteJid?: string`
- `smbClientCampaignId?: string`
- `smbServerCampaignId?: string`
- `stanzaId?: string`
- `statusAttributions?: IStatusAttribution[]`
- `statusAttributionType?: StatusAttributionType`
- `statusAudienceMetadata?: IStatusAudienceMetadata`
- `statusSourceType?: StatusSourceType`
- `trustBannerAction?: number`
- `trustBannerType?: string`
- `urlTrackingMap?: IUrlTrackingMap`
- `utm?: IUTMInfo`
