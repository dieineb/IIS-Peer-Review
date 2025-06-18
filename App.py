import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="IIS - Revisão por Pares", page_icon="📝")
st.title("📝 IIS - Revisão por Pares")

# 🔐 Configuração das credenciais via Secrets do Streamlit
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Ler as credenciais do arquivo de Secrets
creds_dict = st.secrets["gcp_service_account"]
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)

# Autenticar no Google Sheets
client = gspread.authorize(creds)

# Abrir a planilha e selecionar a aba
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
    "12 - Bioinformática"
   # "99 - Grupo de Teste"
]

st.subheader("👥 Identificação")
grupo_origem = st.selectbox("Seu grupo (quem faz a avaliação):", grupos)
grupo_destino = st.selectbox(
    "Grupo que você está avaliando:", 
    [g for g in grupos if g != grupo_origem]
)
titulo = st.text_input("Título do Trabalho Avaliado:")

st.subheader("✔️ Avaliação")

def criterio(nome, descricao):
    st.markdown(f"**{nome}**: {descricao}")
    return st.radio(
        f"Nota para {nome}",
        ["1 - Rejeição Forte", "2 - Rejeição", "3 - Rejeição Fraca",
         "4 - Neutro", "5 - Aceitação Fraca", "6 - Aceitar", "7 - Aceitação Forte"],
        horizontal=True
    )

originalidade = criterio("Originalidade", "O trabalho apresenta ideias novas, criativas, soluções originais ou perspectivas próprias sobre o tema?")
qualidade = criterio("Qualidade Técnica", "O conteúdo está bem estruturado, consistente, fundamentado teoricamente e metodologicamente adequado?")
relevancia = criterio("Relevância", "O trabalho está alinhado aos temas e objetivos da disciplina, contribuindo para a compreensão do assunto?")
apresentacao = criterio("Apresentação", "O texto é claro, bem organizado, com boa escrita, uso adequado de elementos como gráficos, tabelas, imagens, e referências corretamente aplicadas?")
analise = criterio("Análise Crítica", "O trabalho demonstra desenvolvimento consistente, reflexão, análise e aprofundamento sobre o tema, indo além da descrição superficial?")
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

