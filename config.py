import mysql.connector
from mysql.connector import errorcode

DB_NAME = "ControleDeVendas"

config = {
  # ------------------ MUDAR ISSO AQUI PROS PARAMETROS DO USUARIO ------------------
  'user':'root',
  'password':'root',
  'host': '127.0.0.1'
}

DB_NAME = 'ControleDeVendas'

#estabelece-se a conexao com o banco de dados, com as configuracoes presentes no dicionario config
cnx = mysql.connector.connect(**config)

#cursor para a execucao de comandos na linguagem MySQL
cursor = cnx.cursor()

#Conecta-se a database presente na variavel DB_NAME
try:
  cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
  print("Database {} nao existe.".format(DB_NAME))

cursor.close()

def ultimoIDinserido(cursor,tabela,coluna):
  ultimoID = cursor.execute('SELECT max({}) FROM {};'.format(coluna,tabela))
  ultimoID = cursor.fetchall()

  '''Como a query executada anteriormente retorna uma lista de tuplas(com apenas 1 tupla com 1 elemento),
    pega-se o primeiro elemento da primeira tupla, que é o valor da coluna da tabela, passadas como parametros.
    Caso a tabela esteja vazia, o valor da coluna será None'''
  ultimoID=list(ultimoID[0]).pop()
  if ultimoID == None:
    ultimoID = 0

  return (int(ultimoID)+1)

def insereMarca(marca):
  '''
  Insere uma marca, passada como parametro, na database.

  Parametros:
  marca -- dicionario contendo os valores da marca em questão ('idMarca','Nome')
  '''
  global cnx
  cursor = cnx.cursor()
  try:
    ID = ultimoIDinserido(cursor,"Marca","idMarca")

    cursor.execute("INSERT INTO Marca VALUES({},'{}')".format(ID,marca['Nome']))
    cnx.commit()
    cursor.close()
  except mysql.connector.Error as err:
    cursor.close()
    print(err)
    return(None)
  else:
    return(marca)

def insereProduto(produto):
  '''
  Insere um produto, passado como parametro, na database.

  Parametros:
  produto -- dicionario contendo os valores do produto em questao('codigo','Descricao','Linha','Marca_idMarca')
  '''
  global cnx
  cursor = cnx.cursor()
  try:
    cursor.execute("INSERT INTO Produto VALUES ({},'{}','{}',{})"\
    .format(produto['codigo'],produto['Descricao'], produto['Linha'], produto['Marca_idMarca']))

    cnx.commit()
    cursor.close()
  except:
    cursor.close()
    return(None)
  else:
    return(produto)

def insereCliente(cliente):
  '''
  Insere um cliente, passado como parametro, na database.

  Parametros:
  cliente -- dicionario contendo os valores do cliente em questao('idCliente','Nome','Telefone')
  '''
  global cnx
  cursor = cnx.cursor()
  try:
    ID = ultimoIDinserido(cursor,"Cliente","idCliente")
    
    cursor.execute("INSERT INTO Cliente VALUES ({},'{}','{}')"\
    .format(ID,cliente['Nome'],cliente['Telefone']))
    cnx.commit()
    cursor.close()
  except mysql.connector.Error as err:
    cursor.close()
    print(err)
    return(None)
  else:
    return(cliente)

def insereEstoque(estoque):
  '''
  Insere um estoque, passado como parametro, na database.

  Parametros:
  estoque -- dicionario contendo os valores do estoque em questao('idEstoque','Quantidade','Validade','Produto_codigo','Preco')

  '''
  global cnx
  cursor=cnx.cursor()
  try:
    ID = ultimoIDinserido(cursor,"Estoque","idEstoque")

    cursor.execute("INSERT INTO Estoque VALUES ({},{},'{}',{},{})" \
    .format(ID,estoque['Quantidade'],estoque['Validade'],estoque['Produto_codigo'],estoque['Preco']))
  except:
    cursor.close()
    return(None)
  else:
    return(estoque)

def insereDescricaoVenda(descricaoVenda):
  '''
  Insere uma Descricao de venda, passada como parametro, na database.

  Parametros:
  descricaoVenda -- dicionario contendo os valores da descricao de venda em questao('Estoque_idEstoque','Venda_idVenda','quantidadeProduto')
  '''
  global cnx
  cursor=cnx.cursor()
  try:
    cursor.execute("INSERT INTO DescricaoVenda VALUES ({},{},{})"\
    .format(descricaoVenda['Estoque_idEstoque'],descricaoVenda['Venda_idVenda'],descricaoVenda['quantidadeProduto']))
  except:
    return(None)
  else:
    return(descricaoVenda)

def listarTudoTabela(tabela):
  '''
  Lista todas as linhas de uma determinada tabela.

  Parametros:
  tabela -- A tabela que sera listada ('Marca' ou 'Produto ou 'Estoque' etc)
  '''
  cursor = cnx.cursor(dictionary=True)
  try:
    cursor.execute("SELECT * FROM {}".format(tabela))
    lista = cursor.fetchall()
    cursor.close()
    return(lista)
  except:
    return(None)

def apagarLinhaTabela(ID,tabela,colunaID):
  cursor = cnx.cursor()
  try:
    cursor.execute("DELETE FROM {} WHERE {}={}".format(tabela,colunaID,ID))
    return(ID)
  except:
    return(None)

