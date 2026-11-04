# Tarefas do MVP

O MVP é um backup somente leitura: conecta a conta, grava o que chega no SQLite e não envia mensagens. Os itens de "Implementação/investigação futura" do `AGENTS.md` estão fora dele.

## Como usar

Execute as tarefas na ordem, uma de cada vez.

- `[ ]` pendente
- `[~]` em revisão: implementada e aguardando a revisão do autor do projeto
- `[x]` concluída: só depois que o autor aprovar na revisão

Ao terminar uma tarefa, marque `[~]` e pare. A próxima só começa depois da aprovação.

## Por que esta sequência

O servidor só envia o sync inicial uma vez por vínculo (`Socket/chats.js:1086`). Por isso, a persistência precisa estar pronta antes do vínculo definitivo, na T8. A T1 valida a conexão com o histórico desligado, e a T8 refaz o vínculo com tudo pronto. Mídia e fotos ficam depois do sync porque podem ser buscadas a partir do que já está no banco.

## Decisões do MVP

- **Identificador das mensagens:** `(remote_jid, id)`, como nos guias. A deduplicação entre PN e LID é trabalho futuro.
- **Gravação:** `INSERT ... ON CONFLICT DO NOTHING` em transações em lote. Nunca `INSERT OR REPLACE`.
- **Formato do `WAMessage`:** protobuf em BLOB, mais colunas extraídas para consulta (data, remetente, tipo, texto). A confirmar na T3 com mensagens reais: em um exemplo mínimo, o protobuf ocupou 41 bytes e o JSON, 141.
- **Mídia:** arquivos em `data/media/`, nomeados pelo SHA-256, com metadados e caminho no banco. Conteúdo idêntico ocupa espaço uma vez só.
- **Autenticação:** armazenamento próprio em SQLite, em `data/auth.db`, separado de `wa.db`, com `synchronous = FULL` e `makeCacheableSignalKeyStore` na frente. Uma transação grava todas as chaves ou nenhuma, e as chaves ficam fora do banco de mensagens.
- **Eventos sem tabela própria:** ficam em um log bruto (T7), o que preserva edições e exclusões para o trabalho futuro sem interpretá-las agora.
- **Histórico sob demanda:** só roda quando acionado por opção de linha de comando (T12), para não gerar um grande volume de pedidos sem escolha do autor.

## Tarefas

### [ ] T1. Conexão por QR Code

- Implementar o `AuthenticationState` em `data/auth.db`, usando `Utils/use-multi-file-auth-state.js` como referência: serializar com `BufferJSON`, restaurar `app-state-sync-key` com `proto.Message.AppStateSyncKeyData.fromObject` e tratar `null` em `set` como remoção.
- Gravar cada `set` em uma única transação, concluída antes de a promise resolver.
- Conectar com `socketOptions` e exibir o QR no terminal.
- Reconectar com espera crescente; reabrir em `restartRequired`, que é esperado após o scan; parar em `loggedOut`.
- Usar `markOnlineOnConnect: false`, para não suprimir as notificações do celular.
- Usar a versão padrão do WhatsApp Web da Baileys, sem `fetchLatestBaileysVersion`, como recomenda o FAQ.
- Manter o histórico desligado nesta etapa (`shouldSyncHistoryMessage: () => false`).

**Revisão:** testes de ida e volta do armazenamento (`Buffer`, `app-state-sync-key` e remoção); escanear o QR, reiniciar sem novo QR, derrubar a rede e ver a reconexão.

### [ ] T2. Schema e migrações

- Criar migrações versionadas com `PRAGMA user_version`.
- Criar as tabelas `messages`, `chats`, `contacts`, `lid_mappings`, `groups`, `group_participants`, `reactions`, `receipts`, `media` e `event_log`, com índices para as consultas por conversa e data.
- Em `contacts`, separar o nome salvo por mim (`name`) do nome definido pelo usuário (`notify`).

**Revisão:** ler o schema; testes de migração a partir de um banco vazio e de um já migrado.

### [ ] T3. Gravação de mensagens

- Serializar o `WAMessage` completo e extrair as colunas de consulta.
- Gravar em lote, em uma transação, com deduplicação.
- Implementar a leitura usada pelo `getMessage`.

**Revisão:** testes de ida e volta da serialização, de duplicatas e de um lote grande, com o tempo medido.

### [ ] T4. Mensagens em tempo real

- Processar eventos com `ev.process` e gravar `messages.upsert` dos tipos `notify` e `append`.
- Conectar o `getMessage` ao banco.

**Revisão:** enviar e receber texto, foto e arquivo pelo celular e conferir no banco, sem duplicatas.

### [ ] T5. Reações e status

- Gravar `messages.reaction` e o campo `reactions` do `WAMessage`, removendo a reação quando `reaction.text` vier vazio.
- Gravar `message-receipt.update`.
- Em `messages.update`, aplicar somente `status`. Não mesclar `message`, porque uma exclusão o define como `null` e apagaria o conteúdo.

**Revisão:** reagir, trocar e remover uma reação; conferir no banco; apagar uma mensagem e confirmar que o conteúdo continua lá.

### [ ] T6. Contatos, conversas e grupos

- Gravar `contacts.upsert`, `contacts.update`, `chats.upsert`, `chats.update` e `lid-mapping.update`.
- Em `chats.delete`, marcar a conversa como apagada, sem remover os dados.
- Buscar grupos com `groupFetchAllParticipating` e acompanhar `groups.*` e `group-participants.update`.
- Tratar a origem dos nomes: no histórico, `Contact.name` pode vir de `displayName`, `name` ou `username` (`Utils/history.js`).

**Revisão:** comparar com o celular um contato salvo com nome diferente do definido por ele, um contato não salvo e um grupo.

### [ ] T7. Log bruto de eventos

- Gravar em `event_log` os eventos sem tabela própria (por exemplo `messages.delete`, `messages.update` e `call`).
- Excluir `creds.update`, `connection.update` e `messaging-history.set`: o primeiro contém credenciais e o último é grande e já fica nas tabelas.
- Medir o crescimento do log.

**Revisão:** editar e apagar uma mensagem e ver os eventos no log; conferir que não há credenciais nele.

### [ ] T8. Sync inicial e vínculo definitivo

- Definir `shouldSyncHistoryMessage: () => true`. O padrão da Baileys recusa o tipo `FULL`.
- Gravar `messaging-history.set` em lotes, incluindo `lidPnMappings`, e registrar o progresso com `messaging-history.status`.
- Remover o vínculo da T1 no celular, apagar `data/auth.db` e escanear de novo.

**Revisão:** acompanhar o sync; comparar conversas e mensagens antigas com o celular; medir duração, memória e tamanho do banco.

### [ ] T9. Reconexão

- Validar que o que chega durante uma desconexão é gravado sem lacunas e sem duplicatas. Essas mensagens chegam como `append` (`Socket/messages-recv.js:1432`).
- Corrigir o que o teste revelar.

**Revisão:** parar a aplicação, trocar mensagens e reações pelo celular, religar e conferir no banco.

### [ ] T10. Download de mídia

- Criar uma fila persistida no banco, com concorrência limitada, que continua depois de reiniciar e não bloqueia o processamento de eventos.
- Baixar em modo `'stream'` com `reuploadRequest: sock.updateMediaMessage` e gravar por SHA-256.
- Registrar falhas e limitar as tentativas: mídia antiga pode não estar mais disponível.

**Revisão:** abrir arquivos de cada tipo; reiniciar no meio da fila; conferir a contagem de pendentes e de falhas e o espaço ocupado.

### [ ] T11. Fotos de perfil

- Baixar as fotos de contatos e grupos para `data/`, com limite de requisições.
- Tratar `imgUrl`: `'changed'` pede nova busca e `null` indica que não há foto.
- Tratar a falta de permissão por privacidade sem repetir a tentativa indefinidamente.

**Revisão:** comparar algumas fotos com o celular; trocar a foto de um contato de teste, se possível.

### [ ] T12. Histórico sob demanda

- Implementar `sock.fetchMessageHistory` a partir da mensagem mais antiga de cada conversa, acionado por opção de linha de comando (por exemplo `--backfill`).
- Fazer um pedido por vez, com intervalo configurável, e guardar o progresso por conversa.
- Parar a conversa quando não vier mensagem nova.

**Revisão:** rodar em uma conversa com mensagens mais antigas que as do sync inicial e conferir o resultado, com o celular online.

### [ ] T13. Validação final e documentação

- Rodar a aplicação por um período com uso normal e conferir duplicatas, lacunas, fila de mídia e crescimento do banco.
- Escrever o `README.md`: instalação, uso, onde os dados ficam e riscos.

**Revisão:** seguir o `README.md` do zero, com um banco vazio.

## Fora do MVP

- Itens de "Implementação/investigação futura" do `AGENTS.md`
- Interface para consultar os dados
- Envio de mensagens e automações
- Presença e cálculo de votos em enquetes (os eventos brutos ficam no log)
