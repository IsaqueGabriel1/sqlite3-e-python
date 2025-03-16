import sqlite3

def selectVendas():
    select = """
        SELECT 
            cliente.Nome_Cliente, venda.id_transacao, produto.Nome_Produto,venda.quantidade
        from cliente,produto,venda 
        where cliente.id_Cliente = venda.id_Cliente
    """
    con = sqlite3.connect("Floricultura.db")
    cur = con.cursor()
    resp = cur.execute(select)
    print(resp.fetchall())
    
    
selectVendas()    
    
