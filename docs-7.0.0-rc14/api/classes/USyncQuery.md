# USyncQuery

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Class · source `src/WAUSync/USyncQuery.ts:21`

## Constructors

- `new USyncQuery(): USyncQuery`

## Properties

- `context: string`
- `mode: string`
- `protocols: USyncQueryProtocol[]`
- `users: USyncUser[]`

## Methods

- `parseUSyncQueryResult(result: undefined | BinaryNode): undefined | USyncQueryResult`
- `withBotProfileProtocol(): USyncQuery`
- `withContactProtocol(): USyncQuery`
- `withContext(context: string): USyncQuery`
- `withDeviceProtocol(): USyncQuery`
- `withDisappearingModeProtocol(): USyncQuery`
- `withLIDProtocol(): USyncQuery`
- `withMode(mode: string): USyncQuery`
- `withStatusProtocol(): USyncQuery`
- `withUser(user: USyncUser): USyncQuery`
- `withUsernameProtocol(): USyncQuery`
