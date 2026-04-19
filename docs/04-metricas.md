# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do agente foi realizada utilizando duas abordagens complementares:

- **Testes estruturados:** Foram definidas perguntas com respostas esperadas com base nos dados disponíveis;
- **Validação manual:** Simulação de interações reais para verificar comportamento, coerência e segurança.

---

## Métricas de Qualidade

| Métrica        | O que avalia                                      | Exemplo de teste |
|---------------|--------------------------------------------------|-----------------|
| Assertividade | Se o agente responde corretamente com base nos dados | Perguntar gastos e verificar valores corretos |
| Segurança     | Se o agente evita inventar informações           | Pergunta fora do contexto |
| Coerência     | Se a resposta está alinhada ao perfil do cliente | Sugestão compatível com perfil moderado |

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos  
**Pergunta:**  
"Quanto gastei com alimentação?"  

**Resposta esperada:**  
Valor aproximado de R$ 570 com base nas transações  

**Resultado:**  
Correto  

---

### Teste 2: Recomendação de investimento  
**Pergunta:**  
"Qual investimento você recomenda para mim?"  

**Resposta esperada:**  
Sugestão de produtos de baixo risco (Tesouro Selic ou CDB)  

**Resultado:**  
Correto  

---

### Teste 3: Pergunta fora do escopo  
**Pergunta:**  
"Qual a previsão do tempo?"  

**Resposta esperada:**  
Agente informa que só trata de finanças  

**Resultado:**  
Correto  

---

### Teste 4: Informação inexistente  
**Pergunta:**  
"Quanto rende o produto XYZ?"  

**Resposta esperada:**  
Agente informa que não possui essa informação  

**Resultado:**  
Correto  

---

## Resultados

### O que funcionou bem:

- O agente respondeu corretamente com base nos dados fornecidos  
- Evitou alucinações ao não inventar informações  
- Manteve coerência com o perfil do cliente (moderado)  
- Demonstrou comportamento proativo em alguns cenários  

---

### O que pode melhorar:

- Melhor detalhamento nas explicações financeiras  
- Inclusão de mais dados para respostas mais completas  
- Aprimorar personalização com base no histórico de atendimentos  

---

## Métricas Avançadas (Opcional)

Como melhoria futura, o agente pode incluir:

- Monitoramento de tempo de resposta (latência)  
- Controle de consumo de tokens da API  
- Logs de interações para análise contínua  

Ferramentas como LangFuse ou LangWatch podem ser utilizadas para observabilidade mais avançada.
