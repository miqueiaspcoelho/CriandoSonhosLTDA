import sqlite3

# Conecta (ou cria) o banco de dados SQLite
conn = sqlite3.connect("pizzamais.db")
cursor = conn.cursor()

# Criação da tabela Pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedidos (
    IdPedido INTEGER PRIMARY KEY,
    Status VARCHAR(30) NOT NULL,
    Delivery BOOLEAN,
    Endereco VARCHAR(100),
    Data DATE,
    ValorTotal REAL NOT NULL
);
""")

# Criação da tabela Itens
cursor.execute("""
CREATE TABLE IF NOT EXISTS Itens (
    IdItens INTEGER PRIMARY KEY,
    Nome VARCHAR(30),
    Preco REAL,
    Tipo VARCHAR(30),
    Descricao VARCHAR(255),
    CONSTRAINT Produto_Unique UNIQUE (Nome)
);
""")

# Criação da tabela ItensPedidos (relacionamento N:N)
cursor.execute("""
CREATE TABLE IF NOT EXISTS ItensPedidos (
    Id INTEGER PRIMARY KEY,
    IdPedido INTEGER NOT NULL,
    IdItem INTEGER NOT NULL,
    FOREIGN KEY (IdPedido) REFERENCES Pedidos(IdPedido),
    FOREIGN KEY (IdItem) REFERENCES Itens(IdItens)
);
""")

# Confirma e fecha a conexão
conn.commit()
conn.close()

print("Tabelas criadas com sucesso!")
