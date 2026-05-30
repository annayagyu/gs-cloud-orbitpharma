import streamlit as st

# Configuração da página
st.set_page_config(page_title="Orbit Pharma Labs", page_icon="🚀", layout="wide")

# Título Principal
st.title("🚀 Orbit Pharma Labs — Controle de Bioreatores Orbitais")
st.subheader("Solução integrada para cristalização de proteínas em microgravidade")
st.write("---")

# Abas do sistema
aba_projeto, aba_dashboard = st.tabs(["📋 Sobre o Projeto", "📊 Dashboard de Telemetria"])

with aba_projeto:
    st.header("O Problema Espacial")
    st.write(
        "A cristalização de proteínas em ambientes de microgravidade (como na ISS) permite o crescimento "
        "de cristais perfeitamente simétricos e puros, acelerando pesquisas farmacêuticas cruciais para a Terra. "
        "Contudo, a altíssima latência de comunicação, os custos severos de telemetria e o impacto de microvibrações "
        "tornam o monitoramento tradicional inviável e extremamente custoso."
    )
    
    st.header("Nossa Solução & Vínculo com ODS")
    st.write(
        "A **Orbit Pharma Labs** propõe uma plataforma centralizada na nuvem integrada a pipelines de Big Data "
        "e modelos locais de Visão Computacional (Edge Computing). Esta infraestrutura garante a tomada de decisão "
        "autônoma e o monitoramento seguro dos experimentos biológicos espaciais."
    )
    st.info("📌 **Alinhamento Global:** Este projeto atende diretamente ao **ODS 9: Indústria, Inovação e Infraestrutura**.")

with aba_dashboard:
    st.header("Monitoramento em Tempo Real (Dados Simulados)")
    st.write("Métricas consolidadas a partir do pipeline de dados e das análises preditivas de IA.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Temperatura do Reator", value="37.2 °C", delta="Estável")
    col2.metric(label="Nível de pH do Fluido", value="7.41", delta="-0.02")
    col3.metric(label="Status do Cristal (Previsão IA)", value="94% Puro", delta="Crescimento Saudável")
    
    st.write("---")
    st.warning("⚠️ **Alerta do Sistema:** Nenhuma microvibração destrutiva detectada nas últimas 6 horas.")
