# AuthenticationCreds

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Auth.ts:48`

```ts
type AuthenticationCreds = SignalCreds & object
```

## Type declaration

- `account?: IADVSignedDeviceIdentity`
- `accountSettings: AccountSettings`
- `accountSyncCounter: number` — number of times history & app state has been synced
- `additionalData?: any`
- `advSecretKey: string`
- `firstUnuploadedPreKeyId: number`
- `lastAccountSyncTimestamp?: number`
- `lastPropHash: string | undefined`
- `me?: Contact`
- `myAppStateKeyId?: string`
- `nextPreKeyId: number`
- `readonly noiseKey: KeyPair`
- `pairingCode: string | undefined`
- `readonly pairingEphemeralKeyPair: KeyPair`
- `platform?: string`
- `processedHistoryMessages: MinimalMessage[]`
- `registered: boolean`
- `routingInfo: Buffer | undefined`
- `signalIdentities?: SignalIdentity[]`
