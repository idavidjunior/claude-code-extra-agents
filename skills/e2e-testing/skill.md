---
name: e2e-testing
description: |
  Testes E2E com Playwright e Page Object Model.
  Trigger phrases: "E2E", "end to end", "Playwright", "page object", "teste de interface"
allowed-tools: Read, Grep, Bash
version: 1.0.0
---

# E2E Testing — Playwright e Page Object Model

## Estrutura de Teste E2E
- Page Object Model: cada pagina e uma classe
- Testes independentes: cada teste cria seu proprio estado
- Dados de teste isolados por execucao
- Timeout generoso: 30s por operacao, 5min por teste

## Playwright Boilerplate
- Use locators, nunca seletores CSS diretos
- page.waitForSelector substituido por locator.waitFor()
- Trace on failure para debugging
- Screenshots automaticos em falha

## Regras de Ouro
- Teste fluxo critico: login, checkout, pagamento
- Nao teste aparencia visual (cor, posicao)
- Mock API externa (pagamento, email)
- Banco de dados limpo antes de cada suite
- Rode em CI com navegador headless

## Anti-Patterns
- Teste dependente de ordem
- Sleep fixo em vez de waitFor
- Testar layout visual em vez de comportamento
- Mockar API interna (perde o proposito do E2E)
- Nao limpar estado entre testes
