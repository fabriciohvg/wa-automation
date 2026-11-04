# addTransactionCapability

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/auth-utils.ts:116`

```ts
function addTransactionCapability(state: SignalKeyStore, logger: ILogger, __namedParameters: TransactionCapabilityOptions): SignalKeyStoreWithTransaction
```

Adds DB-like transaction capability to the SignalKeyStore
Uses AsyncLocalStorage for automatic context management

## Parameters

- `state: SignalKeyStore` — the key store to apply this capability to
- `logger: ILogger` — logger to log events
- `__namedParameters: TransactionCapabilityOptions`
- returns — SignalKeyStore with transaction capability
