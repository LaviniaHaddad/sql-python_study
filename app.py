import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

conn_params = {
    'host': 'localhost',
    'dbname': 'vendas_db',
    'user': 'postgres',
    'password': '55728246',
    'port': 5432
}

def run_query(query, params=None):
    with psycopg2.connect(**conn_params) as conn:
        return pd.read_sql(query, conn, params=params)

st.title("Dashboard Interativo de Vendas")

# --- Sidebar filtros ---
st.sidebar.header("Filtros")

# Data mínima e máxima da base para controle
query_min_max_date = "SELECT MIN(invoicedate) as min_date, MAX(invoicedate) as max_date FROM vendas;"
df_date = run_query(query_min_max_date)
min_date = df_date['min_date'][0]
max_date = df_date['max_date'][0]

start_date = st.sidebar.date_input("Data inicial", min_date)
end_date = st.sidebar.date_input("Data final", max_date)

# Países disponíveis
query_paises = "SELECT DISTINCT country FROM vendas ORDER BY country;"
df_paises = run_query(query_paises)
paises = df_paises['country'].tolist()
pais_selecionado = st.sidebar.multiselect("País(es)", paises, default=paises)

# Cliente
query_clientes = "SELECT DISTINCT customerid FROM vendas WHERE customerid IS NOT NULL ORDER BY customerid;"
df_clientes = run_query(query_clientes)
clientes = df_clientes['customerid'].tolist()
cliente_selecionado = st.sidebar.multiselect("Cliente(s)", clientes, default=[])

# Formatar datas para SQL
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# --- Query principal para filtro geral ---
query_base = """
SELECT * FROM vendas
WHERE invoicedate::date BETWEEN %s AND %s
AND country = ANY(%s)
"""

params = [start_date_str, end_date_str, pais_selecionado]

if cliente_selecionado:
    query_base += " AND customerid = ANY(%s)"
    params.append(cliente_selecionado)

df_filtered = run_query(query_base, params)

st.write(f"### Dados filtrados: {len(df_filtered)} registros")

# --- Gráfico: Vendas totais por mês ---
df_filtered['month'] = pd.to_datetime(df_filtered['invoicedate']).dt.to_period('M').dt.to_timestamp()

df_vendas_mes = (
    df_filtered.groupby('month')
    .apply(lambda x: (x['quantity'] * x['unitprice']).sum())
    .reset_index(name='total_sales')
)

fig1 = px.line(df_vendas_mes, x='month', y='total_sales', title='Vendas Totais por Mês')
st.plotly_chart(fig1)

# --- Gráfico: Vendas por país ---
df_vendas_pais = (
    df_filtered.groupby('country')
    .apply(lambda x: (x['quantity'] * x['unitprice']).sum())
    .reset_index(name='total_sales')
    .sort_values(by='total_sales', ascending=False)
)

fig2 = px.bar(df_vendas_pais, x='country', y='total_sales', title='Vendas Totais por País')
st.plotly_chart(fig2)

# --- Produtos mais vendidos (Top 10) ---
df_produtos_top = (
    df_filtered.groupby('stockcode')
    .agg({'quantity': 'sum', 'description': 'first'})
    .reset_index()
    .sort_values(by='quantity', ascending=False)
    .head(10)
)

fig3 = px.bar(df_produtos_top, x='description', y='quantity', title='Top 10 Produtos Mais Vendidos')
st.plotly_chart(fig3)

# --- Quantidade de devoluções ---
devolucoes = df_filtered[df_filtered['quantity'] < 0]['quantity'].abs().sum()
st.write(f"### Quantidade total de devoluções: {devolucoes}")

# --- Ticket médio ---
df_filtered['total_value'] = df_filtered['quantity'] * df_filtered['unitprice']
ticket_medio = df_filtered.groupby('invoiceno')['total_value'].sum().mean()
st.write(f"### Ticket médio por compra: R$ {ticket_medio:.2f}")

# --- Vendas por dia da semana ---
df_filtered['weekday'] = pd.to_datetime(df_filtered['invoicedate']).dt.day_name()

df_vendas_semana = (
    df_filtered.groupby('weekday')
    .apply(lambda x: (x['quantity'] * x['unitprice']).sum())
    .reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    .reset_index(name='total_sales')
)

fig4 = px.bar(df_vendas_semana, x='weekday', y='total_sales', title='Vendas por Dia da Semana')
st.plotly_chart(fig4)