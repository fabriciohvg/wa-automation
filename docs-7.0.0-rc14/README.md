# Baileys v7 docs for LLM agents

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

## Version this documents

- Library: **Baileys** (WhiskeySockets), WhatsApp Web API over WebSocket, TypeScript/Node.js.
- Version: **`7.0.0-rc14`**, the npm `latest` dist-tag (published 2026-07-29). v7 is still in RC; `6.7.x` is the `legacy` tag.
- API reference generated from Baileys `master` @ `81345beb67ca` (package.json version `7.0.0-rc14`).
- Install: `npm i baileys` (canonical) — `@whiskeysockets/baileys` is published at the same version. The guides import from
  `'@whiskeysockets/baileys'`; use whichever name you installed. The package is **ESM-only** (`"type": "module"`), Node.js **>= 20**.
- If a project pins `6.x`, these docs may not match: read [guides/migration/v7.md](guides/migration/v7.md) for the breaking changes
  (LIDs, ESM, removed APIs). v8 is unreleased and not covered.
- Source: https://github.com/WhiskeySockets/docs (English only; pt-BR, community pages, site config and the v8 preview dropped).

## How to use this directory

1. Task-oriented questions ("how do I send an image / reconnect / use pairing code") -> `guides/`.
2. Exact signatures/fields -> `api/README.md` (index with inlined function signatures), then `api/<kind>/<Name>.md`.
3. Socket methods (`sock.sendMessage`, `sock.groupMetadata`, ...) -> `api/functions/makeWASocket.md`.
4. Raw protobuf shapes (`proto.IMessage`, `proto.Message.IImageMessage`, ...) -> `proto/README.md`.
5. Find any symbol by file name: `**/<Name>.md`, or grep the tree.

## Guides

### Get started

- [Introduction](guides/introduction.md) — What Baileys is, what you can build with it, and what the runtime needs.
- [Installation](guides/installation.md) — Install the stable release or the edge build, plus optional peer dependencies.
- [Quickstart](guides/quickstart.md) — Connect, persist a session, and send your first message in a few minutes.
- [FAQ](guides/faq.md) — Common questions about connections, message delivery, LIDs, and history sync.

### Authentication

- [QR code](guides/authentication/qr-code.md) — Authenticate by scanning a QR code with the WhatsApp mobile app.
- [Pairing code](guides/authentication/pairing-code.md) — Link without scanning — enter an 8-digit code on the phone instead.
- [Session management](guides/authentication/session-management.md) — Persist auth state so you don't re-scan the QR every restart.

### Core concepts

- [Socket config](guides/concepts/socket-config.md) — All `SocketConfig` options: auth, browser, logger, caching, retries, timeouts.
- [Events](guides/concepts/events.md) — Typed events for messages, connection state, groups, contacts, and more.
- [JIDs](guides/concepts/jids.md) — How WhatsApp identifies users, groups, and broadcasts — including PN/LID duality.
- [Data store](guides/concepts/data-store.md) — Persist chats, messages, and contacts. In-memory store or your own backend.

### Messaging

- [Send messages](guides/messaging/sending-messages.md) — Text, links, contacts, locations, reactions, polls, and pins via `sock.sendMessage`.
- [Media messages](guides/messaging/media-messages.md) — Send and download images, video, audio, documents, GIFs, and stickers.
- [Message actions](guides/messaging/message-actions.md) — Edit, delete, mark as read, and update typing or online presence.
- [Manage chats](guides/messaging/chat-management.md) — Archive, mute, mark read, pin, star, or delete chats and messages.

### Features

- [Groups](guides/features/groups.md) — Create groups, manage participants and invites, and toggle ephemeral messages.
- [Privacy](guides/features/privacy.md) — Block users, control last-seen, read receipts, and default disappearing mode.
- [Presence](guides/features/presence.md) — Track online, typing, and recording state — and broadcast your own.
- [Broadcasts & Stories](guides/features/broadcasts-stories.md) — Publish Status updates and send to broadcast lists.

### Advanced

- [History sync](guides/advanced/history-sync.md) — Receive prior chats and contacts, and pull more history on demand.
- [USync](guides/advanced/usync.md) — Query user metadata, LID/PN mappings, and device lists via USync and MEX.
- [Calls](guides/advanced/calls.md) — Listen for incoming calls and reject them.
- [Custom functionality](guides/advanced/custom-functionality.md) — Register raw WebSocket callbacks, enable debug logs, and read binary nodes.
- [Troubleshooting](guides/advanced/troubleshooting.md) — Connection drops, QR failures, delivery problems, session expiry, media errors.

### Migration

- [v7 migration](guides/migration/v7.md) — Breaking changes in 7.x: LIDs, removed ACKs, ESM-only, slimmer protobufs.

## Reference

- [API index](api/README.md) — 417 exported symbols (functions, types, interfaces, classes, enums, variables).
- [Protobuf index](proto/README.md) — 672 `proto.*` interfaces and enums.
