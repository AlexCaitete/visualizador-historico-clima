# 📊 Visualizador de Histórico Climático (SQL + Python)

Este projeto atua como o **Módulo de Visualização** de um pipeline de dados climáticos. Ele é responsável por conectar-se a um banco de dados relacional (`SQLite`), executar consultas de leitura (`SELECT`) e formatar os dados brutos em uma interface tabular legível para o usuário final.

## 🔌 Integração e Dependência

Este sistema foi projetado para ler dados gerados pelo **Módulo de Ingestão**. Para que este visualizador funcione, você precisa ter o banco de dados populado pelo projeto de consulta:

👉 **[Acesse o Gerador de Dados Climáticos AQUI]([])**

*O fluxo de dados funciona assim:*
1. **Consultor (Outro Repo):** Consome API -> Salva no SQLite.
2. **Visualizador (Este Repo):** Lê do SQLite -> Formata no Terminal.

## 🚀 Funcionalidades

- **Leitura de Banco de Dados:** Conexão com `SQLite3` para extração de dados.
- **Formatação Tabular:** Uso de f-strings avançadas para alinhamento dinâmico de colunas.
- **Tratamento de Strings:** Ajuste de espaçamento para leitura confortável de dados variáveis (ex: nomes de cidades longos).

## 🛠️ Tecnologias

- **Python 3.12+**
- **SQLite3**
- **Data Visualization** (Terminal-based)

## 📦 Como usar

### 1. Pré-requisito
Certifique-se de ter o arquivo `historico_clima.db` na mesma pasta do script. Esse arquivo é gerado automaticamente ao rodar o projeto "Consultor Climático".

### 2. Execução
```bash
python ver_historico.py
