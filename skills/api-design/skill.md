# API Design — REST, Paginação, Erros

## Estrutura de URL
- Coleções: /orders
- Item: /orders/{id}
- Sub-recursos: /orders/{id}/items
- Verbos HTTP: GET (ler), POST (criar), PUT (substituir), PATCH (atualizar parcial), DELETE (remover)

## Paginação
- Use cursor-based (recomendado) ou offset-based
- Resposta sempre inclui: next, prev, total
- Limite máximo de itens por página (max 100)

## Respostas de Erro
- Use códigos HTTP corretos: 400 (validação), 401 (não autenticado), 403 (sem permissão), 404 (não encontrado), 409 (conflito), 422 (entidade não processável), 429 (rate limit), 500 (erro interno)
- Corpo do erro padronizado: { "error": { "code": "...", "message": "...", "details": [...] } }
- Nunca exponha stack trace na resposta

## Versionamento
- Prefira header: Accept: application/vnd.api.v2+json
- Alternativa: URL /v2/orders
- Mantenha versões antigas por pelo menos 6 meses

## Regras de Ouro
- Idempotência: POST com Idempotency-Key para operações críticas
- Rate limiting: 429 com header Retry-After
- Compressão: gzip para payloads > 1KB
- Caching: ETag e Last-Modified
- CORS: apenas origens explícitas, nunca wildcard com credenciais
- Autenticação via Authorization header, nunca cookie para APIs

## Anti-Patterns
- GET que modifica dados
- Rota /getOrders (verbo na URL)
- Erro 200 com mensagem de erro no corpo
- IDs sequenciais expostos (use UUID)
- Paginação sem total