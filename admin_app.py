import streamlit as st
import pandas as pd
import os

# Configuração da página
st.set_page_config(page_title="Admin - Revisões por Pares", page_icon="🗂️")

st.title("🗂️ Admin - Visualização das Revisões por Pares")

CSV_FILE = "revisoes.csv"

# Verifica se o arquivo existe
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)

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

    # 📥 Download do CSV filtrado
    csv = df_filtrado.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 Baixar dados filtrados como CSV",
        data=csv,
        file_name='revisoes_filtradas.csv',
        mime='text/csv',
    )

    # 📊 Resumo
    st.subheader("📊 Resumo das Avaliações")
    st.write(f"Total de avaliações: {df.shape[0]}")
    st.write(f"Total de grupos avaliadores: {df['Grupo Avaliador'].nunique()}")
    st.write(f"Total de grupos avaliados: {df['Grupo Avaliado'].nunique()}")

else:
    st.warning("⚠️ Nenhuma revisão encontrada. O arquivo 'revisoes.csv' ainda não foi criado.")
