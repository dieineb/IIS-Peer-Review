import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Admin - Revisões por Pares", page_icon="🗂️")
st.title("🗂️ Admin - Visualização das Revisões por Pares")

# Configurar credenciais
SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('nome_do_arquivo.json', scopes=SCOPE)
client = gspread.authorize(creds)

# Acessar a planilha e a aba
SHEET_NAME = "IIS - Revisão por Pares - 2025"
worksheet = client.open(SHEET_NAME).worksheet("Respostas")

# Ler os dados da planilha
data = worksheet.get_all_records()
df = pd.DataFrame(data)

st.subheader("📑 Dados das Revisões")
st.dataframe(df)

# 🔍 Filtros
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

st.subheader("📄 Dados Filtrados")
st.dataframe(df_filtrado)

# 📥 Download do CSV
csv = df_filtrado.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Baixar dados como CSV",
    data=csv,
    file_name='revisoes_filtradas.csv',
    mime='text/csv',
)

# 📊 Resumo
st.subheader("📊 Resumo das Avaliações")
st.write(f"Total de avaliações: {df.shape[0]}")
st.write(f"Total de grupos avaliadores: {df['Grupo Avaliador'].nunique()}")
st.write(f"Total de grupos avaliados: {df['Grupo Avaliado'].nunique()}")
