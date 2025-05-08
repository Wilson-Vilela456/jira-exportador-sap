# SCRIPT_SAP_JIRA

Exportador automatizado de tickets do Jira (projeto SAPS) para Excel, com logs, segmentação de descrição, preservação de formatação e uso seguro de credenciais.

## 🚀 Funcionalidades
- Extração via API do Jira (projeto SAPS)
- Exportação para Excel com formatação preservada
- Atualização automática das colunas `Descrição` e `Status`
- Segmentação da descrição em múltiplas colunas (`Descricao2` até `Descricao10`)
- Geração de logs em `.csv` e `.txt`
- Utilização de `.env` para proteger o token da API
- Preparado para empacotamento como `.exe` (via `pyinstaller`)

## 📦 Como usar
1. Crie um arquivo `.env` na raiz do projeto com:


2. Instale as dependências:


3. Execute o script:

> O script gerará o Excel `jira_exportado_completo.xlsx` com todos os dados e uma aba extra `Descricao_Segmentada`.

## 📁 Estrutura do projeto
jira-exportador-sap/
├── .gitignore
├── .env # (IGNORADO pelo Git)
├── README.md
├── requirements.txt
├── main.py # Script principal de exportação
├── venv/ # Ambiente virtual (IGNORADO)
├── dist/ # Build do .exe (IGNORADO)
├── build/ # Build intermediário (IGNORADO)
├── jira_exportado_completo.xlsx # GERADO automaticamente
├── log_execucao.csv # GERADO automaticamente
├── log_detalhado.txt # GERADO automaticamente
└── src/
└── Atualizacao SAP.spec # Script/Spec do executável


## ⚠️ Boas práticas
- Nunca envie arquivos sensíveis ou gerados (`.env`, `.xlsx`, `.csv`, `.txt`) para o GitHub — eles já estão protegidos no `.gitignore`.
- Use `python-dotenv` para carregar variáveis de ambiente com segurança.
- Após qualquer modificação no `.gitignore`, use:


Para garantir que o Git pare de rastrear o que deve ser ignorado.



