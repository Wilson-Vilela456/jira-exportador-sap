# SCRIPT_SAP_JIRA

Exportador automatizado de tickets do Jira (projeto SAPS) para Excel, com logs, formatação e segurança.

## Funcionalidades

- Extração via API do Jira
- Exportação para Excel com segmentação de descrição
- Preserva formatação do Excel
- Logs em `.csv` e `.txt`
- Uso seguro de token via `.env`

## Como usar

1. Crie o arquivo `.env` com:

JIRA_API_TOKEN=seu_token_aqui

2. Instale as dependências:

pip install -r requirements.txt

3. Execute o script:

python main.py

## Estrutura

SCRIPT_SAP_JIRA/
├── main.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt

## Aviso

**Nunca envie o arquivo `.env` ou tokens para o GitHub.**

