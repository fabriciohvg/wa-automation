# Introduction

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

What Baileys is, what you can build with it, and what the runtime needs.

Baileys is a WebSocket-based TypeScript library that lets you interact with the WhatsApp Web API directly — no browser, no Selenium, no Chromium required. It speaks the same binary Noise/protobuf protocol as WhatsApp Web, so you can authenticate, send and receive messages, manage groups, and react to real-time events from a lightweight Node.js process.

## Key capabilities

- **Send and receive messages** — text, images, video, audio, documents, stickers, polls, reactions, locations, and contacts
- **Media handling** — stream uploads and downloads without loading entire files into memory; automatic thumbnail generation with optional dependencies
- **Groups** — create groups, manage participants, update metadata, handle join requests, and configure ephemeral messages
- **Privacy controls** — read and update last-seen, profile picture, status, read receipts, and groups-add privacy
- **Presence** — subscribe to and broadcast typing indicators and online status
- **Real-time events** — typed EventEmitter interface covering messages, connection state, contacts, chats, and group changes
- **Session persistence** — save and restore authentication state so you only scan the QR code once
- **TypeScript-first** — all public types are exported; full IntelliSense support in VS Code and compatible editors

## Requirements

- **Node.js >=20.0.0** — enforced at install time via the `engines` field in `package.json`
- **TypeScript** is supported out of the box; the package ships with `.d.ts` declaration files
