import sqlite3

# Conectar ao banco de dados (o mesmo que você criou anteriormente)
conn = sqlite3.connect("pizzamais.db")
cursor = conn.cursor()

# Consulta as tabelas existentes
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

print("Tabelas encontradas no banco:")
for t in tabelas:
    print("-", t[0])

# Fecha a conexão
conn.close()
