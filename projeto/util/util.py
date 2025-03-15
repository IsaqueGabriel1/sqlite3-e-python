import sqlite3

#cria tabela no sqlite3
def inserirDados(value1,value2,value3,cur:sqlite3.Cursor,con):
    query = """
            INSERT INTO filme values
            ('{}','{}','{}')
            """.format(value1,value2,value3)
    cur.execute(query)
    con.commit()
    con.close()

def inserirDadosEspecial(dados,nomeTab,cur:sqlite3.Cursor,con):
    query = """
            INSERT INTO {} (titulo,ano,duracao) values
            (?,?,?)
            """.format(nomeTab)
    cur.executemany(query,dados)
    con.commit()
    con.close()   
    

def buscar(value1,cur:sqlite3.Cursor):
    query = """
            SELECT {} from Cliente
            """.format(value1)
    res = cur.execute(query)
    print(res.fetchall())



def insertWithContext(dados,cur:sqlite3.Cursor,con):
    try:
        with con:
            con.executemany("INSERT INTO filme (titulo,ano,duracao) values (?,?,?)",dados)
            res = cur.execute("SELECT titulo from filme")
            print(res.fetchall())
    except:
        print("Banco de dados não acessivel")


def criarTabela(nomeTab,cur:sqlite3.Cursor):
    #query de criacao
    query = "CREATE TABLE {}(titulo,ano,duracao)".format(nomeTab)
    #executa a query
    try:
        cur.execute(query)
    except SyntaxError:
        return SyntaxError.msg
    #verifica se a tabela master está diferente de vazia
    res = cur.execute("SELECT name FROM sqlite_master") 
    respTupla = res.fetchall()
    for info in respTupla:
        if info[0] == nomeTab:
            return  info[0]
        
def insertDinamico(dados,nomeTab,coluns,cur:sqlite3.Cursor,con):
    query = """
            INSERT INTO {} (titulo,ano,duracao) values
            (?,?,?)
            """.format(nomeTab)
    cur.executemany(query,dados)
    con.commit()
    con.close()   
        
def criarTabelaAparitDeString(sqlString,nometab,cur:sqlite3.Cursor):
    try:
        cur.execute(sqlString)
    except SyntaxError:
        return SyntaxError.msg
    #verifica se a tabela master está diferente de vazia
    res = cur.execute("SELECT name FROM sqlite_master") 
    respTupla = res.fetchall()
    for info in respTupla:
        if info[0] == nometab:
            return  info[0]
          
def criaTabelaDinamica(nomeTab,tupColuns,cur:sqlite3.Cursor):
    #query de criacao
    query = "CREATE TABLE {}{}".format(nomeTab,tupColuns)
    #executa a query
    try:
        cur.execute(query)
    except SyntaxError:
        return SyntaxError.msg
    #verifica se a tabela master está diferente de vazia
    res = cur.execute("SELECT name FROM sqlite_master") 
    respTupla = res.fetchall()
    for info in respTupla:
        if info[0] == nomeTab:
            return  info[0]