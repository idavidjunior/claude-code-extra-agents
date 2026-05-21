---
name: autonomous-loops
description: |
  Loops autônomos: pipelines sequenciais, PR loops, DAG.
  Trigger phrases: "autonomous loop", "pipeline", "DAG", "PR loop", "automation"
allowed-tools: Read, Grep, Bash
version: 1.0.0
---

# Autonomous Loops — Pipelines Sequenciais, PR Loops, DAG

## Tipos de Loop Autônomo

### Pipeline Sequencial
- Etapas executadas em ordem fixa
- Cada etapa depende da anterior
- Exemplo: build -> test -> deploy
- Falha em qualquer etapa interrompe o pipeline

### PR Loop
- Monitora PRs abertos
- Executa verificações automáticas
- Adiciona comentários com feedback
- Reexecuta quando PR é atualizado

### DAG (Directed Acyclic Graph)
- Etapas com dependências explícitas
- Etapas independentes executam em paralelo
- Exemplo: lint e test em paralelo, deploy após ambos
- Ferramentas: Airflow, Dagster, Prefect

## Regras de Ouro
- Timeout explícito em cada etapa
- Retry com backoff em falhas transitórias
- Log de cada etapa com timestamp
- Notificação em falha (Slack, email)
- Idempotência: reexecutar não causa dano

## Anti-Patterns
- Loop infinito sem condição de saída
- Sem timeout (loop trava para sempre)
- Sem log (impossível depurar)
- Sem notificação de falha
- Estado compartilhado entre loops paralelos
