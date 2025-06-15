# IIS - Revisão por Pares - Metodologia Ativa

## 📝 Descrição (PT-BR)

Este projeto foi desenvolvido para facilitar a **avaliação por pares entre grupos**, na disciplina **IIS - Metodologia Ativa**.

- 🔹 Um app permite que os alunos realizem avaliações de outros grupos.
- 🔹 Um app administrativo permite que o professor visualize, filtre e baixe os dados das avaliações.
- 🔹 Todos os dados são armazenados diretamente em uma planilha no **Google Sheets**, funcionando como banco de dados compartilhado.

---

## 🚀 Como Executar Localmente

1. Instale as dependências:
```bash
pip install streamlit pandas gspread google-auth
```

2. Tenha o arquivo de credenciais JSON da sua conta de serviço do Google.

3. Execute o app para os alunos:
```bash
streamlit run app.py
```

4. Ou execute o app administrativo:
```bash
streamlit run admin_app.py
```

---

## 🌐 Deploy no Streamlit Cloud

1. Crie um repositório no GitHub com estes arquivos.
2. No Streamlit Cloud 👉 https://streamlit.io/cloud, clique em **“New app”**.
3. Escolha:
- Para o formulário dos alunos: `app.py`.
- Para o painel administrativo: `admin_app.py`.
4. Adicione seu arquivo de credenciais JSON via **“Secrets”** no Streamlit (recomendado para segurança).
5. Clique em **Deploy**.

---

## 🔗 Banco de Dados

Os dados são armazenados diretamente na planilha:  
**`IIS - Revisão por Pares - 2025`**  
Na aba:  
**`Respostas`**

A planilha deve ser compartilhada com a conta de serviço gerada no Google Cloud, com permissão de **Editor**.

---

## 📦 Arquivos no Projeto

| Arquivo            | Descrição                                                       |
|--------------------|-----------------------------------------------------------------|
| `app.py`           | App de preenchimento para os alunos                            |
| `admin_app.py`     | App administrativo para visualização, filtros e download        |
| `requirements.txt` | Dependências (Streamlit, Pandas, GSpread, Google Auth)          |
| `README.md`        | Descrição do projeto                                            |
| `seu_arquivo.json` | Arquivo de credenciais do Google (não subir público no GitHub)  |

---

## 🔐 Segurança dos Dados

- 🔸 O banco de dados é uma planilha no Google Sheets, acessível **somente ao professor**, via credenciais da conta de serviço ou painel administrativo.
- 🔸 O acesso aos dados é restrito, seguro e controlado, garantindo a privacidade das avaliações.

---

# 🌍 IIS - Peer Review - Active Methodology

## 📝 Description (EN)

This project was developed to facilitate **peer review between groups** in the course **IIS - Active Methodology**.

- 🔹 One app allows students to evaluate other groups.
- 🔹 An admin app allows the teacher to view, filter, and download the evaluation data.
- 🔹 All data is stored directly in a **Google Sheets spreadsheet**, acting as the database.

---

## 🚀 How to Run Locally

1. Install dependencies:
```bash
pip install streamlit pandas gspread google-auth
```

2. Have the JSON credential file from your Google Service Account.

3. Run the student app:
```bash
streamlit run app.py
```

4. Or run the admin app:
```bash
streamlit run admin_app.py
```

---

## 🌐 Deploy on Streamlit Cloud

1. Create a GitHub repository with these files.
2. On Streamlit Cloud 👉 https://streamlit.io/cloud, click **“New app”**.
3. Select:
- For the student form: `app.py`.
- For the admin panel: `admin_app.py`.
4. Add your JSON credential file via **“Secrets”** (recommended for security).
5. Click **Deploy**.

---

## 🔗 Database

The data is stored in the spreadsheet:  
**`IIS - Revisão por Pares - 2025`**  
Sheet/tab name:  
**`Respostas`**

The spreadsheet must be shared with your Google Service Account email with **Editor** permissions.

---

## 📦 Project Files

| File               | Description                                                       |
|--------------------|-------------------------------------------------------------------|
| `app.py`           | Student app for submitting evaluations                            |
| `admin_app.py`     | Admin app for viewing, filtering, and downloading data            |
| `requirements.txt` | Dependencies (Streamlit, Pandas, GSpread, Google Auth)            |
| `README.md`        | Project description                                               |
| `your_credentials.json` | Google credentials file (do not upload publicly to GitHub) |

---

## 🔐 Data Security

- 🔸 The database is a Google Sheets spreadsheet, accessible **only to the teacher**, via the service account credentials or the admin panel.
- 🔸 Data access is restricted, secure, and controlled, ensuring privacy of the evaluations.
