import streamlit as st
from agente import responder

st.title("💰 Agente Financeiro")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    resposta = responder(pergunta)
    st.write("### Resposta:")
    st.write(resposta)
