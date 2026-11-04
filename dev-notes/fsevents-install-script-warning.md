# Aviso de install script do fsevents

`npm install` avisava sobre `fsevents@2.3.3 (install: (install scripts present))`, mas o pacote instalado não tem script de instalação. É um falso positivo. Observado com npm 11.19.1.

## Causa

Os metadados e o pacote divergem:

| Fonte | Conteúdo |
|---|---|
| Registro do npm | `install: node-gyp rebuild`, `gypfile: true`, `hasInstallScript: true` |
| `package-lock.json` | `hasInstallScript: true` |
| Tarball instalado | Sem script `install` e sem `binding.gyp`; traz `fsevents.node` pronto |

Em `@npmcli/arborist/lib/install-scripts.js`, o npm não encontra script no pacote nem no disco. Como o lockfile diz `hasInstallScript: true`, ele usa o texto fixo `(install scripts present)`, e o alerta é emitido.

Hipótese não confirmada para a divergência: o npm viu o `binding.gyp` na pasta do autor ao publicar e adicionou o script aos metadados, mas o campo `files` deixou esse arquivo fora do tarball.

## Decisão

Rodamos `npm install-scripts deny fsevents`, que grava `"fsevents": false` em `allowScripts`. O aviso sumiu e `fsevents.node` continua no lugar.

A entrada não tem versão, então também bloqueia qualquer script real de uma versão futura. Se o `fsevents` deixar de funcionar depois de uma atualização, comece por essa entrada. Hoje ele só entra no projeto como dependência opcional do `tsx`.
