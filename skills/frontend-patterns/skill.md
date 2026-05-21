# Frontend Patterns — React e Next.js

## Estrutura de Componentes
- Atomic Design: atoms, molecules, organisms, templates, pages
- Container/Presentational: lógica separada da apresentação
- Custom Hooks: extraia lógica reutilizável

## Gerenciamento de Estado
- Estado local: useState para UI
- Estado compartilhado: Context ou Zustand
- Estado de servidor: React Query ou SWR
- URL: estado que deve sobreviver a refresh

## Performance
- React.memo para componentes puros
- useMemo e useCallback com moderação
- Code splitting com dynamic import
- Imagens com next/image e lazy loading

## Regras de Ouro
- Fetch de dados no servidor (RSC) sempre que possível
- Loading e error states sempre tratados
- Formulários com validação client e server
- Acessibilidade: labels, roles, teclado
- Mobile-first com media queries

## Anti-Patterns
- useState para dados de servidor
- useEffect desnecessário
- Prop drilling profundo (> 3 níveis)
- Sem tratamento de loading/error
- Div aninhada sem semântica
