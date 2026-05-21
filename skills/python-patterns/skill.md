---
name: python-patterns
description: |
  Padrões de Python: estrutura de projeto, type hints, testes, concorrência.
  Trigger phrases: "python", "Python patterns", "pytest", "type hints", "asyncio"
allowed-tools: Read, Grep, Bash, Write, Edit
version: 1.0.0
---

# Python Patterns — Idiomas e Boas Práticas

## Estrutura de Projeto
- src/ ou app/ para código fonte
- tests/ espelhando src/
- pyproject.toml para configuração moderna
- Type hints em toda função pública (mypy strict)

## Data Classes e Pydantic
- dataclasses para objetos de domínio simples
- Pydantic para validação de entrada (FastAPI)
- Enum para constantes com significado
- Structural pattern matching (Python 3.10+)

## Tratamento de Erros
- Exceções específicas, nunca except Exception genérico
- Context managers (with) para recursos
- Logging estruturado com structlog
- Nunca passe erros silenciosamente

## Concorrência
- asyncio para I/O bound
- multiprocessing para CPU bound
- ThreadPoolExecutor para legacy bloqueante
- Sempre defina timeout em operações de rede

## Regras de Ouro
- Virtual environment por projeto
- pip-audit ou safety para vulnerabilidades
- black + ruff + mypy no CI
- Testes com pytest + fixtures + parametrize
- Requirements congelados para produção

## Anti-Patterns
- import * (polui namespace)
- Mutable default arguments
- List comprehension com efeito colateral
- Exceção sem mensagem
- print em produção (use logging)
