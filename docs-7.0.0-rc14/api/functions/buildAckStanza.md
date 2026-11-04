# buildAckStanza

> Baileys **v7** reference — package version `7.0.0-rc14` (npm `latest`). Not valid for v6 or v8.

Function · source `src/Utils/stanza-ack.ts:11`

```ts
function buildAckStanza(node: BinaryNode, errorCode?: number, meId?: string): BinaryNode
```

Builds an ACK stanza for a received node.
Pure function -- no I/O, no side effects.

Mirrors WhatsApp Web's ACK construction:
- WAWebHandleMsgSendAck.sendAck / sendNack
- WAWebCreateNackFromStanza.createNackFromStanza
