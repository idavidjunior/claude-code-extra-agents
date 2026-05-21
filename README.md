```markdown
# 🧠 Claude Code Extra Agents

20 agentes especializados, 18 skills de domínio e 13 comandos para transformar o Claude Code em um ecossistema completo de desenvolvimento, segurança e operações.

## ⚡ Instalação

### Plugin (recomendado)
```
/plugin marketplace add idavidjunior/claude-code-extra-agents
/plugin install claude-code-extra-agents@claude-code-extra-agents
```

### Script (Windows)
```powershell
.\install.ps1
```

### Script (Linux/macOS)
```bash
bash install.sh
```

---

## 🧠 Agentes

| Agente | Comando | Função |
|--------|---------|--------|
| **doctor** | `/doctor` | Auto-diagnóstico do ambiente. Agenda, cache, lock. |
| **sentinel** | automático | Orquestrador de 9 camadas com ferramentas reais |
| **debug-forensic** | `/forensic` | Investigação forense de erros em produção |
| **ai-code-verifier** | `/verify` | Verifica código gerado por IA antes do merge |
| **vulnerability-hunter** | automático | Caça cirúrgica de vulnerabilidades. Zero alarmismo. |
| **web-navigator** | `/navigate` | Navegação web autônoma com DOM + visão |
| **incident-simulator** | `/simulate` | War games para treinar times |
| **performance-profiler** | `/perf` | Profiling de CPU, memória, banco e rede |
| **dependency-auditor** | `/audit` | Auditoria de supply chain e CVEs |
| **api-integration-specialist** | automático | Integração idiomática com APIs externas |
| **schema-evolution-planner** | automático | Migração de banco sem downtime |
| **diagram-as-code** | `/diagram` | Gera Mermaid, PlantUML e C4 |
| **contract-test-broker** | `/contract-test` | Testes de contrato entre serviços |
| **prompt-optimizer** | automático | Otimização de prompts com evals A/B |
| **rag-pipeline-builder** | automático | Construção de pipelines RAG |
| **legacy-modernizer** | `/migrate` | Migração de código legado |
| **monorepo-architect** | automático | Gerência de monorepos |
| **i18n-l10n-engineer** | `/i18n` | Internacionalização e localização |
| **a11y-auditor** | automático | Auditoria WCAG 2.2 |
| **feature-flag-surgeon** | automático | Feature flags com rollout gradual |

---

## 🛠️ Skills Refinadas

| Skill | Conteúdo |
|-------|----------|
| **resilience-engineering** | 6 pilares: circuit breaker, retry, timeout, bulkhead, graceful degradation, chaos engineering |
| **observability-stack** | Logging estruturado, métricas golden signals, tracing OpenTelemetry |
| **authz-authn-matrix** | OAuth2, OIDC, Passkeys, JWT, RBAC, ABAC, ReBAC |
| **agentic-search** | Navegação híbrida: DOM + visão + API direta |

---

## ⚡ Comandos

| Comando | Agente |
|---------|--------|
| `/doctor` | Auto-diagnóstico |
| `/forensic` | Debug forense |
| `/verify` | Verificador IA |
| `/simulate` | Simulador de incidentes |
| `/navigate` | Navegador web |
| `/perf` | Performance |
| `/audit` | Auditoria |
| `/diagram` | Diagramas |
| `/contract-test` | Testes de contrato |
| `/i18n` | Internacionalização |
| `/migrate` | Migração |
| `/incident` | Postmortem |
| `/unbreak` | Breaking changes |

---

## 🛡️ Arquitetura

```
DOCTOR → SENTINEL → Debug Forensic | AI Code Verifier | Vulnerability Hunter | Web Navigator | Incident Simulator
```

## 🚀 Primeiros passos

1. Instale o plugin
2. Execute `/doctor`
3. Use `/verify` antes de merge com código IA
4. Use `/simulate` para treinar o time
5. Use `/forensic` quando algo quebrar

## 📄 Licença
MIT
```
