# AnyMediaMessageContent

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Message.ts:174`

```ts
type AnyMediaMessageContent = object & Mentionable & Contextable & WithDimensions | object & Mentionable & Contextable & WithDimensions | { audio: WAMediaUpload; ptt: boolean; seconds: number; } | object & WithDimensions | object & Contextable & object & Editable & object
```

## Type declaration

- `mimetype?: string`

## Type declaration

- `albumParentKey?: WAMessageKey` — key of the parent albumMessage to associate this media with
