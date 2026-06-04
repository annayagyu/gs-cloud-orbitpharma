import streamlit as st
import random
import math
import pandas as pd

st.set_page_config(
    page_title="Orbit Pharma Labs",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
  .stApp { background-color: #0a0e1a; color: #e0e6f0; }
  [data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1b2a 0%, #1a2744 100%);
    border-right: 1px solid #1e3a5f;
  }
  h1, h2, h3 { color: #4fc3f7 !important; }
  [data-testid="metric-container"] {
    background: linear-gradient(135deg, #0d1b2a, #1a2744);
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 16px;
  }
  [data-testid="stMetricValue"] { color: #4fc3f7 !important; font-size: 2rem !important; }
  [data-testid="stMetricDelta"] { color: #81c784 !important; }
  .stTabs [data-baseweb="tab-list"] { background-color: #0d1b2a; border-radius: 8px; }
  .stTabs [data-baseweb="tab"] { color: #90caf9; }
  .stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: #1e3a5f;
    color: #4fc3f7 !important;
    border-radius: 6px;
  }
  .stAlert { border-radius: 10px; }
  hr { border-color: #1e3a5f; }
  .stDataFrame { border: 1px solid #1e3a5f; border-radius: 8px; }
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
  .badge-red    { background: #b71c1c; color: #ef9a9a; border: 1px solid #c62828; }
  .custom-card {
    background: linear-gradient(135deg, #0d1b2a, #1a2744);
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 20px;
    margin: 8px 0;
  }
  .kpi-label { font-size: 0.85rem; color: #90a4ae; text-transform: uppercase; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## Orbit Pharma Labs")
    st.markdown("**Missao:** Cristalizacao de proteinas em microgravidade orbital")
    st.markdown("---")

    st.markdown("### Status da Missao")
    st.markdown('<span class="badge badge-green">SISTEMA OPERACIONAL</span>', unsafe_allow_html=True)
    st.markdown('<span class="badge badge-blue">ISS LINK ATIVO</span>', unsafe_allow_html=True)
    st.markdown('<span class="badge badge-green">AZURE CLOUD OK</span>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Satelite Ativo")
    st.markdown("**Orbita:** LEO — 408 km")
    st.markdown("**Inclinacao:** 51.6°")
    st.markdown("**Velocidade:** 27.600 km/h")
    st.markdown("**Periodo orbital:** 92.68 min")

    st.markdown("---")
    st.markdown("### Equipe")
    st.markdown("""
- Sofia Amorim Coutinho — RM 552534
- Anna Yagyu — RM 550360
- Felipe Capriotti da Silva Santos — RM 098460
- Gustavo Kawamura Christofani — RM 099679
- Gabriel Pacheco — RM 550191
    """)
    st.markdown("**FIAP — ESPX 4° Ano — 2026**")


# ── Header ───────────────────────────────────────────────────
st.markdown("""
<div style='background: linear-gradient(135deg, #0d1b2a, #1a2744);
            border: 1px solid #1e3a5f; border-radius: 16px;
            padding: 32px; margin-bottom: 24px; text-align: center;'>
  <h1 style='color: #4fc3f7; font-size: 2.4rem; margin: 0;'>Orbit Pharma Labs</h1>
  <p style='color: #90caf9; font-size: 1.1rem; margin: 8px 0 0 0;'>
    Plataforma de Controle e Monitoramento de Bioreatores Orbitais
  </p>
  <p style='color: #546e7a; font-size: 0.9rem; margin: 4px 0 0 0;'>
    Cristalizacao de proteinas em microgravidade · Azure Cloud · CI/CD Automatizado
  </p>
</div>
""", unsafe_allow_html=True)


# ── KPIs Globais ─────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
k1.metric("Pureza do Cristal (IA)", "94.3%", "+0.8%")
k2.metric("Temperatura Reator", "37.2 C", "Estavel")
k3.metric("pH do Fluido", "7.41", "-0.02")
k4.metric("Uptime Azure", "99.97%", "+0.01%")

st.markdown("---")


# ── Abas ─────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "Sobre o Projeto",
    "Dashboard de Telemetria",
    "Arquitetura Cloud",
    "Status do Pipeline"
])


# ═══════════════════════════════════════════════════════
# ABA 1 — SOBRE O PROJETO
# ═══════════════════════════════════════════════════════
with tab1:
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("### O Problema Espacial")
        st.markdown("""
A cristalizacao de proteinas em **microgravidade** (como na ISS a 408 km de altitude)
elimina os efeitos de conveccao e sedimentacao, permitindo o crescimento de cristais
**perfeitamente simetricos e puros** — estruturalmente impossiveis de replicar na Terra.

Esses cristais aceleram a descoberta de tratamentos para doencas como:
- Cancer e doencas autoimunes
- Alzheimer e Parkinson
- Resistencia a antibioticos

**O desafio:** latencia de comunicacao, custo severo de telemetria e
sensibilidade a microvibracoes tornam o monitoramento tradicional inviavel.
        """)

    with col_b:
        st.markdown("### Nossa Solucao")
        st.markdown("""
A **Orbit Pharma Labs** opera uma plataforma SaaS em nuvem (Microsoft Azure)
que conecta bioreatores em orbita baixa a algoritmos de IA em tempo real.

**Stack tecnologico:**
        """)
        st.markdown("""
| Camada | Tecnologia |
|--------|-----------|
| Cloud | Azure App Service + Key Vault |
| CI/CD | GitHub Actions (OIDC) |
| Backend | Python 3.12 + Streamlit |
| IA | Modelos preditivos de pureza cristalina |
| Monitoramento | Application Insights + Alert Rules |
| Seguranca | RBAC + DevSecOps |
        """)

    st.markdown("---")

    col_c, col_d, col_e = st.columns(3)
    with col_c:
        st.markdown("""
        <div class='custom-card' style='text-align:center;'>
          <div class='kpi-label'>ODS Alinhado</div>
          <div style='color:#4fc3f7; font-weight:bold; font-size:1.1rem;'>ODS 9</div>
          <div style='color:#90a4ae; font-size:0.85rem;'>Industria, Inovacao e Infraestrutura</div>
        </div>
        """, unsafe_allow_html=True)
    with col_d:
        st.markdown("""
        <div class='custom-card' style='text-align:center;'>
          <div class='kpi-label'>Altitude Orbital</div>
          <div style='color:#4fc3f7; font-weight:bold; font-size:1.1rem;'>408 km</div>
          <div style='color:#90a4ae; font-size:0.85rem;'>Orbita Baixa Terrestre (LEO)</div>
        </div>
        """, unsafe_allow_html=True)
    with col_e:
        st.markdown("""
        <div class='custom-card' style='text-align:center;'>
          <div class='kpi-label'>Experimentos Ativos</div>
          <div style='color:#4fc3f7; font-weight:bold; font-size:1.1rem;'>3 Bioreatores</div>
          <div style='color:#90a4ae; font-size:0.85rem;'>Missao Orbital Ativa</div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# ABA 2 — DASHBOARD DE TELEMETRIA
# ═══════════════════════════════════════════════════════
with tab2:
    st.markdown("### Telemetria em Tempo Real (Dados Simulados)")
    st.caption("Metricas consolidadas do pipeline de dados e das analises preditivas de IA orbital.")

    st.success("Sistema Nominal — Nenhuma microvilbracao destrutiva detectada nas ultimas 6 horas.")

    st.markdown("---")
    st.markdown("#### Status dos Bioreatores")
    b1, b2, b3 = st.columns(3)

    bioreatores = [
        {"id": "BR-01", "proteina": "Insulina Cristalina", "pureza": 94.3, "temp": 37.2, "ph": 7.41, "status": "Nominal"},
        {"id": "BR-02", "proteina": "Hemoglobina S",       "pureza": 88.7, "temp": 36.8, "ph": 7.38, "status": "Nominal"},
        {"id": "BR-03", "proteina": "Lisozima Pura",       "pureza": 97.1, "temp": 37.5, "ph": 7.44, "status": "Otimo"},
    ]

    for col, br in zip([b1, b2, b3], bioreatores):
        badge_color = "badge-green" if br["status"] in ["Nominal", "Otimo"] else "badge-red"
        col.markdown(f"""
        <div class='custom-card'>
          <div style='font-size:1.3rem; font-weight:bold; color:#4fc3f7;'>{br["id"]}</div>
          <div style='color:#90a4ae; font-size:0.8rem; margin-bottom:8px;'>{br["proteina"]}</div>
          <div style='font-size:1.8rem; font-weight:bold; color:#81c784;'>{br["pureza"]}%</div>
          <div style='color:#90a4ae; font-size:0.75rem;'>Pureza cristalina</div>
          <div style='margin-top:8px;'>
            <span style='color:#b0bec5;'>Temp: {br["temp"]}C</span> &nbsp;
            <span style='color:#b0bec5;'>pH: {br["ph"]}</span>
          </div>
          <div style='margin-top:8px;'>
            <span class='badge {badge_color}'>{br["status"]}</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Metricas do Sistema")
    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Latencia API", "142 ms", "-8 ms")
    m2.metric("Pacotes Recebidos", "1.847", "+23")
    m3.metric("Erros de Telemetria", "0", "0")
    m4.metric("CPU Azure", "12%", "-3%")
    m5.metric("Memoria", "487 MB", "+12 MB")

    st.markdown("---")
    st.markdown("#### Historico de Pureza Cristalina (Ultimas 24h)")

    horas = list(range(24))
    dados = {
        "Hora":    [f"{h:02d}:00" for h in horas],
        "BR-01 (%)": [round(93 + math.sin(h * 0.4) * 1.5 + random.uniform(-0.2, 0.2), 2) for h in horas],
        "BR-02 (%)": [round(87 + math.sin(h * 0.3) * 1.2 + random.uniform(-0.2, 0.2), 2) for h in horas],
        "BR-03 (%)": [round(96 + math.sin(h * 0.5) * 0.8 + random.uniform(-0.1, 0.1), 2) for h in horas],
    }
    df = pd.DataFrame(dados).set_index("Hora")
    st.line_chart(df, height=280)

    st.markdown("---")
    st.warning("Proxima janela de comunicacao com ISS: em 47 minutos (orbita #8.234)")


# ═══════════════════════════════════════════════════════
# ABA 3 — ARQUITETURA CLOUD
# ═══════════════════════════════════════════════════════
with tab3:
    st.markdown("### Arquitetura da Infraestrutura Azure")

    col_arch1, col_arch2 = st.columns([1, 1])

    with col_arch1:
        st.markdown("#### Componentes Provisionados")
        componentes = [
            ("Azure App Service",   "orbitpharma",    "Python 3.12 · Linux · SKU F1"),
            ("Azure Key Vault",     "kv-orbitpharma", "RBAC · Soft-delete 90d"),
            ("Application Insights","orbitpharma",    "Telemetria · Alertas · Metricas"),
            ("Resource Group",      "rg-orbitpharma", "East US · Azure for Students"),
        ]
        for nome, recurso, desc in componentes:
            st.markdown(f"""
            <div class='custom-card' style='padding:14px;'>
              <strong style='color:#4fc3f7;'>{nome}</strong>
              <code style='color:#90caf9; margin-left:8px;'>{recurso}</code>
              <br><span style='color:#90a4ae; font-size:0.82rem;'>{desc}</span>
            </div>
            """, unsafe_allow_html=True)

    with col_arch2:
        st.markdown("#### Fluxo de Dados")
        st.markdown("""
```
+-------------------------------------+
|       BIOREATORES ORBITAIS          |
|   ISS · LEO 408km · 27.600 km/h    |
+----------------+--------------------+
                 | Telemetria
                 v
+-------------------------------------+
|        AZURE APP SERVICE            |
|   orbitpharma.azurewebsites.net     |
|       Python 3.12 + Streamlit       |
+------+-----------------+-----------+
       |                 |
       v                 v
+--------------+  +------------------+
|  KEY VAULT   |  | APP. INSIGHTS    |
| kv-orbitpharma|  | Telemetria +    |
|  API Secrets |  | Alert Rules      |
+--------------+  +------------------+
       |
       v
+-------------------------------------+
|       GITHUB ACTIONS CI/CD          |
|  push -> build -> deploy (OIDC)     |
+-------------------------------------+
```
        """)

    st.markdown("---")
    st.markdown("#### Seguranca (DevSecOps)")
    s1, s2, s3, s4 = st.columns(4)
    s1.success("OIDC Ativo — Sem senhas estaticas")
    s2.success("Key Vault — Segredos isolados")
    s3.success("RBAC — Privilegio minimo")
    s4.success("HTTPS — TLS ativo")


# ═══════════════════════════════════════════════════════
# ABA 4 — STATUS DO PIPELINE
# ═══════════════════════════════════════════════════════
with tab4:
    st.markdown("### Status do Pipeline CI/CD")

    p1, p2, p3 = st.columns(3)
    p1.metric("Total de Deploys", "8", "+1")
    p2.metric("Taxa de Sucesso", "87.5%", "7/8 runs")
    p3.metric("Ultimo Deploy", "Sucesso", "main branch")

    st.markdown("---")
    st.markdown("#### Historico de Execucoes")

    runs = [
        {"Run": "#8 — Enhance app layout", "Status": "Sucesso", "Branch": "main", "Duracao": "3m 57s"},
        {"Run": "#7 — Remove environment block", "Status": "Sucesso", "Branch": "main", "Duracao": "2m 10s"},
        {"Run": "#6 — Fix env variable", "Status": "Sucesso", "Branch": "main", "Duracao": "2m 05s"},
        {"Run": "#5 — Improve YAML pipeline", "Status": "Falhou", "Branch": "main", "Duracao": "12s"},
        {"Run": "#4 — Update workflow", "Status": "Sucesso", "Branch": "main", "Duracao": "2m 30s"},
        {"Run": "#3 — Add startup script", "Status": "Sucesso", "Branch": "main", "Duracao": "1m 40s"},
        {"Run": "#2 — Refactor Azure workflow", "Status": "Sucesso", "Branch": "main", "Duracao": "2m 51s"},
        {"Run": "#1 — Initial workflow config", "Status": "Falhou", "Branch": "main", "Duracao": "37s"},
    ]
    st.dataframe(pd.DataFrame(runs), use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("#### Estrutura do Workflow")
    st.markdown("""
| Stage | Job | Duracao Media |
|-------|-----|---------------|
| 1 | Build — checkout, setup Python, instalar deps, empacotar | ~30s |
| 2 | Deploy — download artefato, login OIDC, deploy App Service | ~3m |
    """)
    st.info("Autenticacao via OpenID Connect (OIDC) — sem senhas estaticas no repositorio.")


# ── Footer ────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#546e7a; font-size:0.8rem; padding: 16px;'>
  <strong style='color:#4fc3f7;'>Orbit Pharma Labs</strong> ·
  FIAP — ESPX 4° Ano · Global Solution 2026 ·
  Sofia · Anna · Felipe · Gustavo · Gabriel
</div>
""", unsafe_allow_html=True)
