---
name: cost-aware-llm-pipeline
description: |
  Otimização de custo com LLMs: cache, batching, escolha de modelo.
  Trigger phrases: "LLM cost", "token cost", "model routing", "optimize LLM", "reduce cost"
allowed-tools: Read, Grep, Bash
version: 1.0.0
---

# Cost-Aware LLM Pipeline — Otimização de Custo com LLMs

## Estratégia de Modelos por Tarefa
| Tarefa | Modelo | Custo |
|--------|--------|-------|
| Classificação simples | Claude Haiku / GPT-4o-mini | Baixo |
| Geração de código | Claude Sonnet | Médio |
| Análise complexa | Claude Opus / GPT-4o | Alto |
| Embeddings | text-embedding-3-small | Baixo |

## Padrões de Economia
- Cache de respostas idênticas (SHA-256 da entrada)
- Batching de requisições quando possível
- Prompt mais curto = token mais barato
- Streaming para respostas longas (melhor UX, mesmo custo)

## Regras de Ouro
- Comece sempre pelo modelo mais barato
- Suba para modelo mais caro apenas se necessário
- Registre custo por requisição
- Defina orçamento máximo por mês
- Alerta quando atingir 80% do orçamento

## Anti-Patterns
- Usar modelo caro para tarefa simples
- Não cachear respostas repetidas
- Prompt longo com contexto desnecessário
- Sem monitoramento de custo
