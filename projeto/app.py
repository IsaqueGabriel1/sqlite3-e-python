import sqlite3
from projeto.util.util import criarTabela,inserirDados,buscar,inserirDadosEspecial,criaTabelaDinamica,criarTabelaAparitDeString
from tabs_sql.crudFlori.crud import insertVendas
from tabs_sql.dados.dados import vendas

from projeto.tabs_sql.tabelas.sql import sql_cliente,sql_produtos,sql_venda
#criar/conectar com banco de dados
con = sqlite3.connect("Floricultura.db")

try:
    #cusor, consegue manipular os itens do banco de dados
    cur = con.cursor()
    #listaColunas = ("id_Produto","Nome_Produto","Tipo_Produto","Preco","Qtde_estoque")
    #res = criaTabelaDinamica("Produto",listaColunas,cur)
    #criarTabelaAparitDeString()
    #cur.execute(sql_cliente)
    #cur.execute(sql_venda)
    #cur.execute(sql_produtos)
    
    insertVendas(vendas,"Venda",cur,con)
    
    
    #con.commit()
except con.DatabaseError as erro:
    print("Erro no banco de dados {}".format(erro))
except:
    print("Houve um erro ao acessar/criar o banco")
    
    
con.close()