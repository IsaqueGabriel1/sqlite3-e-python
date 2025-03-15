import sqlite3

def insertVendas(dados,nomeTab,cur:sqlite3.Cursor,con):
    query = """
            INSERT INTO Venda (id_Cliente, id_Produto, Nota_fiscal, data_compra, quantidade) VALUES
                (?,?,?,?,?)
            """.format(dados)
    cur.executemany(query,dados)
    con.commit()
    resp = cur.execute("SELECT * FROM VENDA")
    print(resp)
    
    con.close()  