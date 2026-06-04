import streamlit as st
import random
import math

st.set_page_config(
    page_title="Orbit Pharma Labs",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS customizado ──────────────────────────────────────────
st.markdown("""
<style>
  /* Fundo geral */
  .stApp { background-color: #0a0e1a; color: #e0e6f0; }

  /* Sidebar */
  [data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1b2a 0%, #1a2744 100%);
    border-right: 1px solid #1e3a5f;
  }

  /* Títulos */
  h1, h2, h3 { color: #4fc3f7 !important; }

  /* Cards de métrica */
  [data-testid="metric-container"] {
    background: linear-gradient(135deg, #0d1b2a, #1a2744);
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 16px;
  }
  [data-testid="stMetricValue"] { color: #4fc3f7 !important; font-size: 2rem !important; }
  [data-testid="stMetricDelta"] { color: #81c784 !important; }

  /* Tabs */
  .stTabs [data-baseweb="tab-list"] { background-color: #0d1b2a; border-radius: 8px; }
  .stTabs [data-baseweb="tab"] { color: #90caf9; }
  .stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: #1e3a5f;
    color: #4fc3f7 !important;
    border-radius: 6px;
  }

  /* Caixas de info/warning/success */
  .stAlert { border-radius: 10px; }

  /* Divisor */
  hr { border-color: #1e3a5f; }

  /* Tabela */
  .stDataFrame { border: 1px solid #1e3a5f; border-radius: 8px; }

  /* Botão */
  .stButton > button {
    background: linear-gradient(135deg, #1565c0, #0d47a1);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 20px;
  }
  .stButton > button:hover { background: linear-gradient(135deg, #1976d2, #1565c0); }

  /* Badge customizado */
  .badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: bold;
    margin: 2px;
  }
  .badge-green  { background: #1b5e20; color: #a5d6a7; border: 1px solid #2e7d32; }
  .badge-blue   { background: #0d47a1; color: #90caf9; border: 1px solid #1565c0; }
  .badge-orange { background: #e65100; color: #ffcc80; border: 1px solid #ef6c00; }
  .badge-red    { background: #b71c1c; color: #ef9a9a; border: 1px solid #c62828; }

  /* Card personalizado */
  .custom-card {
    background: linear-gradient(135deg, #0d1b2a, #1a2744);
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 20px;
    margin: 8px 0;
  }
  .kpi-value { font-size: 2.5rem; font-weight: bold; color: #4fc3f7; }
  .kpi-label { font-size: 0.85rem; color: #90a4ae; text-transform: uppercase; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🚀 Orbit Pharma Labs")
    st.markdown("**Missão:** Cristalização de proteínas em microgravidade orbital")
    st.markdown("---")

    st.markdown("### 🛰️ Status da Missão")
    st.markdown('<span class="badge badge-green">● SISTEMA OPERACIONAL</span>', unsafe_allow_html=True)
    st.markdown('<span class="badge badge-blue">● ISS LINK ATIVO</span>', unsafe_allow_html=True)
    st.markdown('<span class="badge badge-green">● AZURE CLOUD OK</span>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📡 Satélite Ativo")
    st.markdown("**Órbita:** LEO — 408 km")
    st.markdown("**Inclinação:** 51.6°")
    st.markdown("**Velocidade:** 27.600 km/h")
    st.markdown("**Período orbital:** 92.68 min")

    st.markdown("---")
    st.markdown("### 👥 Equipe")
    st.markdown("""
    - Sofia Amorim Coutinho
    - Anna Yagyu
    - Felipe Capriotti da Silva Santos
    - Gustavo Kawamura Christofani
    - Gabriel Pacheco
    """)
    st.markdown("**FIAP — ESW 4º Ano — 2026**")


# ── Header ───────────────────────────────────────────────────
st.markdown("""
<div style='background: linear-gradient(135deg, #0d1b2a, #1a2744);
            border: 1px solid #1e3a5f; border-radius: 16px;
            padding: 32px; margin-bottom: 24px; text-align: center;'>
  <h1 style='color: #4fc3f7; font-size: 2.4rem; margin: 0;'>
    🚀 Orbit Pharma Labs
  </h1>
  <p style='color: #90caf9; font-size: 1.1rem; margin: 8px 0 0 0;'>
    Plataforma de Controle e Monitoramento de Bioreatores Orbitais
  </p>
  <p style='color: #546e7a; font-size: 0.9rem; margin: 4px 0 0 0;'>
    Cristalização de proteínas em microgravidade · Azure Cloud · CI/CD Automatizado
  </p>
</div>
""", unsafe_allow_html=True)


# ── KPIs Globais ─────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
k1.metric("🧬 Pureza do Cristal (IA)", "94.3%", "+0.8%")
k2.metric("🌡️ Temperatura Reator", "37.2 °C", "Estável")
k3.metric("💧 pH do Fluido", "7.41", "-0.02")
k4.metric("⚡ Uptime Azure", "99.97%", "+0.01%")

st.markdown("---")


# ── Abas ─────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "🌍 Sobre o Projeto",
    "📊 Dashboard de Telemetria",
    "🏗️ Arquitetura Cloud",
    "📋 Status do Pipeline"
])


# ═══════════════════════════════════════════════════════
# ABA 1 — SOBRE O PROJETO
# ═══════════════════════════════════════════════════════
with tab1:
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("### 🔬 O Problema Espacial")
        st.markdown("""
        A cristalização de proteínas em **microgravidade** (como na ISS a 408 km de altitude)
        elimina os efeitos de convecção e sedimentação, permitindo o crescimento de cristais
        **perfeitamente simétricos e puros** — estruturalmente impossíveis de replicar na Terra.

        Esses cristais aceleram a descoberta de tratamentos para doenças como:
        - 🦠 Câncer e doenças autoimunes
        - 🧠 Alzheimer e Parkinson
        - 💊 Resistência a antibióticos

        **O desafio:** latência de comunicação, custo severo de telemetria e
        sensibilidade a microvibrações tornam o monitoramento tradicional inviável.
        """)

    with col_b:
        st.markdown("### 💡 Nossa Solução")
        st.markdown("""
        A **Orbit Pharma Labs** opera uma plataforma SaaS em nuvem (Microsoft Azure)
        que conecta bioreatores em órbita baixa a algoritmos de IA em tempo real.

        **Stack tecnológico:**
        """)
        st.markdown("""
        | Camada | Tecnologia |
        |--------|-----------|
        | Cloud | Azure App Service + Key Vault |
        | CI/CD | GitHub Actions (OIDC) |
        | Backend | Python 3.12 + Streamlit |
        | IA | Modelos preditivos de pureza cristalina |
        | Monitoramento | Application Insights + Alert Rules |
        | Segurança | RBAC + DevSecOps |
        """)

    st.markdown("---")

    col_c, col_d, col_e = st.columns(3)
    with col_c:
        st.markdown("""
        <div class='custom-card' style='text-align:center;'>
          <div style='font-size:2rem;'>🎯</div>
          <div class='kpi-label'>ODS Alinhado</div>
          <div style='color:#4fc3f7; font-weight:bold; font-size:1.1rem;'>ODS 9</div>
          <div style='color:#90a4ae; font-size:0.85rem;'>Indústria, Inovação e Infraestrutura</div>
        </div>
        """, unsafe_allow_html=True)
    with col_d:
        st.markdown("""
        <div class='custom-card' style='text-align:center;'>
          <div style='font-size:2rem;'>🛰️</div>
          <div class='kpi-label'>Altitude Orbital</div>
          <div style='color:#4fc3f7; font-weight:bold; font-size:1.1rem;'>408 km</div>
          <div style='color:#90a4ae; font-size:0.85rem;'>Órbita Baixa Terrestre (LEO)</div>
        </div>
        """, unsafe_allow_html=True)
    with col_e:
        st.markdown("""
        <div class='custom-card' style='text-align:center;'>
          <div style='font-size:2rem;'>⚗️</div>
          <div class='kpi-label'>Experimentos Ativos</div>
          <div style='color:#4fc3f7; font-weight:bold; font-size:1.1rem;'>3 Bioreatores</div>
          <div style='color:#90a4ae; font-size:0.85rem;'>Missão Orbital Ativa</div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# ABA 2 — DASHBOARD DE TELEMETRIA
# ═══════════════════════════════════════════════════════
with tab2:
    st.markdown("### 📡 Telemetria em Tempo Real (Dados Simulados)")
    st.caption("Métricas consolidadas do pipeline de dados e das análises preditivas de IA orbital.")

    # Alerta de sistema
    st.success("✅ **Sistema Nominal:** Nenhuma microvibração destrutiva detectada nas últimas 6 horas.")

    st.markdown("---")

    # Bioreatores
    st.markdown("#### 🧪 Status dos Bioreatores")
    b1, b2, b3 = st.columns(3)

    bioreatores = [
        {"id": "BR-01", "proteina": "Insulina Cristalina", "pureza": 94.3, "temp": 37.2, "ph": 7.41, "status": "Nominal"},
        {"id": "BR-02", "proteina": "Hemoglobina S", "pureza": 88.7, "temp": 36.8, "ph": 7.38, "status": "Nominal"},
        {"id": "BR-03", "proteina": "Lisozima Pura", "pureza": 97.1, "temp": 37.5, "ph": 7.44, "status": "Ótimo"},
    ]

    for col, br in zip([b1, b2, b3], bioreatores):
        badge_color = "badge-green" if br["status"] in ["Nominal", "Ótimo"] else "badge-red"
        col.markdown(f"""
        <div class='custom-card'>
          <div style='font-size:1.3rem; font-weight:bold; color:#4fc3f7;'>{br["id"]}</div>
          <div style='color:#90a4ae; font-size:0.8rem; margin-bottom:8px;'>{br["proteina"]}</div>
          <div style='font-size:1.8rem; font-weight:bold; color:#81c784;'>{br["pureza"]}%</div>
          <div style='color:#90a4ae; font-size:0.75rem;'>Pureza cristalina</div>
          <div style='margin-top:8px;'>
            <span style='color:#b0bec5;'>🌡️ {br["temp"]}°C</span> &nbsp;
            <span style='color:#b0bec5;'>💧 pH {br["ph"]}</span>
          </div>
          <div style='margin-top:8px;'>
            <span class='badge {badge_color}'>● {br["status"]}</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Métricas de sistema
    st.markdown("#### ⚙️ Métricas do Sistema")
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Latência API", "142 ms", "-8 ms")
    m2.metric("Pacotes Recebidos", "1.847", "+23")
    m3.metric("Erros de Telemetria", "0", "0")
    m4.metric("CPU Azure", "12%", "-3%")
    m5.metric("Memória", "487 MB", "+12 MB")

    st.markdown("---")

    # Histórico simulado
    st.markdown("#### 📈 Histórico de Pureza Cristalina (Últimas 24h)")

    import pandas as pd
    horas = list(range(24))
    dados = {
        "Hora": [f"{h:02d}:00" for h in horas],
        "BR-01 (%)": [round(93 + math.sin(h * 0.4) * 1.5 + random.uniform(-0.2, 0.2), 2) for h in horas],
        "BR-02 (%)": [round(87 + math.sin(h * 0.3) * 1.2 + random.uniform(-0.2, 0.2), 2) for h in horas],
        "BR-03 (%)": [round(96 + math.sin(h * 0.5) * 0.8 + random.uniform(-0.1, 0.1), 2) for h in horas],
    }
    df = pd.DataFrame(dados).set_index("Hora")
    st.line_chart(df, height=280)

    st.markdown("---")
    st.warning("⚠️ **Próxima janela de comunicação com ISS:** em 47 minutos (órbita #8.234)")


# ═══════════════════════════════════════════════════════
# ABA 3 — ARQUITETURA CLOUD
# ═══════════════════════════════════════════════════════
with tab3:
    st.markdown("### 🏗️ Arquitetura da Infraestrutura Azure")

    col_arch1, col_arch2 = st.columns([1, 1])

    with col_arch1:
        st.markdown("#### Componentes Provisionados")
        componentes = [
            ("🌐", "Azure App Service", "orbitpharma", "Python 3.12 · Linux · SKU F1"),
            ("🔐", "Azure Key Vault", "kv-orbitpharma", "RBAC · Soft-delete 90d"),
            ("📊", "Application Insights", "orbitpharma", "Telemetria · Alertas · Métricas"),
            ("📁", "Resource Group", "rg-orbitpharma", "East US · Azure for Students"),
        ]
        for icon, nome, recurso, desc in componentes:
            st.markdown(f"""
            <div class='custom-card' style='padding:14px;'>
              <span style='font-size:1.2rem;'>{icon}</span>
              <strong style='color:#4fc3f7;'> {nome}</strong>
              <code style='color:#90caf9; margin-left:8px;'>{recurso}</code>
              <br><span style='color:#90a4ae; font-size:0.82rem;'>{desc}</span>
            </div>
            """, unsafe_allow_html=True)

    with col_arch2:
        st.markdown("#### Fluxo de Dados")
        st.markdown("""
        ```
        ┌─────────────────────────────────────┐
        │         BIOREATORES ORBITAIS         │
        │    ISS · LEO 408km · 27.600 km/h    │
        └──────────────┬──────────────────────┘
                       │ Telemetria
                       ▼
        ┌─────────────────────────────────────┐
        │         AZURE APP SERVICE           │
        │     orbitpharma.azurewebsites.net   │
        │         Python 3.12 + Streamlit     │
        └──────┬────────────────┬────────────┘
               │                │
               ▼                ▼
        ┌──────────────┐  ┌──────────────────┐
        │  KEY VAULT   │  │ APP. INSIGHTS    │
        │ kv-orbitpharma│  │  Telemetria +   │
        │  API Secrets │  │  Alert Rules     │
        └──────────────┘  └──────────────────┘
               │
               ▼
        ┌─────────────────────────────────────┐
        │         GITHUB ACTIONS CI/CD        │
        │   push → build → deploy (OIDC)     │
        └─────────────────────────────────────┘
        ```
        """)

    st.markdown("---")
    st.markdown("#### 🔒 Segurança (DevSecOps)")
    s1, s2, s3, s4 = st.columns(4)
    s1.success("✅ OIDC Ativo\nSem senhas estáticas")
    s2.success("✅ Key Vault\nSegredos isolados")
    s3.success("✅ RBAC\nPrivilégio mínimo")
    s4.success("✅ HTTPS\nTLS ativo")


# ═══════════════════════════════════════════════════════
# ABA 4 — STATUS DO PIPELINE
# ═══════════════════════════════════════════════════════
with tab4:
    st.markdown("### 🔄 Status do Pipeline CI/CD")

    p1, p2, p3 = st.columns(3)
    p1.metric("Total de Deploys", "3", "+1")
    p2.metric("Taxa de Sucesso", "66.7%", "2/3 runs")
    p3.metric("Último Deploy", "✅ Sucesso", "main branch")

    st.markdown("---")

    st.markdown("#### Histórico de Execuções")
    runs = [
        {"Run": "#3 — Add startup script", "Status": "✅ Sucesso", "Branch": "main", "Duração": "1m 40s", "Trigger": "push"},
        {"Run": "#2 — Refactor Azure workflow", "Status": "✅ Sucesso", "Branch": "main", "Duração": "2m 51s", "Trigger": "push"},
        {"Run": "#1 — Initial workflow config", "Status": "❌ Falhou", "Branch": "main", "Duração": "37s", "Trigger": "push"},
    ]
    import pandas as pd
    st.dataframe(pd.DataFrame(runs), use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("#### Estrutura do Workflow")
    st.markdown("""
    | Stage | Job | Duração Média |
    |-------|-----|---------------|
    | 1 | **Build** — checkout → setup Python → instalar deps → empacotar | ~30s |
    | 2 | **Deploy** — download artefato → login OIDC → deploy App Service | ~1m 40s |
    """)

    st.info("🔐 Autenticação via **OpenID Connect (OIDC)** — sem senhas estáticas no repositório.")


# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#546e7a; font-size:0.8rem; padding: 16px;'>
  🚀 <strong style='color:#4fc3f7;'>Orbit Pharma Labs</strong> · 
  FIAP — Engenharia de Software 4º Ano · Global Solution 2026 ·
  Sofia · Anna · Felipe · Gustavo · Gabriel
</div>
""", unsafe_allow_html=True)
