# Quickstart

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Connect, persist a session, and send your first message in a few minutes.

This guide walks you through creating a minimal Baileys application that connects to WhatsApp, persists your session, listens for incoming messages, and replies to them. By the end you will have a working bot you can extend with your own logic.

## Complete example

The steps below build up to this complete working script. You can use it as a starting point for your own project.

```typescript
import makeWASocket, { DisconnectReason, useMultiFileAuthState } from '@whiskeysockets/baileys'
import { Boom } from '@hapi/boom'
import qrcode from 'qrcode-terminal'

async function connectToWhatsApp() {
    const { state, saveCreds } = await useMultiFileAuthState('auth_info_baileys')

    const sock = makeWASocket({
        auth: state
    })

    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect, qr } = update
        if (qr) {
            qrcode.generate(qr, { small: true })
        }
        if (connection === 'close') {
            const shouldReconnect =
                (lastDisconnect?.error as Boom)?.output?.statusCode !== DisconnectReason.loggedOut
            console.log('connection closed due to', lastDisconnect?.error, ', reconnecting:', shouldReconnect)
            if (shouldReconnect) {
                connectToWhatsApp()
            }
        } else if (connection === 'open') {
            console.log('opened connection')
        }
    })

    sock.ev.on('messages.upsert', async (event) => {
        if (event.type !== 'notify') return
        for (const m of event.messages) {
            if (m.key.fromMe) continue
            console.log(JSON.stringify(m, undefined, 2))

            console.log('replying to', m.key.remoteJid)
            await sock.sendMessage(m.key.remoteJid!, { text: 'Hello from Baileys!' })
        }
    })

    // Save credentials whenever they are updated
    sock.ev.on('creds.update', saveCreds)
}

connectToWhatsApp()
```

## Step-by-step walkthrough

**Step 1: Install Baileys**

Add Baileys and its `@hapi/boom` peer to your project. `@hapi/boom` is a direct dependency of Baileys and is used to inspect disconnect error codes.

```bash npm
npm install @whiskeysockets/baileys @hapi/boom
```

```bash yarn
yarn add @whiskeysockets/baileys @hapi/boom
```

Make sure you are running **Node.js 20.0.0 or later**. Installation will fail otherwise.

**Step 2: Set up auth state**

Baileys requires an auth state object to manage your session credentials and Signal Protocol keys. The built-in `useMultiFileAuthState` utility saves everything to a local folder.

```typescript
import makeWASocket, { useMultiFileAuthState } from '@whiskeysockets/baileys'

const { state, saveCreds } = await useMultiFileAuthState('auth_info_baileys')
```

`state` holds the current credentials and keys. `saveCreds` is a callback you will pass to the `creds.update` event so the session is written to disk whenever it changes.

> **Tip:** The folder name (`auth_info_baileys` in this example) can be any path you choose. Store it outside your source tree and add it to `.gitignore` — it contains long-lived cryptographic keys for your WhatsApp account.

**Step 3: Create the socket**

Create a socket by calling `makeWASocket` with your auth state. Listen for the `qr` field on `connection.update` and render it yourself — `printQRInTerminal` is deprecated.

```typescript
import qrcode from 'qrcode-terminal'

const sock = makeWASocket({
    auth: state
})

sock.ev.on('connection.update', ({ qr }) => {
    if (qr) qrcode.generate(qr, { small: true })
})
```

> **Note:** When you run this for the first time, a QR code appears in your terminal. Open WhatsApp on your phone, go to **Settings → Linked devices → Link a device**, and scan the code. On subsequent runs, the saved credentials are reused and no QR code is shown.

**Step 4: Handle connection updates**

Listen to `connection.update` to react when the connection opens, closes, or encounters an error. The reconnect logic below restarts the socket automatically — unless you were explicitly logged out.

```typescript
import { DisconnectReason } from '@whiskeysockets/baileys'
import { Boom } from '@hapi/boom'

sock.ev.on('connection.update', (update) => {
    const { connection, lastDisconnect } = update
    if (connection === 'close') {
        const shouldReconnect =
            (lastDisconnect?.error as Boom)?.output?.statusCode !== DisconnectReason.loggedOut
        console.log('connection closed due to', lastDisconnect?.error, ', reconnecting:', shouldReconnect)
        if (shouldReconnect) {
            connectToWhatsApp()
        }
    } else if (connection === 'open') {
        console.log('opened connection')
    }
})
```

`DisconnectReason.loggedOut` means your session was revoked (for example, you removed the linked device in the WhatsApp app). In that case, delete the auth folder and re-scan a QR code.

**Step 5: Listen for incoming messages**

The `messages.upsert` event fires whenever new messages arrive. Iterate over `event.messages` to handle each one.

```typescript
sock.ev.on('messages.upsert', async (event) => {
    if (event.type !== 'notify') return
    for (const m of event.messages) {
        if (m.key.fromMe) continue
        console.log(JSON.stringify(m, undefined, 2))

        console.log('replying to', m.key.remoteJid)
        await sock.sendMessage(m.key.remoteJid!, { text: 'Hello from Baileys!' })
    }
})
```

Filtering on `event.type === 'notify'` and `!m.key.fromMe` keeps the bot from replying to its own messages and from treating history backfills as fresh.

`m.key.remoteJid` is the WhatsApp ID (JID) of the chat the message came from — a phone number for individual chats, or a group ID for group chats. Pass it as the first argument to `sock.sendMessage` to reply.

**Step 6: Save credentials on update**

Register the `saveCreds` callback on the `creds.update` event. Baileys calls this whenever your session credentials change — for example, after the initial QR scan or after Signal session keys rotate.

```typescript
sock.ev.on('creds.update', saveCreds)
```

If you skip this step, your session will not be saved and you will need to scan the QR code again on every restart.
