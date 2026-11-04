# USyncDeviceProtocol

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Class · source `src/WAUSync/Protocols/USyncDeviceProtocol.ts:22`

## Constructors

- `new USyncDeviceProtocol(): USyncDeviceProtocol`

## Properties

- `name: string = 'devices'` — The name of the protocol

## Methods

- `getQueryElement(): BinaryNode` — Defines what goes inside the query part of a USyncQuery
- `getUserElement(): null | BinaryNode` — Defines what goes inside the user part of a USyncQuery
- `parser(node: BinaryNode): ParsedDeviceInfo` — Parse the result of the query
  - returns — Whatever the protocol is supposed to return
