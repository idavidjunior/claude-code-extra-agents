---
name: state-machine-patterns
description: |
  Modelagem com XState e statecharts. Estados finitos, guards, actions, transições paralelas, visualização.
  Trigger phrases: "state machine", "XState", "statechart", "estado finito"
allowed-tools: Read, Grep, Bash
version: 1.0.0
---

# State Machine Patterns — Modelagem com XState e Statecharts

## Conceitos
- Estados finitos: cada estado é explícito e limitado
- Guards: condições para transição entre estados
- Actions: efeitos colaterais ao entrar/sair/transicionar
- Transições paralelas: estados simultâneos independentes

## Quando usar
- Fluxo de autenticação (login, 2FA, logado, expirado)
- Carrinho de compras (vazio, adicionando, checkout, pago)
- Upload de arquivo (selecionando, enviando, processando, concluído, erro)
- Wizard multi-etapas com navegação condicional

## Ferramentas
- XState (JavaScript/TypeScript)
- Robot (leve, funcional)
- Statecharts.io (visualização)

## Anti-Patterns
- Booleanos múltiplos em vez de estados (isLoading, isError, isSuccess)
- Transição impossível não tratada
- Estado sem saída (dead end)
