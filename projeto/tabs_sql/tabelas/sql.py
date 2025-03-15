sql_cliente = """

CREATE TABLE Cliente (
    id_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    RG VARCHAR(12) NOT NULL,
    Nome_Cliente VARCHAR(30) NOT NULL,
    Sobrenome VARCHAR(30) NOT NULL,
    Telefone VARCHAR(12),
    Rua VARCHAR(40),
    Numero VARCHAR(5),
    Bairro VARCHAR(25)
);

"""

sql_venda = """

CREATE TABLE Venda (
    id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_Cliente INTEGER NOT NULL,
    id_Produto INTEGER NOT NULL,
    Nota_fiscal SMALLINT NOT NULL,
    data_compra DATETIME,
    quantidade SMALLINT NOT NULL,
    FOREIgn KEY (id_Cliente) REFERENCES Clientes(id_Cliente),
    FOREIgn KEY (id_Produto) REFERENCES Produto(id_Produto)
);


"""

sql_produtos = """

CREATE TABLE Produto (
    id_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Produto VARCHAR(30) NOT NULL,
    Tipo_Produto VARCHAR(25) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Qtde_estoque SMALLINT NOT NULL
);


"""