# proto.IPaymentInfo

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Protobuf interface · all fields optional and nullable (`null` omitted below)

## Properties

- `amount1000?: number | Long`
- `currency?: string`
- `currencyDeprecated?: Currency`
- `exchangeAmount?: IMoney`
- `expiryTimestamp?: number | Long`
- `futureproofed?: boolean`
- `primaryAmount?: IMoney`
- `receiverJid?: string`
- `requestMessageKey?: IMessageKey`
- `status?: Status`
- `transactionTimestamp?: number | Long`
- `txnStatus?: TxnStatus`
- `useNoviFiatFormat?: boolean`
