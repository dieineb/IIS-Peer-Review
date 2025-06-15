import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuração da página
st.set_page_config(page_title="IIS - Revisão por Pares", page_icon="📝")

st.title("📝 IIS - Revisão por Pares - Metodologia Ativa")

# Arquivo CSV para armazenamento
CSV_FILE = "revisoes.csv"

# Lista dos grupos (incluindo grupo de teste)
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

# Formulário
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
    dados = {
        "Data/Hora": data_hora,
        "Grupo Avaliador": grupo_origem,
        "Grupo Avaliado": grupo_destino,
        "Título do Trabalho": titulo,
        "Originalidade": originalidade,
        "Qualidade": qualidade,
        "Relevância": relevancia,
        "Apresentação": apresentacao,
        "Análise Crítica": analise,
        "Recomendação Final": recomendacao,
        "Comentários para Autores": comentario_autores,
        "Comentários para Professor": comentario_professor
    }

    # Verifica se o CSV já existe
    if os.path.exists(CSV_FILE):
        df_existente = pd.read_csv(CSV_FILE)
        df = pd.concat([df_existente, pd.DataFrame([dados])], ignore_index=True)
    else:
        df = pd.DataFrame([dados])

    df.to_csv(CSV_FILE, index=False)

    st.success("✅ Avaliação enviada e salva no arquivo CSV!")
    st.balloons()
