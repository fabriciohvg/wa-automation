# Semântica dos eventos de mensagem

Observado no código da Baileys `7.0.0-rc14`, em `node_modules/baileys/lib`. Em alguns pontos, difere de `guides/concepts/events.md`.

## `append` não é só histórico

O guia define `append` como mensagens de histórico ou backfill. No código, também é o tipo de:

- mensagens entregues depois de um período offline (`Socket/messages-recv.js:1432`);
- mensagens enviadas pelo próprio socket (`Socket/messages-send.js:1137`).

Quem filtra por `notify` perde essas mensagens.

## `messages.update` pode apagar conteúdo

Uma exclusão emite `update: { message: null, ... }` (`Utils/process-message.js:299`). Uma edição emite `update.message.editedMessage` (`Utils/process-message.js:365`). Mesclar `update` na mensagem gravada, como faz o exemplo de `guides/concepts/data-store.md`, perde o conteúdo original.

## Reações têm evento próprio

O guia lista reações em `messages.update`, mas uma mensagem de reação emite `messages.reaction` (`Utils/process-message.js:416`). Se `reaction.text` vier vazio, a reação foi removida (`Types/Events.d.ts`).
