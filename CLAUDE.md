# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Objetivos, requisitos, padrões de código e commits: @AGENTS.md

Estilo de escrita: @WRITING.md

Tarefas do MVP: @TASKS.md

## Regras para o Claude Code

- Executar as tarefas do `TASKS.md` na sequência indicada, uma de cada vez. Ao terminar, marcar `[~]` e parar. Só marcar `[x]` e começar a próxima depois da aprovação do autor do projeto na revisão.

- Não incluir o Claude Code como coautor nos commits: sem `Co-Authored-By` nem outra linha de atribuição. Esta regra prevalece sobre o padrão da ferramenta.
- Não implementar nem investigar itens da seção "Implementação/investigação futura" do `AGENTS.md` sem pedido explícito.
- Durante o desenvolvimento, registrar em `dev-notes/`, em Markdown, os gotchas, trade-offs e pontos distorcidos ou obscuros da documentação que forem identificados. Use um arquivo por assunto. Registre só o que for relevante e tiver sido verificado: nada de registros forçados, extrapolados ou falsos. Hipóteses devem ser marcadas como tal.

## Comandos

```sh
npm run dev        # executa src/index.ts com tsx
npm run build      # compila para dist/, sem os testes
npm start          # executa dist/index.js
npm run typecheck  # checa os tipos, incluindo os testes
npm run lint       # executa o Biome em src/
npm test           # executa todos os testes (node:test)
node --import tsx --test src/db/database.test.ts  # executa um único teste
```

O linter é o Biome, com o formatador desligado; ESLint com `typescript-eslint` não instala com o TypeScript 7. A regra `noFloatingPromises` é experimental e pode mudar entre versões do Biome. O `dev` não usa modo watch de propósito: reiniciar a cada alteração derrubaria a conexão com o WhatsApp.

## Estado atual

O scaffold abre o banco e encerra. Ainda não há schema, conexão com o WhatsApp nem sincronização. O andamento fica em `TASKS.md`.

O repositório é público, então nada sensível pode ser versionado. Banco de dados e autenticação ficam em `data/`, que está no `.gitignore`.

## Stack

- Mantenha a versão exata `7.0.0-rc14` da Baileys, sem `^`, pois é um release candidate. O projeto usa o pacote `baileys`; os guias importam de `@whiskeysockets/baileys`, então ajuste os imports ao copiar exemplos.
- O projeto é ESM (`"type": "module"`), como exige a Baileys, e os imports internos usam a extensão `.js`.
- O projeto exige Node.js >= 22 por causa do `better-sqlite3`; a Baileys aceita >= 20.
- O `pino` fica na major 9, a mesma da Baileys, para não instalar duas cópias.
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
- Use `browser: Browsers.macOS('Desktop')` e mantenha `syncFullHistory` ativo. Os dois são necessários para receber o histórico estendido no sync inicial, mas não bastam: o padrão de `shouldSyncHistoryMessage` recusa o tipo `FULL` (ver `dev-notes/history-sync-defaults.md`).
- O histórico chega de forma assíncrona em `messaging-history.set`, em lotes que podem ter milhares de mensagens. Grave-os em transações em lote.
- `sock.fetchMessageHistory` entrega os resultados nesse mesmo evento.
- O QR Code vem no campo `qr` de `connection.update` e precisa ser renderizado pela aplicação.

**Identidade (JIDs)**
- Um mesmo usuário tem um PN (`@s.whatsapp.net`) e um LID (`@lid`), e os guias tratam o LID como identificador canônico. Modele o banco para os dois, usando `remoteJidAlt`/`participantAlt`, `lid-mapping.update` e `sock.signalRepository.lidMapping`.
- Nem todo LID pode ser convertido em PN: `getPNForLID` só funciona se o mapeamento já tiver sido visto.
- Não compare JIDs com `===` nem os separe com `split('@')`, pois podem ter sufixo de dispositivo (`:2`). Use `jidDecode`, `jidNormalizedUser` e `areJidsSameUser`; este último não compara PN com LID.

**Contatos**
- `Contact.name` é o nome salvo na sua conta e `Contact.notify` é o nome que o usuário definiu no WhatsApp. Armazene-os em colunas separadas; é a distinção pedida no `AGENTS.md`. No histórico, `name` pode ter outra origem (ver `dev-notes/history-sync-defaults.md`).
- `Contact.imgUrl` não é só uma URL: `'changed'` indica que a foto mudou e precisa ser buscada de novo com `sock.profilePictureUrl`, e `null` indica que não há foto.

**Mídia**
- Baixe com `downloadMediaMessage`, de preferência no modo `'stream'`, passando `reuploadRequest: sock.updateMediaMessage` para recuperar mídia que expirou nos servidores do WhatsApp.
