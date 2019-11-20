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

def insereVenda(venda):
  '''
  Insere uma venda, passada como parametro, na database

  Parametros:
  venda -- dicionario contendo os valores da venda em questao('idVenda','DataVenda','DataPagamento','Cliente_idCliente')
  '''
  cursor=cnx.cursor()
  try:
    ID = ultimoIDinserido(cursor,"Venda","idVenda")
    cursor.execute("INSERT INTO Venda VALUES ({},'{}','{}',{})"\
    .format(ID,venda['DataVenda'],venda['DataPagamento'],venda['Cliente_idCliente']))
    cursor.close()
  except:
    cursor.close()
    return(None)
  else:
    return(venda)

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
    cursor.close()
    return(None)

def apagarLinhaTabela(ID,tabela,colunaID):
  '''
  Apaga uma linha de uma determinada tabela com determinado ID

  Parametros:
  ID -- chave primaria da linha a ser apagada
  tabela -- tabela da qual a linha sera apagada
  colunaID -- nome da coluna da chave primaria
  '''
  cursor = cnx.cursor()
  try:
    cursor.execute("DELETE FROM {} WHERE {}={}".format(tabela,colunaID,ID))
    cursor.close()
    return(ID)
  except:
    cursor.close()
    return(None)

def atualizarLinhaTabela(ID, objeto, tabela):
  '''
  Atualiza uma linha numa determinada tabela com determinado ID

  Parametros:
  ID -- Chave primária do objeto passado
  objeto -- Objeto de uma determinada tabela('Produto','Cliente','Venda',etc)
  tabela -- Nome da tabela a qual pertence o objeto
  '''
  cursor = cnx.cursor()

  try:
    if tabela=="Marca":
      cursor.execute("UPDATE 'Marca' SET Nome='{}' WHERE idMarca={}"\
      .format(objeto['Nome'],ID))

    elif tabela=="Produto":
      cursor.execute("UPDATE 'Produto' SET Descricao='{}',Linha='{}',Marca_idMarca='{}' WHERE codigo={}"\
      .format(objeto['Descricao'],objeto['Linha'],objeto['Marca_idMarca'],ID))

    elif tabela=="Cliente":
      cursor.execute("UPDATE 'Cliente' SET Nome='{}',Telefone='{}' WHERE idCliente={}"\
      .format(objeto['Nome'],objeto['Telefone'],ID))

    elif tabela=="Estoque":
      cursor.execute("UPDATE 'Estoque' SET Quantidade={},Validade='{}',Produto_codigo={},Preco={} WHERE idEstoque={}"\
      .format(objeto['Quantidade'],objeto['Validade'],objeto['Produto_codigo'],objeto['Preco'],ID))

    elif tabela=="Venda": #venda('idVenda','DataVenda','DataPagamento','Cliente_idCliente')
      cursor.execute("UPDATE 'Venda' SET DataVenda='{}',DataPagamento='{}',Cliente_idCliente={} WHERE idVenda={}"\
      .format(objeto['DataVenda'],objeto['DataPagamento'],objeto['Cliente_idCliente'],ID))

    else:
      return(-1)
  except:
    cursor.close()
    return(None)