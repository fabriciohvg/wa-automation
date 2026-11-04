# Estilo de escrita

Vale para todo texto escrito neste projeto: comentários de código, commits, documentação e notas de desenvolvimento.

Escreva de forma concisa e clara, sem AI slop.

## Como escrever

- Vá direto ao ponto. Se uma frase pode sair sem perder informação, tire.
- Use palavras simples e frases curtas.
- Seja específico: cite o arquivo, o valor, o erro ou a consequência.
- Afirme só o que foi verificado. Se for hipótese, diga que é hipótese.
- Em comentários, explique o porquê. Não repita o que o código já diz.

## O que é AI slop

- Aberturas e fechamentos vazios: "É importante notar que", "Em resumo", "Vale ressaltar".
- Adjetivos promocionais: "robusto", "poderoso", "elegante", "perfeito".
- Ênfase exagerada: negrito em excesso, emojis, pontos de exclamação.
- Frases genéricas, que serviriam para qualquer projeto.
- Contrastes artificiais: "não é apenas X, é Y".
- Títulos e listas onde uma frase resolve.

## Exemplo

```ts
// Ruim: repete o código
// Define o modo synchronous como NORMAL
db.pragma('synchronous = NORMAL')

// Bom: explica o motivo
// Com WAL, NORMAL não corrompe o banco em caso de queda e evita um fsync por transação.
db.pragma('synchronous = NORMAL')
```
