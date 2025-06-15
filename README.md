# IIS - Revisão por Pares - Metodologia Ativa

## 📝 Descrição (PT-BR)

Este projeto foi desenvolvido para facilitar a **avaliação por pares entre grupos**, na disciplina **IIS - Metodologia Ativa**.

- 🔹 Um app permite que os alunos realizem avaliações de outros grupos.
- 🔹 Um app administrativo permite que o professor visualize, filtre e baixe os dados das avaliações.
- 🔹 Todos os dados são armazenados localmente em um arquivo CSV chamado **`revisoes.csv`**.

---

## 🚀 Como Executar Localmente

1. Instale as dependências:
```bash
pip install streamlit pandas
```

2. Execute o app para os alunos:
```bash
streamlit run app.py
```

3. Ou execute o app administrativo:
```bash
streamlit run admin_app.py
```

---

## 🌐 Deploy no Streamlit Cloud

1. Crie um repositório no GitHub com estes arquivos.
2. Acesse 👉 https://streamlit.io/cloud.
3. Clique em **“New app”**.
4. Escolha:
- Para o formulário dos alunos: `app.py`.
- Para o painel administrativo: `admin_app.py`.
5. Clique em **Deploy**.

---

## 📦 Arquivos no Projeto

| Arquivo            | Descrição                                                       |
|--------------------|-----------------------------------------------------------------|
| `app.py`           | App de preenchimento para os alunos                            |
| `admin_app.py`     | App administrativo para visualização, filtros e download        |
| `requirements.txt` | Dependências (Streamlit + Pandas)                              |
| `README.md`        | Descrição do projeto                                            |
| `revisoes.csv`     | (Opcional) Dados das avaliações, criado automaticamente         |

---

## 🔐 Segurança dos Dados

- 🔸 O arquivo **`revisoes.csv`** é acessível **somente ao professor**, que possui acesso ao repositório ou ao painel administrativo.
- 🔸 O acesso aos dados é restrito e controlado, garantindo a privacidade das avaliações.

---

# 🌍 IIS - Peer Review - Active Methodology

## 📝 Description (EN)

This project was developed to facilitate **peer review between groups** in the course **IIS - Active Methodology**.

- 🔹 One app allows students to evaluate other groups.
- 🔹 An admin app allows the teacher to view, filter, and download the evaluation data.
- 🔹 All data is stored locally in a CSV file called **`revisoes.csv`**.

---

## 🚀 How to Run Locally

1. Install dependencies:
```bash
pip install streamlit pandas
```

2. Run the student app:
```bash
streamlit run app.py
```

3. Or run the admin app:
```bash
streamlit run admin_app.py
```

---

## 🌐 Deploy on Streamlit Cloud

1. Create a GitHub repository with these files.
2. Go to 👉 https://streamlit.io/cloud.
3. Click **“New app”**.
4. Select:
- For the student form: `app.py`.
- For the admin panel: `admin_app.py`.
5. Click **Deploy**.

---

## 📦 Project Files

| File               | Description                                                       |
|--------------------|-------------------------------------------------------------------|
| `app.py`           | Student app for submitting evaluations                            |
| `admin_app.py`     | Admin app for viewing, filtering, and downloading data            |
| `requirements.txt` | Dependencies (Streamlit + Pandas)                                 |
| `README.md`        | Project description                                               |
| `revisoes.csv`     | (Optional) Evaluations data, created automatically if not present |

---

## 🔐 Data Security

- 🔸 The **`revisoes.csv`** file is accessible **only to the teacher**, who has access to the repository or the admin panel.
- 🔸 Data access is restricted and controlled, ensuring the privacy of the evaluations.
