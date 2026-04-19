import streamlit as st
import pandas as pd
import json
import time

# --- CONFIGURAÇÃO DA PÁGINA (Foco em UX) ---
st.set_page_config(page_title="Lumina - Agente Financeiro", page_icon="🌟")

# --- CARREGAMENTO DE DADOS (Base de Conhecimento) ---
def load_data():
    transacoes = pd.read_csv('../data/transacoes.csv')
    historico = pd.read_csv('../data/historico_atendimento.csv')
    with open('../data/perfil_investidor.json', 'r', encoding='utf-8') as f:
        perfil = json.load(f)
    with open('../data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
        produtos = json.load(f)
    return transacoes, historico, perfil, produtos

transacoes, historico, perfil, produtos = load_data()

# --- INTERFACE LATERAL (Sidebar) ---
with st.sidebar:
    st.title("🌟 Lumina")
    st.subheader(f"Cliente: {perfil['nome']}")
    st.write(f"**Perfil:** {perfil['perfil_investidor'].capitalize()}")
    st.progress(perfil['reserva_emergencia_atual'] / 15000)
    st.caption("Progresso da Reserva de Emergência")
    st.divider()
    st.info("Meta Atual: Entrada do Apartamento (2027)")

# --- LÓGICA DO CHAT (Simulação de IA Generativa) ---
st.title("Assistente Financeira Consultiva")

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Mensagem inicial proativa
    intro = f"Olá, {perfil['nome']}! Sou a Lumina. Notei que você gastou R$ {transacoes[transacoes['categoria']=='transporte']['valor'].sum():.2f} com transporte este mês. Vamos otimizar isso para sua meta do apartamento?"
    st.session_state.messages.append({"role": "assistant", "content": intro})

# Exibir histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do Usuário
if prompt := st.chat_input("Como posso ajudar suas finanças hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta da Lumina (Simulando raciocínio com os dados)
    with st.chat_message("assistant"):
        with st.spinner("Lumina está analisando seus dados..."):
            time.sleep(1) # Simula latência de IA
            
            # Lógica simples de resposta baseada em palavras-chave para o protótipo
            if "investir" in prompt.lower() or "dinheiro" in prompt.lower():
                response = f"Com base no seu perfil **{perfil['perfil_investidor']}**, o produto mais indicado no momento é o **{produtos[0]['nome']}**. Ele rende {produtos[0]['rentabilidade']} e é ideal para quem, como você, não aceita riscos elevados no momento."
            elif "gastei" in prompt.lower() or "gastos" in prompt.lower():
                total_gastos = transacoes[transacoes['tipo']=='saida']['valor'].sum()
                response = f"Você gastou um total de R$ {total_gastos:.2f} este mês. O maior peso foi em **Moradia**. Quer que eu analise onde podemos cortar?"
            else:
                response = "Entendi sua dúvida. Como sua assistente, foco em ajudar você a atingir sua meta de R$ 50.000 para o apartamento. Pode me dar mais detalhes?"
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
