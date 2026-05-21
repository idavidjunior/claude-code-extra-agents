# Database Migrations — Migração sem Downtime

## Estratégia Expand-Contract
1. Expand: adicione nova coluna/tabela (sem remover nada)
2. Migrate: código escreve nos dois formatos durante transição
3. Contract: remova coluna/tabela antiga após migração completa

## Regras de Ouro
- Migração é sempre forward-only (não reverta migração em produção)
- Toda migração tem backup antes de executar
- Colunas novas são nullable ou têm default
- Nunca renomeie coluna (adicione nova, migre dados, remova antiga)
- Índices são criados CONCURRENTLY (PostgreSQL)
- Migração pesada é executada em janela de baixa

## Tipos de Migração Segura
| Operação | Seguro? | Alternativa |
|----------|---------|-------------|
| ADD COLUMN nullable | Sim | - |
| ADD COLUMN com default | Sim (PostgreSQL 11+) | - |
| DROP COLUMN | Não | Expand-Contract |
| RENAME COLUMN | Não | Add new + drop old |
| ADD INDEX | Sim (CONCURRENTLY) | - |
| CHANGE TYPE | Não | Nova coluna + migração |

## Ferramentas
- Prisma: npx prisma migrate deploy
- Django: python manage.py migrate
- Flyway: Java, SQL puro
- golang-migrate: Go, arquivos SQL numerados
- Alembic: Python/SQLAlchemy

## Anti-Patterns
- Migração que altera tipo de coluna com dados
- Migração sem transação (parcialmente aplicada)
- Executar migração no mesmo deploy do código
- Rollback de migração em produção (perda de dados)