# Padrões do sync de histórico

Observado no código da Baileys `7.0.0-rc14`, em `node_modules/baileys/lib`.

## O histórico FULL é recusado por padrão

O padrão de `shouldSyncHistoryMessage` é `syncType !== FULL` (`Defaults/index.js:65`). O `syncFullHistory: true`, por sua vez, só pede o histórico ao celular (`Utils/validate-connection.js`).

Isso contradiz a documentação:

- `api/types/SocketConfig.md` diz "by default will sync up everything".
- Os guias só citam essa opção para desligar o histórico.

Para aceitar o tipo `FULL`, use `shouldSyncHistoryMessage: () => true`. O efeito em uma conta real ainda não foi verificado; isso será feito na T8 do `TASKS.md`.

## O sync inicial não se repete na reconexão

Quando `creds.accountSyncCounter > 0`, a Baileys não espera o histórico, porque o servidor não o reenvia (`Socket/chats.js:1086`). Quem perde o sync inicial precisa refazer o vínculo.

## `Contact.name` não é sempre o nome salvo

No histórico, `name` vem de `displayName || name || username` (`Utils/history.js`). O `Contact.md` o descreve como o nome salvo na conta, mas esse valor pode ter outra origem.
