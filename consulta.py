import psycopg2

# Dados da conexão 
conn = psycopg2.connect(
    host="localhost",
    database="vendas_db",
    user="postgres",
    password="55728246"
)

cur = conn.cursor()

cur.execute("SELECT * FROM vendas LIMIT 5;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
