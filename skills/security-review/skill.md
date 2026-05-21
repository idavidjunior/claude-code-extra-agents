---
name: security-review
description: |
  Checklist de segurança OWASP Top 10 para code review.
  Trigger phrases: "security review", "OWASP", "vulnerability check", "security checklist"
allowed-tools: Read, Grep, Bash
version: 1.0.0
---

# Security Review — Checklist de Segurança

## OWASP Top 10

1. Broken Access Control — verifique se toda rota admin tem controle de acesso
2. Cryptographic Failures — dados sensíveis em trânsito (HTTPS) e em repouso (AES-256)
3. Injection — SQL, NoSQL, OS command, template em toda entrada do usuário
4. Insecure Design — threat modeling antes de codar
5. Security Misconfiguration — headers HTTP, CORS restritivo, debug mode off
6. Vulnerable Components — dependências atualizadas, sem CVEs conhecidos
7. Auth Failures — bcrypt/argon2, sem limite de tentativas, MFA disponível
8. Software e Data Integrity — CI/CD seguro, assinatura de artefatos
9. Logging e Monitoring — logs de auth, transações e erros com trace_id
10. SSRF — URLs do usuário nunca acessam recursos internos

## Checklist rápido para code review

- Nenhum segredo hardcoded (API key, token, senha)
- Toda query SQL usa parâmetros preparados
- Input do usuário validado e sanitizado
- Output escapado (XSS prevenido)
- CORS restrito a origens conhecidas
- Rate limiting em endpoints de auth
- Logs não contêm PII ou segredos
- Dependências sem CVEs críticos ou altos

## Headers HTTP obrigatórios
- Content-Security-Policy
- Strict-Transport-Security (HSTS)
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- Referrer-Policy: strict-origin

## Referências
- OWASP Top 10: owasp.org/Top10
- OWASP Cheat Sheet Series: cheatsheetseries.owasp.org
