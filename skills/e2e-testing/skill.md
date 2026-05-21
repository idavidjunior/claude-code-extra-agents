# E2E Testing — Playwright e Page Object Model

## Estrutura de Teste E2E
- Page Object Model: cada página é uma classe
- Testes independentes: cada teste cria seu próprio estado
- Dados de teste isolados por execução
- Timeout generoso: 30s por operação, 5min por teste

## Playwright Boilerplate
- use locators, nunca seletores CSS diretos
- page.waitForSelector substituído por locator.waitFor()
- trace on failure para debugging
- screenshots automáticos em falha

## Regras de Ouro
- Teste fluxo crítico: login, checkout, pagamento
- Não teste aparência visual (cor, posição)
- Mock API externa (pagamento, email)
- Banco de dados limpo antes de cada suíte
- Rode em CI com navegador headless

## Anti-Patterns
- Teste dependente de ordem
- Sleep fixo em vez de waitFor
- Testar layout visual em vez de comportamento
- Mockar API interna (perde o propósito do E2E)
- Não limpar estado entre testes