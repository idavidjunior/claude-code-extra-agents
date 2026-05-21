# Backend Patterns — API, Cache, Filas

## Arquitetura em Camadas
- Controller: recebe HTTP, valida input, retorna resposta
- Service: lógica de negócio pura
- Repository: acesso a dados
- Domain: entidades e value objects

## Cache
- Cache aside: aplicação gerencia cache manualmente
- Read through: cache busca do banco automaticamente
- Write behind: escrita assíncrona no banco via cache
- Invalidação: TTL + invalidação explícita em mutation

## Filas e Mensageria
- Para tarefas lentas: envio de email, geração de relatório
- Para desacoplamento: serviço A não espera serviço B
- Para resiliência: retry automático em falha temporária
- Ferramentas: RabbitMQ, SQS, Redis Streams

## Regras de Ouro
- Controller nunca tem lógica de negócio
- Service nunca sabe HTTP (req/res)
- Repository nunca tem lógica de negócio
- Cache tem TTL explícito
- Fila tem dead letter queue

## Anti-Patterns
- Controller com regra de negócio
- Cache sem TTL (memória infinita)
- Fila sem dead letter (mensagens perdidas)
- Service que acessa banco diretamente sem repository
