# TDD Workflow — Test-Driven Development

## O Ciclo Red-Green-Refactor

### Red — Escreva um teste que falha
- Teste deve falhar pela razão certa (funcionalidade não implementada)
- Nome do teste descreve o comportamento: should_return_error_when_email_is_invalid
- Um teste por comportamento, não um teste por método

### Green — Faça o teste passar
- Escreva o código mais simples possível
- Não implemente nada além do necessário para o teste passar
- Se a implementação mais simples é hardcoded, hardcode e depois generalize

### Refactor — Melhore o código
- Elimine duplicação
- Melhore nomes
- Extraia métodos e classes
- Garanta que os testes continuam passando

## Tipos de Teste

| Tipo | Escopo | Quantidade | Exemplo |
|------|--------|------------|---------|
| Unitário | 1 função/classe | 80% dos testes | should_calculate_total_with_discount |
| Integração | 2+ componentes reais | 15% dos testes | should_persist_order_to_database |
| E2E | Fluxo completo | 5% dos testes | should_complete_checkout_from_cart_to_payment |

## Regras de Ouro
- Sempre veja o teste falhar antes de implementar
- Nunca escreva código novo sem teste falhando
- Cobertura mínima: 80%
- Teste rápido (menos de 100ms unitário, menos de 5s integração)
- Teste independente (sem depender de ordem de execução)
- Mock apenas o que é lento ou externo (banco, API, email)

## Anti-Patterns
- Teste que nunca falhou (não testa nada real)
- Teste que testa implementação em vez de comportamento
- Mock excessivo (tudo mockado = nada testado)
- Teste lento (desestimula rodar)
- Teste interdependente (falha em cascata)

## Referências
- "Test-Driven Development: By Example" — Kent Beck
- "Growing Object-Oriented Software, Guided by Tests" — Freeman & Pryce