# GroupMetadata

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Interface · source `src/Types/GroupMetadata.ts:16`

## Properties

- `addressingMode?: WAMessageAddressingMode` — group uses 'lid' or 'pn' to send messages
- `announce?: boolean` — is set when the group only allows admins to write messages
- `author?: string` — the person who added you to group or changed some setting in group
- `authorPn?: string`
- `authorUsername?: string`
- `creation?: number`
- `desc?: string`
- `descId?: string`
- `descOwner?: string`
- `descOwnerPn?: string`
- `descOwnerUsername?: string`
- `descTime?: number`
- `ephemeralDuration?: number`
- `id: string`
- `inviteCode?: string`
- `isCommunity?: boolean` — is this a community
- `isCommunityAnnounce?: boolean` — is this the announce of a community
- `joinApprovalMode?: boolean` — Request approval to join the group
- `linkedParent?: string` — if this group is part of a community, it returns the jid of the community to which it belongs
- `memberAddMode?: boolean` — is set when the group also allows members to add participants
- `notify?: string`
- `owner: undefined | string`
- `owner_country_code?: string`
- `ownerPn?: string`
- `ownerUsername?: string`
- `participants: GroupParticipant[]`
- `restrict?: boolean` — is set when the group only allows admins to change group settings
- `size?: number` — number of group participants
- `subject: string`
- `subjectOwner?: string` — group subject owner
- `subjectOwnerPn?: string`
- `subjectOwnerUsername?: string`
- `subjectTime?: number` — group subject modification date
