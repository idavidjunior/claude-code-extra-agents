# Agentic Search — Navegação Web Autônoma com Ferramentas Reais

## Quando Aplicar
- O Sentinel precisa buscar informações atualizadas na internet
- Extrair dados estruturados de sites que não têm API
- Automatizar tarefas repetitivas de navegação
- Pesquisar documentação técnica em múltiplas fontes simultaneamente

## Arquitetura Híbrida (o que funciona de verdade)

### Modo 1: DOM Determinístico (PRIMÁRIO)
**Ferramenta principal: Playwright MCP**
- Transforma o DOM ao vivo em texto estruturado acessível ao modelo
- Navegação por seletores CSS/XPath — determinística, rápida, sem alucinação
- Cobertura ideal: sites com estrutura HTML previsível

**Ferramenta secundária: Stagehand (Browserbase)**
- Automação com linguagem natural
- Compatível com Playwright e Puppeteer
- Melhor para prototipagem rápida

### Modo 2: Visão Computacional (FALLBACK)
**Ferramenta: Computer Use (Claude) ou Operator API**
- Funciona em interfaces não padronizadas
- Limitação: mais lento, mais caro, 35.8% sucesso em tarefas reais
- Use APENAS quando DOM falhar

### Modo 3: API Direta (PREFERENCIAL)
- Sempre verifique se o site tem API antes de navegar
- APIs são 10-100x mais baratas e 100% determinísticas

## Ferramentas por Caso de Uso
| Tarefa | Primária | Fallback |
|--------|----------|----------|
| Documentação técnica | Playwright MCP | Stagehand |
| Extrair tabelas | Playwright MCP + seletores | Stagehand |
| Formulários | Playwright MCP | Stagehand |
| Dashboard | Stagehand | Computer Use |
| Captcha | NÃO AUTOMATIZAR | Humano |

## Processo de Navegação Segura

### Antes de navegar
- Verificar se o site tem API
- Confirmar domínio legítimo (HTTPS)
- Definir escopo de URLs permitidas
- Timeouts: 30s por página, 5min por tarefa

### Durante a navegação
- NUNCA clicar em links externos sem confirmação
- NUNCA inserir credenciais ou tokens
- NUNCA baixar executáveis
- NUNCA submeter formulários com consequências reais

### Extração de dados
- Prefira JSON-LD, microdata, RDFa
- Tabelas: page.locator + parse
- Listas: seletores CSS consistentes
- Texto livre: page.innerText

## Anti-Patterns
- Navegar sem escopo definido
- Usar visão quando DOM funciona
- Simular clique quando API existe
- Extrair dados sem verificar fonte
- Ignorar robots.txt

## Referências
- Playwright MCP: github.com/microsoft/playwright-mcp
- Stagehand: stagehand.dev
- Computer Use: docs.anthropic.com
