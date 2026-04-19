import pandas as pd
import json
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def carregar_dados():
    transacoes = pd.read_csv("../data/transacoes.csv")
    historico = pd.read_csv("../data/historico_atendimento.csv")
    
    with open("../data/perfil_investidor.json") as f:
        perfil = json.load(f)
        
    with open("../data/produtos_financeiros.json") as f:
        produtos = json.load(f)
        
    return transacoes, historico, perfil, produtos


def montar_contexto(transacoes, perfil):
    total_gastos = transacoes[transacoes["tipo"] == "saida"]["valor"].sum()
    renda = perfil["renda_mensal"]
    poupanca = renda - total_gastos

    contexto = f"""
Dados do Cliente:
Nome: {perfil['nome']}
Perfil: {perfil['perfil_investidor']}
Renda mensal: R$ {renda}

Resumo financeiro:
Total de gastos: R$ {round(total_gastos, 2)}
Capacidade de poupança: R$ {round(poupanca, 2)}
"""

    return contexto


def responder(pergunta):
    transacoes, historico, perfil, produtos = carregar_dados()
    contexto = montar_contexto(transacoes, perfil)

    system_prompt = """
Você é um agente financeiro inteligente.

Siga as regras:
- Use apenas os dados fornecidos
- Não invente informações
- Seja claro e objetivo
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{contexto}\n\nPergunta: {pergunta}"}
        ]
    )

    return response.choices[0].message.content
