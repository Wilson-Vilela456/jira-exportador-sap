# Atualização SAP - Exportador de Tickets Jira

Projeto em Python com interface gráfica que realiza a exportação automatizada de tickets do Jira para Excel, com atualização incremental, log de execução e preservação de formatação.

## Funcionalidades

- Exportação dos tickets do projeto SAPS via API Jira
- Atualização das colunas `Descrição` e `Status` em um Excel existente
- Interface gráfica simples com botão de execução
- Segmentação da descrição em múltiplas colunas
- Geração de log CSV com estatísticas por execução
- Empacotamento como executável `.exe` com nome e ícone personalizado

## Como usar

1. Execute `Atualizacao SAP.exe`
2. Clique em "Executar Exportação"
3. Verifique o arquivo `jira_exportado_completo.xlsx` atualizado
4. Consulte o `log_execucao.csv` para ver quantos tickets foram adicionados ou alterados

## Estrutura do projeto

