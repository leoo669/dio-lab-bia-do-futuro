# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Identificar interesses do cliente (ex: Tesouro Selic, CDB) e evitar recomendações repetidas |
| `perfil_investidor.json` | JSON | Personalizar recomendações com base em renda, objetivos e perfil de risco |
| `produtos_financeiros.json` | JSON | Filtrar e sugerir produtos compatíveis com o perfil do cliente |
| `transacoes.csv` | CSV | Analisar comportamento financeiro, padrões de consumo e capacidade de investimento |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram enriquecidos com interpretações derivadas para melhorar a inteligência do agente:

### Classificação de gastos por categoria:
- Moradia: R$ 1.380  
- Alimentação: R$ 570  
- Transporte: R$ 295  
- Saúde: R$ 188  
- Lazer: R$ 55,90  

### Cálculo de indicadores financeiros:
- Receita mensal: R$ 5.000  
- Total de despesas: R$ 2.488,90  
- Capacidade de poupança estimada: ~R$ 2.500  

### Análise de perfil:
- Perfil: moderado  
- Não aceita alto risco  
- Foco atual: reserva de emergência  

### Progresso de metas:
- Reserva de emergência: 66% concluída (R$ 10.000 de R$ 15.000)

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

- `transacoes.csv` e `historico_atendimento.csv` são carregados via pandas  
- `perfil_investidor.json` e `produtos_financeiros.json` são carregados como objetos JSON  

Os dados são processados no início da aplicação e mantidos em memória para consultas rápidas.

---

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

O agente utiliza uma abordagem dinâmica:

- Seleciona apenas os dados relevantes para cada pergunta  
- Resume informações antes de enviar ao modelo  
- Cruza diferentes fontes para gerar contexto mais rico  

**Exemplos:**

- Pergunta sobre gastos → usa transações + agregações  
- Sugestão de investimento → usa perfil + produtos + histórico  
- Acompanhamento de meta → usa perfil + progresso calculado  

Isso evita sobrecarga de contexto e melhora a precisão das respostas.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Idade: 32 anos
- Renda mensal: R$ 5.000
- Perfil: Moderado
- Aceita risco alto: Não

Objetivos:
- Reserva de emergência: R$ 15.000 (66% concluída)
- Entrada de imóvel: R$ 50.000 até 2027

Resumo financeiro:
- Total de gastos no mês: R$ 2.488,90
- Capacidade de poupança: ~R$ 2.500
- Maior gasto: Moradia (R$ 1.380)

Últimas transações relevantes:
- Supermercado: R$ 450
- Restaurante: R$ 120
- Combustível: R$ 250

Histórico de interações:
- Interesse em Tesouro Selic e CDB
- Já buscou informações sobre reserva de emergência

Produtos elegíveis:
- Tesouro Selic (baixo risco)
- CDB Liquidez Diária (baixo risco)
- Fundo Multimercado (risco médio)
...
```
