# USyncContactProtocol

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Class · source `src/WAUSync/Protocols/USyncContactProtocol.ts:5`

## Constructors

- `new USyncContactProtocol(): USyncContactProtocol`

## Properties

- `name: string = 'contact'` — The name of the protocol

## Methods

- `getQueryElement(): BinaryNode` — Defines what goes inside the query part of a USyncQuery
- `getUserElement(user: USyncUser): BinaryNode` — Defines what goes inside the user part of a USyncQuery
- `parser(node: BinaryNode): boolean` — Parse the result of the query
  - returns — Whatever the protocol is supposed to return
