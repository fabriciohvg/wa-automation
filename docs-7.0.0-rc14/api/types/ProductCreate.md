# ProductCreate

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Type alias · source `src/Types/Product.ts:40`

```ts
type ProductCreate = ProductBase & object
```

## Type declaration

- `images: WAMediaUpload[]` — images of the product
- `originCountryCode: string | undefined` — ISO country code for product origin. Set to undefined for no country
