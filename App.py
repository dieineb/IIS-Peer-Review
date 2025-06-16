import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

st.set_page_config(page_title="IIS - Revisão por Pares", page_icon="📝")
st.title("📝 IIS - Revisão por Pares - Metodologia Ativa")

# Configurar credenciais
SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('nome_do_arquivo.json', scopes=SCOPE)
client = gspread.authorize(creds)

# Acessar a planilha e a aba
SHEET_NAME = "IIS - Revisão por Pares - 2025"
worksheet = client.open(SHEET_NAME).worksheet("Respostas")

# Lista dos grupos
grupos = [
    "3 - Robótica em Saúde",
    "4 - Games na Saúde",
    "5 - Inteligência Artificial na Saúde",
    "6 - Mobile Health",
    "7 - Processamento de Imagens Médicas",
    "8 - Processamento de Sinais Biológicos",
    "12 - Bioinformática",
    "99 - Grupo de Teste"
]

st.subheader("🔍 Identificação")
grupo_origem = st.selectbox("Seu grupo (quem faz a avaliação):", grupos)
grupo_destino = st.selectbox(
    "Grupo que você está avaliando:", 
    [g for g in grupos if g != grupo_origem]
)
titulo = st.text_input("Título do Trabalho Avaliado:")

st.subheader("🏆 Avaliação")

def criterio(nome, descricao):
    st.markdown(f"**{nome}**: {descricao}")
    return st.radio(
        f"Nota para {nome}",
        ["1 - Rejeição Forte", "2 - Rejeição", "3 - Rejeição Fraca",
         "4 - Neutro", "5 - Aceitação Fraca", "6 - Aceitar", "7 - Aceitação Forte"],
        horizontal=True
    )

originalidade = criterio("Originalidade", "Ideias novas, criativas, soluções originais?")
qualidade = criterio("Qualidade Técnica", "Conteúdo consistente, bem fundamentado?")
relevancia = criterio("Relevância", "Alinhado com os temas da disciplina?")
apresentacao = criterio("Apresentação", "Organização, uso de gráficos, clareza, referências?")
analise = criterio("Análise Crítica", "Há reflexão, discussão e profundidade no tema?")
recomendacao = criterio("Recomendação Final", "Avaliação geral do trabalho.")

st.subheader("💬 Comentários")
comentario_autores = st.text_area("Comentários para os autores (visível aos avaliados):")
comentario_professor = st.text_area("Comentários privados para o professor:")

if st.button("✅ Enviar Avaliação"):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dados = [
        data_hora, grupo_origem, grupo_destino, titulo,
        originalidade, qualidade, relevancia, apresentacao,
        analise, recomendacao, comentario_autores, comentario_professor
    ]
    worksheet.append_row(dados)
    st.success("✅ Avaliação enviada com sucesso!")
    st.toast("📥 Dados registrados na planilha.")
    #st.balloons()

