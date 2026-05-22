# Claude Code Extra Agents

Ecossistema de agentes e skills para desenvolvimento, qualidade, segurança e operação.

## Estado Atual
- Agentes: 22
- Skills: 30
- Comandos: 13

## Princípios
- Cada agente tem um propósito claro e fronteira de responsabilidade.
- Skills são playbooks reutilizáveis para execução tática.
- Orquestração prioriza: objetivo do usuário -> risco -> custo -> velocidade.
- Sem sobreposição: um agente lidera, os demais apoiam por contexto.

## Fluxo Recomendado
1. `doctor` para validar ambiente e pré-condições.
2. `sentinel` para triagem e roteamento inteligente.
3. Agente especialista para execução principal.
4. Skills complementares por domínio.
5. Relatório final com riscos, decisões e próximos passos.

## Documentação de Orquestração
- [Operating Model](docs/OPERATING_MODEL.md)
- [Skill Index](docs/SKILL_INDEX.md)
- [Agent x Skill Matrix](docs/AGENT_SKILL_MATRIX.md)

## Validação
- Estrutura de front matter: `./scripts/validate-ecosystem.ps1`
- Links locais da documentação: `./scripts/validate-doc-links.ps1`

## Comandos
- `/doctor`
- `/forensic`
- `/verify`
- `/simulate`
- `/navigate`
- `/perf`
- `/audit`
- `/diagram`
- `/contract-test`
- `/i18n`
- `/migrate`
- `/incident`
- `/unbreak`

## Licença
MIT
