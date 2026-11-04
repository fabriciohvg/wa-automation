# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Objetivos, requisitos, padrões de código e commits: @AGENTS.md

## Regras para o Claude Code

- Não incluir o Claude Code como coautor nos commits: sem `Co-Authored-By` nem outra linha de atribuição. Esta regra prevalece sobre o padrão da ferramenta.
- Não implementar nem investigar itens da seção "Implementação/investigação futura" do `AGENTS.md` sem pedido explícito.

## Estado atual

O projeto ainda não tem código: não há `package.json` nem scripts de build/teste. O repositório é público, então nada sensível pode ser versionado. Ao criar o scaffold, documente aqui os comandos reais (build, lint, testes, teste único).

## Stack

- Fixe a versão exata `7.0.0-rc14` da Baileys, sem `^`, pois é um release candidate. O pacote é publicado como `baileys` e `@whiskeysockets/baileys`; os guias importam do segundo.
- A Baileys é ESM-only e exige Node.js >= 20, então o projeto precisa de `"type": "module"`.
- A Baileys v7 removeu APIs da v6, como `makeInMemoryStore`, `printQRInTerminal` e `isJidUser`. Não use exemplos da v6; veja `docs-7.0.0-rc14/guides/migration/v7.md`.

## Consulta à documentação

Em `docs-7.0.0-rc14/`, comece pelo `README.md`, que é o índice:

- Tarefas: `guides/`
- Assinaturas: `api/README.md`, depois `api/<kind>/<Name>.md`
- Métodos do socket: `api/functions/makeWASocket.md`
- Formatos protobuf: `proto/README.md`

## Particularidades da Baileys que afetam o design

**Persistência**
- A Baileys não guarda estado: tudo que for mantido precisa ser construído a partir dos eventos.
- Implemente `getMessage` no `SocketConfig` com leitura do banco. Sem ele, os reenvios de mensagens e a descriptografia de votos em enquetes falham.
- Mantenha o estado de autenticação (chaves Signal) fora das tabelas de mensagens. Atualizações de `keys.set` precisam ser persistidas de imediato; um armazenamento próprio deve serializar com `BufferJSON`.

**Sincronização**
- Use `browser: Browsers.macOS('Desktop')` e mantenha `syncFullHistory` ativo. Os dois são necessários para receber o histórico estendido no sync inicial.
- O histórico chega de forma assíncrona em `messaging-history.set`, em lotes que podem ter milhares de mensagens. Grave-os em transações em lote.
- `sock.fetchMessageHistory` entrega os resultados nesse mesmo evento.
- O QR Code vem no campo `qr` de `connection.update` e precisa ser renderizado pela aplicação.

**Identidade (JIDs)**
- Um mesmo usuário tem um PN (`@s.whatsapp.net`) e um LID (`@lid`), e os guias tratam o LID como identificador canônico. Modele o banco para os dois, usando `remoteJidAlt`/`participantAlt`, `lid-mapping.update` e `sock.signalRepository.lidMapping`.
- Nem todo LID pode ser convertido em PN: `getPNForLID` só funciona se o mapeamento já tiver sido visto.
- Não compare JIDs com `===` nem os separe com `split('@')`, pois podem ter sufixo de dispositivo (`:2`). Use `jidDecode`, `jidNormalizedUser` e `areJidsSameUser`; este último não compara PN com LID.

**Contatos**
- `Contact.name` é o nome salvo na sua conta e `Contact.notify` é o nome que o usuário definiu no WhatsApp. Armazene-os em colunas separadas; é a distinção pedida no `AGENTS.md`.
- `Contact.imgUrl` não é só uma URL: `'changed'` indica que a foto mudou e precisa ser buscada de novo com `sock.profilePictureUrl`, e `null` indica que não há foto.

**Mídia**
- Baixe com `downloadMediaMessage`, de preferência no modo `'stream'`, passando `reuploadRequest: sock.updateMediaMessage` para recuperar mídia que expirou nos servidores do WhatsApp.
