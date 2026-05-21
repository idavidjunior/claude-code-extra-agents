---
name: docker-patterns
description: |
  Docker em produção: multi-stage builds, segurança, docker compose.
  Trigger phrases: "docker", "container", "Dockerfile", "docker compose", "image"
allowed-tools: Read, Grep, Bash
version: 1.0.0
---

# Docker Patterns — Containers em Produção

## Dockerfile de Produção
- Multi-stage build: separa build de runtime
- Imagem final baseada em distroless ou alpine
- Usuário não-root (USER 1000)
- HEALTHCHECK definido
- Nenhum segredo na imagem (docker history)

## Docker Compose
- Serviços com healthcheck e depends_on
- Redes separadas: frontend, backend, database
- Volumes nomeados para dados persistentes
- Variáveis de ambiente via .env (não no compose)

## Segurança
- Nunca rode como root
- Imagens scanneadas com Trivy ou Snyk
- Tags explícitas (nunca :latest em produção)
- dockerignore para excluir secrets e node_modules
- Read-only filesystem quando possível

## Anti-Patterns
- Um container com múltiplos processos
- Dados em bind mount em vez de volume
- .env commitado no repositório
- Imagem com ferramentas de build no runtime
- Portas expostas desnecessariamente
