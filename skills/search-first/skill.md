---
name: search-first
description: |
  Pesquisar antes de codar: documentação, GitHub, StackOverflow.
  Trigger phrases: "search first", "research before code", "look up", "find solution"
allowed-tools: Read, Grep, Bash, WebSearch, WebFetch
version: 1.0.0
---

# Search First — Pesquisar Antes de Codar

## O Princípio
Antes de escrever qualquer código, pesquise:
1. Isso já existe pronto? (biblioteca, SaaS, open source)
2. Alguém já resolveu esse problema? (StackOverflow, GitHub, docs)
3. Qual a forma idiomática na linguagem/framework?

## Ferramentas de Pesquisa
- Documentação oficial: sempre a fonte primária
- GitHub: issues, discussions, código fonte
- StackOverflow: respostas com mais de 50 votos
- Blogs de engenharia: Netflix, Uber, Stripe, Shopify

## Regras de Ouro
- Primeira hora é de pesquisa, não de código
- Solução existente é melhor que código novo
- Código não escrito é o melhor código (sem bugs)
- Documente o que pesquisou para o próximo dev
- Se não encontrou nada, documente a decisão (ADR)

## Anti-Patterns
- Começar a codar sem pesquisar
- Reinventar biblioteca que já existe
- Usar primeira solução do StackOverflow sem entender
- Ignorar documentação oficial
