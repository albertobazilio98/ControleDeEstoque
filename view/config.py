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

def ultimoIDinserido(cursor,tabela):
  '''
  Função que retorna o proximo ID a ser inserido determinada numa tabela com PK auto_increment

  Parametros:
  cursor -- cursor da class mysql.connector
  tabela -- nome da tabela da qual deseja-se pegar o ultimo ID inserido
  '''
  ultimoID = cursor.execute('SELECT max(codigo) FROM {};'.format(tabela))
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
  marca -- dicionario contendo os valores da marca em questão ('codigo','Nome')
  '''
  global cnx
  cursor = cnx.cursor()
  try:
    ID = ultimoIDinserido(cursor,"Marca")

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
  cliente -- dicionario contendo os valores do cliente em questao('codigo','Nome','Telefone')
  '''
  global cnx
  cursor = cnx.cursor()
  try:
    ID = ultimoIDinserido(cursor,"Cliente")
    
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
  estoque -- dicionario contendo os valores do estoque em questao('codigo','Quantidade','Validade','Produto_codigo','Preco')

  '''
  global cnx
  cursor=cnx.cursor()
  try:
    ID = ultimoIDinserido(cursor,"Estoque")

    cursor.execute("INSERT INTO Estoque VALUES ({},{},'{}',{},{})" \
    .format(ID,estoque['Quantidade'],estoque['Validade'],estoque['Produto_codigo'],estoque['Preco']))
    cnx.commit()
    cursor.close()
  except:
    cursor.close()
    return(None)
  else:
    return(estoque)

def insereVenda(venda):
  '''
  Insere uma venda, passada como parametro, na database

  Parametros:
  venda -- dicionario contendo os valores da venda em questao('codigo','DataVenda','DataPagamento','Cliente_idCliente')
  '''
  cursor=cnx.cursor()
  try:
    ID = ultimoIDinserido(cursor,"Venda")
    cursor.execute("INSERT INTO Venda VALUES ({},'{}','{}',{})"\
    .format(ID,venda['DataVenda'],venda['DataPagamento'],venda['Cliente_idCliente']))
    cnx.commit()
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
    cnx.commit()
    cursor.close()
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

def apagarLinhaTabela(tabela,ID,ID2=None):
  '''
  Apaga uma linha de uma determinada tabela com determinado ID

  Parametros:
  tabela -- tabela da qual a linha sera apagada
  ID -- PK da linha a ser apagada (ou FK Estoque_idEstoque caso a tabela selecionada seja DescricaoDeVenda)
  ID2 -- Parametro opcional reservado para a FK Venda_idVenda da tabela DescricaoDeVenda, caso esta tabela seja selecionada
  '''
  cursor = cnx.cursor()
  try:
    if ID2==None:
      cursor.execute("DELETE FROM {} WHERE codigo={}".format(tabela,ID))
      cnx.commit()
      cursor.close()
      return(ID)
    else: #DescricaoVenda('Estoque_idEstoque','Venda_idVenda')
      cursor.execute("DELETE FROM {} WHERE Estoque_idEstoque={} AND Venda_idVenda={}".format(tabela,ID,ID2))
      cnx.commit()
      cursor.close()
      return(ID,ID2)
  except:
    cursor.close()
    return(None)

def atualizarLinhaTabela(tabela,objeto):
  '''
  Atualiza uma linha numa determinada tabela com determinado ID

  Parametros:
  objeto -- Objeto atualizado de uma determinada tabela('Produto','Cliente','Venda',etc)
  tabela -- Nome da tabela a qual pertence o objeto
  '''
  cursor = cnx.cursor()

  try:
    if tabela=="Marca":
      cursor.execute("UPDATE Marca SET Nome='{}' WHERE codigo={}"\
      .format(objeto['Nome'],objeto['codigo']))
      cnx.commit()
      cursor.close()
      return(objeto)

    elif tabela=="Produto":
      cursor.execute("UPDATE Produto SET Descricao='{}',Linha='{}',Marca_idMarca='{}' WHERE codigo={}"\
      .format(objeto['Descricao'],objeto['Linha'],objeto['Marca_idMarca'],objeto['codigo']))
      cnx.commit()
      cursor.close()
      return(objeto)

    elif tabela=="Cliente":
      cursor.execute("UPDATE Cliente SET Nome='{}',Telefone='{}' WHERE codigo={}"\
      .format(objeto['Nome'],objeto['Telefone'],objeto['codigo']))
      cnx.commit()
      cursor.close()
      return(objeto)

    elif tabela=="Estoque":
      cursor.execute("UPDATE Estoque SET Quantidade={},Validade='{}',Produto_codigo={},Preco={} WHERE codigo={}"\
      .format(objeto['Quantidade'],objeto['Validade'],objeto['Produto_codigo'],objeto['Preco'],objeto['codigo']))
      cnx.commit()
      cursor.close()
      return(objeto)

    elif tabela=="Venda": #venda('codigo','DataVenda','DataPagamento','Cliente_idCliente')
      cursor.execute("UPDATE Venda SET DataVenda='{}',DataPagamento='{}',Cliente_idCliente={} WHERE codigoa={}"\
      .format(objeto['DataVenda'],objeto['DataPagamento'],objeto['Cliente_idCliente'],objeto['codigo']))
      cnx.commit()
      cursor.close()
      return(objeto)

    elif tabela=="DescricaoVenda": #DescricaoVenda('Estoque_idEstoque','Venda_idVenda','quantidadeProduto')
      cursor.execute("Update DescricaoVenda SET quantidadeProduto={} WHERE Estoque_idEstoque={} AND Venda_idVenda={}"\
      .format(objeto['quantidadeProduto'],objeto['Estoque_idEstoque'],objeto['Venda_idVenda']))
      cnx.commit()
      cursor.close()
      return(objeto)
    else:
      return(-1)
  except mysql.connector.Error as err:
    print(err)
    cursor.close()
    return(None)