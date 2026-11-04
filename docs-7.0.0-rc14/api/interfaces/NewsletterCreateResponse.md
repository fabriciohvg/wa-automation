# NewsletterCreateResponse

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Interface · source `src/Types/Mex.ts:41`

## Properties

- `id: string`
- `state: object`
  - `type: string`
- `thread_metadata: object`
  - `creation_time: string`
  - `description: object`
    - `description.id: string`
    - `description.text: string`
    - `description.update_time: string`
  - `handle: null | string`
  - `invite: string`
  - `name: object`
    - `name.id: string`
    - `name.text: string`
    - `name.update_time: string`
  - `picture: object`
    - `picture.direct_path: string`
    - `picture.id: string`
    - `picture.type: string`
  - `preview: object`
    - `preview.direct_path: string`
    - `preview.id: string`
    - `preview.type: string`
  - `subscribers_count: string`
  - `verification: "VERIFIED" | "UNVERIFIED"`
- `viewer_metadata: object`
  - `mute: "ON" | "OFF"`
  - `role: NewsletterViewRole`
