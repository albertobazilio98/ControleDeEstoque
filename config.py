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

def insereMarca(marca):
  '''
  Insere uma marca, passada como parametro, na database.

  Parametros:
  marca -- dicionario contendo os valores da marca em questão ('Nome') >>Os valores sao case-sensitive<<
  '''
  global cnx
  cursor = cnx.cursor()
  try:
    cursor.execute("INSERT INTO Marca(Nome) VALUES('{}')".format(marca['Nome']))
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
  cliente -- dicionario contendo os valores do cliente em questao('Nome','Telefone')
  '''
  global cnx
  cursor = cnx.cursor()
  try:
    ultimoId = cursor.execute('SELECT idCliente FROM Cliente ORDER BY idCliente DESC LIMIT 1;')
    print(ultimoId)
    if ultimoId==None:
      ultimoId=0
    cursor.execute("INSERT INTO Cliente VALUES ({},'{}','{}')"\
                    .format(ultimoId+1,cliente['Nome'],cliente['Telefone']))
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
  estoque -- dicionario contendo os valores do estoque em questao('Quantidade','Validade','Produto_codigo','Preco')

  '''
  global cnx
  cursor=cnx.cursor()
  try:
    cursor.execute("INSERT INTO Estoque (Quantidade,Validade,Produto_codigo,Preco) VALUES ({},'{}',{},{})" \
                    .format(estoque['Quantidade'],estoque['Validade'],estoque['Produto_codigo'],estoque['Preco']))
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
  cursor = cnx.cursor()
  try:
    cursor.execute("SELECT * FROM {}".format(tabela))
    lista = cursor.fetchall()
    cursor.close()
    return(lista)
  except:
    return(None)

