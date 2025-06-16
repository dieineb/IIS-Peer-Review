import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# 🔐 CONFIGURAÇÃO DE CREDENCIAIS
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# LER AS CREDENCIAIS DO SECRETS
creds_dict = st.secrets["gcp_service_account"]
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)

# AUTENTICAR COM GOOGLE SHEETS
client = gspread.authorize(creds)

# ACESSAR A PLANILHA E A ABA
SHEET_NAME = "IIS - Revisão por Pares - 2025"
worksheet = client.open(SHEET_NAME).worksheet("Respostas")

# 🔍 LER OS DADOS DA PLANILHA
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# 🔧 CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Admin - Revisão por Pares", page_icon="🗂️")
st.title("🗂️ Admin - Revisão por Pares - Metodologia Ativa")

# 📄 EXIBIR OS DADOS
st.subheader("📑 Dados das Revisões")
st.dataframe(df)

# 🔍 FILTROS
st.subheader("🔍 Filtros")

grupos_avaliadores = df["Grupo Avaliador"].unique()
grupo_avaliador = st.selectbox("Filtrar por Grupo Avaliador:", ["Todos"] + sorted(grupos_avaliadores))

grupos_avaliados = df["Grupo Avaliado"].unique()
grupo_avaliado = st.selectbox("Filtrar por Grupo Avaliado:", ["Todos"] + sorted(grupos_avaliados))

df_filtrado = df.copy()

if grupo_avaliador != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Grupo Avaliador"] == grupo_avaliador]

if grupo_avaliado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Grupo Avaliado"] == grupo_avaliado]

# 📄 EXIBIR OS DADOS FILTRADOS
st.subheader("📄 Dados Filtrados")
st.dataframe(df_filtrado)

# 📥 BOTÃO DE DOWNLOAD DO CSV
csv = df_filtrado.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Baixar dados como CSV",
    data=csv,
    file_name='revisoes_filtradas.csv',
    mime='text/csv',
)

# 📊 RESUMO DAS AVALIAÇÕES
st.subheader("📊 Resumo das Avaliações")
st.write(f"Total de avaliações: {df.shape[0]}")
st.write(f"Total de grupos avaliadores: {df['Grupo Avaliador'].nunique()}")
st.write(f"Total de grupos avaliados: {df['Grupo Avaliado'].nunique()}")
