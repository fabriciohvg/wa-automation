# Contact

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Interface · source `src/Types/Contact.ts:1`

## Properties

- `id: string` — ID either in lid or jid format (preferred) *
- `imgUrl?: null | string`

  Url of the profile picture of the contact

  'changed' => if the profile picture has changed
  null => if the profile picture has not been set (default profile picture)
  any other string => url of the profile picture

- `lid?: string` — ID in LID format (@lid) *
- `name?: string` — name of the contact, you have saved on your WA
- `notify?: string` — name of the contact, the contact has set on their own on WA
- `phoneNumber?: string` — ID in PN format (@s.whatsapp.net)  *
- `status?: string`
- `username?: string` — username associated with this contact, when provided by WA
- `verifiedName?: string` — I have no idea
