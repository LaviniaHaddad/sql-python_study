# 📊 Análise de Vendas com PostgreSQL e Streamlit

Este projeto combina **SQL** e **Python** para análise exploratória de dados de vendas. A base foi criada manualmente com PostgreSQL e visualizada de forma interativa usando **Streamlit** e **Plotly**.

---

## 🗃️ Sobre o Projeto

- Os dados foram inseridos diretamente em um banco de dados PostgreSQL, simulando uma tabela real de vendas (`vendas`).
- A análise é realizada em Python, conectando-se ao banco via `psycopg2` e `pandas`.
- O front-end foi construído com `Streamlit`, permitindo filtros e gráficos dinâmicos com Plotly.

---

## 🧱 Estrutura da Tabela (`vendas`)

| Coluna      | Tipo       | Descrição                          |
|-------------|------------|------------------------------------|
| invoiceno   | TEXT       | Número da nota fiscal              |
| stockcode   | TEXT       | Código do produto                  |
| description | TEXT       | Descrição do produto               |
| quantity    | INTEGER    | Quantidade vendida                 |
| price       | NUMERIC    | Preço unitário                     |
| country     | TEXT       | País da venda                      |
| sale_date   | DATE       | Data da venda                      |

---

## 📌 Funcionalidades do App

- **Resumo geral das vendas**
- **Vendas por país**
- **Total de vendas por mês**
- **Produtos mais vendidos**
- **Filtros por país e intervalo de datas**

---

## ▶️ Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/laviniahaddad/sql-python-vendas.git
cd sql-python-vendas

2. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt

3. Crie o banco PostgreSQL
Abra o pgAdmin ou outro gerenciador.

Crie um banco chamado projeto_vendas.

Execute o script vendas.sql para criar a tabela e inserir os dados.

4. Configure a conexão no app.py
Altere os dados de conexão:

python
Copiar
Editar
conn_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'projeto_vendas',
    'user': 'seu_usuario',
    'password': 'sua_senha'
}
5. Rode o app Streamlit
bash
Copiar
Editar
streamlit run app.py
🧰 Tecnologias Utilizadas
Python 3.x

PostgreSQL

Streamlit

Pandas

Plotly

psycopg2

💡 Objetivo
Este projeto foi desenvolvido com fins educacionais e de portfólio, combinando habilidades em banco de dados (SQL), análise de dados em Python e visualização com dashboards interativos.
