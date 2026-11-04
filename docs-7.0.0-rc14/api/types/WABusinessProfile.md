# WABusinessProfile

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/index.ts:54`

```ts
type WABusinessProfile = object
```

## Type declaration

- `address?: string`
- `business_hours: object`
  - `business_hours.business_config?: WABusinessHoursConfig[]`
  - `business_hours.config?: WABusinessHoursConfig[]`
  - `business_hours.timezone?: string`
- `category?: string`
- `description: string`
- `email: string | undefined`
- `website: string[]`
- `wid?: string`
