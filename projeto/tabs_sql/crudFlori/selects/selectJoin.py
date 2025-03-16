import sqlite3




def selectVendas():
    #traz a intercecção entre as tabelas de cliente e venda
    innerJon = """
        select c.Nome_Cliente, v.id_transacao,v.data_compra, v.Nota_fiscal, v.quantidade
        from cliente as c
        INNER JOIN venda as v
        where c.id_Cliente = v.id_Cliente
        """
        
    con = sqlite3.connect("Floricultura.db")
    cur = con.cursor()
    resp = cur.execute(innerJon)
    print(resp.fetchall())
    


def selectInnerJoinOrderCliente():
    #traz tudo da tabela de cliente, mesmo que n tenha na tabela venda
    query = """
    select * from cliente as c
    left join venda as v
    on c.id_Cliente = v.id_Cliente
    order by c.Nome_Cliente

    """
    con = sqlite3.connect("Floricultura.db")
    cur = con.cursor()
    resp = cur.execute(query)
    print(resp.fetchall())



def selectLeftExcludingJoin():
    query = """
    select * from 
    cliente as c
    left join venda as v
    on c.id_Cliente = v.id_Cliente
    where v.id_Cliente is null
    """
    con = sqlite3.connect("Floricultura.db")
    cur = con.cursor()
    resp = cur.execute(query)
    print(resp.fetchall())
    


def selectRightExcludingJoin():
    query = """
    select * from 
    cliente as c
    right join venda as v
    on c.id_Cliente = v.id_Cliente
    where v.id_Cliente is null
    """
    con = sqlite3.connect("Floricultura.db")
    cur = con.cursor()
    resp = cur.execute(query)
    print(resp.fetchall())



#selectLeftExcludingJoin()
selectRightExcludingJoin()
#selectInnerJoinOrderCliente()
#selectVendas()    