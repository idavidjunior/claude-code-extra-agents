# Go Patterns — Idíomas e Boas Práticas

## Tratamento de Erros
- Erro como valor, nunca exceção
- Sempre verifique erro antes de continuar
- fmt.Errorf com %w para wrapping
- errors.Is e errors.As para verificação
- Panic apenas para erros irrecuperáveis

## Concorrência
- Goroutines com context.Context
- sync.WaitGroup para esperar grupo
- channels para comunicação entre goroutines
- select para múltiplos canais
- errgroup para cancelamento em grupo

## Estrutura de Projeto
- cmd/ para entrypoints
- internal/ para código privado
- pkg/ para bibliotecas públicas
- api/ para protobuf e OpenAPI
- configs/ para arquivos de configuração

## Regras de Ouro
- Interfaces pequenas (1-3 métodos)
- Aceite interfaces, retorne structs
- defer para cleanup (Close, Unlock)
- go fmt e go vet antes de commit
- Testes com table-driven tests

## Anti-Patterns
- Panic em biblioteca
- Goroutine sem cancelamento
- Interface grande (Interface Segregation)
- Ignorar erros com _
- Mutex copiado por valor
