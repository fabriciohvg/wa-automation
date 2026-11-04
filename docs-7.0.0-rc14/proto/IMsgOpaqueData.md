# proto.IMsgOpaqueData

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Protobuf interface · all fields optional and nullable (`null` omitted below)

## Properties

- `body?: string`
- `botMessageSecret?: Uint8Array`
- `caption?: string`
- `clientUrl?: string`
- `correctOptionIndex?: number`
- `description?: string`
- `encIv?: Uint8Array`
- `encPayload?: Uint8Array`
- `encPollVote?: IPollEncValue`
- `encReactionEncIv?: Uint8Array`
- `encReactionEncPayload?: Uint8Array`
- `encReactionTargetMessageKey?: string`
- `eventDescription?: string`
- `eventEndTime?: number | Long`
- `eventExtraGuestsAllowed?: boolean`
- `eventIsScheduledCall?: boolean`
- `eventJoinLink?: string`
- `eventLocation?: IEventLocation`
- `eventName?: string`
- `eventStartTime?: number | Long`
- `futureproofBuffer?: Uint8Array`
- `isEventCanceled?: boolean`
- `isLive?: boolean`
- `isSentCagPollCreation?: boolean`
- `lat?: number`
- `lng?: number`
- `loc?: string`
- `matchedText?: string`
- `messageSecret?: Uint8Array`
- `originalSelfAuthor?: string`
- `paymentAmount1000?: number`
- `paymentNoteMsgBody?: string`
- `plainProtobufBytes?: Uint8Array`
- `pollContentType?: PollContentType`
- `pollName?: string`
- `pollOptions?: IPollOption[]`
- `pollSelectableOptionsCount?: number`
- `pollType?: PollType`
- `pollUpdateParentKey?: string`
- `pollVotesSnapshot?: IPollVotesSnapshot`
- `senderTimestampMs?: number | Long`
- `targetMessageKey?: string`
- `title?: string`
