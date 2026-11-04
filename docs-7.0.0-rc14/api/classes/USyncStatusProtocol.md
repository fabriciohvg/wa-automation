# USyncStatusProtocol

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Class · source `src/WAUSync/Protocols/USyncStatusProtocol.ts:9`

## Constructors

- `new USyncStatusProtocol(): USyncStatusProtocol`

## Properties

- `name: string = 'status'` — The name of the protocol

## Methods

- `getQueryElement(): BinaryNode` — Defines what goes inside the query part of a USyncQuery
- `getUserElement(): null` — Defines what goes inside the user part of a USyncQuery
- `parser(node: BinaryNode): undefined | StatusData` — Parse the result of the query
  - returns — Whatever the protocol is supposed to return
