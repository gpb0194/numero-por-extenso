# Número por extenso 
- Este prejeto converte numeros inteiros em seus respectivos valores por extenso,
  em português do Brasil. Suporta números negativos e valores inteiros até 999.999

## Tecnologias usadas
- Python 3.x

## Como usar

1. Clone o repositório:
   '''bash
   git clone
   https://github.com/gpb0194/numero-por-extenso.git
   cd numero-por-extenso

2. Execute o script principal
   python numero_por_extenso

## Estrutura do código
- num_extenso(num) - Função principal para exibir o número por extenso;
- Dicionários para unidades, dezenas, centenas e casos especiais;
- Funções auxiliares para tratar cada parte do número (unidade, dezena, centena, milhar);
- Suporte a números negativos com prefixo "menos".

## Testes
- Teste manuais. No momento você pode digitar diferentes valores e conferir o resultado no console.

## Melhorias futuras
- Implementar testes automatizados com unittest ou pytest;
- Adcionar suporte a milhões e bilhões;
- Criar interface de API (usando Flask ou FastAPI);
- Suporte a moeda (ex: "R$1.234,56")
- Criar interface grafica simples.

## Contribuindo
- Pull requests são bem vindos! Para sugestões maiores, abra uma issue para discutirmos juntos.

## Licença
- O projeto está licenciado sob a licença MIT.
