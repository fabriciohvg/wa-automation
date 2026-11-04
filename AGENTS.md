Este é um projeto de automação do WhatsApp para uso pessoal em TypeScript com o uso da biblioteca Baileys. A versão da biblioteca Baileys que deverá ser utilizada é 7.0.0-rc14.

A pasta @docs-7.0.0-rc14 contém a documentação oficial da biblioteca Baileys (apis, guides e proto). Sempre que necessário recorra a ela e aos arquivos do respectivo package instalado na pasta do Node.js.

## Motivação

O WhatsApp se tornou uma ferramenta essencial no dia a dia, mas também uma grande fonte de distração e sobrecarga. Além disso, é um gargalo quanto ao uso excessivo de espaço de armazenamento no celular. Para tornar o uso mais produtivo e até mesmo para garantir um backup automático e otimizado para meu uso, desenvolvi este projeto.

## Objetivos

Este projeto deve atingir os seguintes objetivos:

1. Conectar a minha conta pessoal do WhatsApp através do QR Code
2. Sincronizar todas as conversas, mídias, arquivos, informações dos contatos (foto de perfil, etc.) com um banco de dados SQL
3. Sincronizar todos os eventos do WhatsApp com o banco de dados SQL (mensagens recebidas, enviadas, mídias, arquivos, etc.)

## Características e funcionalidades desejadas

### Banco de dados

- Implementar um banco de dados SQLite utilizando a biblioteca better-sqlite3
- Garantir que o banco de dados é otimizado para armazenar e retornar as informações da aplicação

### Sincronização

- Baileys deve conectar usando macOS desktop browser preset
- Por padrão, usar on-demand history sync para além do sync inicial

### Contatos

- Obter e sincronizar/armazenar no banco de dados o máximo de informações possíveis dos contatos (nome, número de telefone no padrão do WhatsApp, foto de perfil, etc.)

> Em relação ao nome dos contatos, é importante distinguir se o nome que está armazenado/exibido é o nome interno do usuário no WhatsApp (que ele definiu) ou se é o nome do contato que eu adicionei na conta. Por exemplo, pode ser que eu tenha salvado na minha conta o nome de um contato como "Fulano de Tal", mas esse usuário use o nome na conta dele do WhatsApp como "Dr. Fulano T. Silva". É importante que seja possível diferenciar essa informação. Se for possível, para os contatos salvos na minha conta, além de armazenar que o nome que eu uso, armazenar o nome que o usuário definiu na conta dele do WhatsApp.

### Conversas e mensagens

- Armazenar e sincronizar todas as mensagens das conversas (mensagens enviadas, recebidas, reações, mídias, arquivos)
- Sincronizar mensagens enviadas e recebidas (todas, incluindo reações, mídias, arquivos, etc.) após se reconectar
- Garantir que a sincronização de mensagens não produz duplicadas
- Armazenar as mensagens de `messages.upsert` dos tipos `notify` e `append`, usando `type` apenas para decidir sobre notificações. Não copiar dos guias o filtro `if (type !== 'notify') return`
- Armazenar o `WAMessage` completo, e não apenas `msg.message` como no exemplo de `guides/concepts/data-store.md`

## Padrões de código

- Otimizar o código para performance, mantendo-o adequado para um ambiente de aprendizagem
- Escrever o código em inglês (identificadores, strings, logs, schema do banco)
- Escrever os comentários em português do Brasil, seguindo o estilo definido em @WRITING.md

## Commits

- Seguir as boas práticas da indústria: Conventional Commits, em inglês, com assunto curto no imperativo e um commit por mudança lógica. O estilo das mensagens segue @WRITING.md
- Antes de qualquer commit, checar se há algo sensível entre os arquivos (credenciais e estado de autenticação da Baileys, banco de dados SQLite, mídias, `.env`) e atualizar o `.gitignore`

## Implementação/investigação futura

Os itens abaixo estão fora do escopo atual. Só devem ser implementados ou investigados quando eu pedir.

### Requisitos adiados

Os guias da Baileys não explicam como receber estes eventos. A investigação deve partir de `docs-7.0.0-rc14/proto/` e do código do pacote instalado.

- Mensagens de visualização única devem ser armazenadas e o conteúdo deve ser armazenado no banco de dados para ser visualizado outras vezes mesmo após a primeira visualização
- Mensagens editadas devem ser armazenadas, tanto a mensagem original quanto a mensagem editada final
- Mensagens deletadas devem ser armazenadas, podendo ser visualizadas posteriormente

### Deduplicação entre PN e LID

A chave `(remoteJid, id)` usada nos guias talvez não baste para evitar duplicatas se a mesma mensagem chegar ora com PN, ora com LID. É uma hipótese ainda não testada.

### Exemplos dos guias que conflitam com os requisitos

- `INSERT OR REPLACE` (`guides/concepts/data-store.md`): sobrescreve o conteúdo existente, o que perderia o original de mensagens editadas ou deletadas
