# Deployment Patterns — CI/CD, Docker, Health Checks

## Pipeline CI/CD mínimo

1. Build — compila, checa tipos, lint
2. Test — unitários, integração, cobertura
3. Security Scan — SAST, SCA, secrets
4. Package — container ou artefato
5. Deploy — staging primeiro, produção depois
6. Verify — health check, smoke test

## Health Check obrigatório
- Endpoint /health: retorna 200 se serviço OK
- Verifica dependências: banco, cache, fila
- Timeout de 5 segundos (não pode travar)
- Kubernetes: livenessProbe e readinessProbe

## Estratégias de Deploy
| Estratégia | Risco | Rollback |
|-----------|-------|----------|
| Rolling Update | Baixo | Automático (K8s) |
| Blue-Green | Médio | Instantâneo (troca tráfego) |
| Canary | Baixo | Automático (tráfego progressivo) |
| Recreate | Alto | Lento (downtime) |

## Regras de Ouro
- Staging espelha produção (dados anonimizados)
- Migração de banco é separada do deploy do código
- Feature flags desacoplam deploy de release
- Rollback não reverte banco (schema forward-only)
- Secrets nunca no código ou imagem Docker
- Logs centralizados desde o primeiro deploy

## Anti-Patterns
- Deploy sexta-feira às 18h
- Sem health check
- Sem plano de rollback documentado
- Migração de banco sem backup
- Configuração diferente entre staging e produção