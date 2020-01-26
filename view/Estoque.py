from tkintertable import TableCanvas, TableModel, Filtering
from tkinter import *
from tkinter import ttk
from collections import OrderedDict
from .Helpers import criarBuscarFrame, criarDateSelectorFrame, formatedMoney, formatedExpirationDate, expirationDateParser, moneyParser
from . import config as db
from .Produtos import selecionar as selecionarProduto
import random
import datetime

tableName = "Estoque"
selected = {}
produtoId = -1

def getTable():
  table = db.listarTudoEstoque()
  if table == []:
    data = { 1: {"codigo": "", "Quantidade": "", "Validade": "", "Produto_codigo": "", "Preco": "", } }
  else:
    # data = { i : table[i] for i in range(0, len(table) ) }
    data = {}
    for i in range(0, len(table) ):
      data[i] = table[i]
      data[i]["Validade"] = formatedExpirationDate(data[i]["Validade"])
      data[i]["Preco"] = formatedMoney(data[i]["Preco"])
      # data[i].pop()
  return data

def updateTable(tabela):
  tabela.model.importDict(getTable())
  tabela.redraw()

def mostrar():
  # funcao que chama a janela de estoque
  data = getTable()
  mostrarWindow = Toplevel()
  estoqueFrame = Frame(mostrarWindow)
  tabelaEstoque = TableCanvas(estoqueFrame, data=data, read_only=TRUE)

  # Frame de busca
  buscarFrame = criarBuscarFrame(mostrarWindow, tabelaEstoque)
  buscarFrame.pack()

  # Frame da tabela de estoque
  tabelaEstoque.show()
  estoqueFrame.pack()

  # Frame de actions
  def cadastarEstoque():
    cadastrar(tabelaEstoque)

  def deletarEstoque():
    selected = tabelaEstoque.get_currentRecord()["codigo"]
    db.apagarLinhaTabela(tableName, selected)
    updateTable(tabelaEstoque)

  def editarEstoque():
    selected = tabelaEstoque.get_currentRecord()
    print(selected["codigo"])
    editar(selected, tabelaEstoque)
  
  actionsFrame = Frame(mostrarWindow)
  cadastrarBtn = Button(actionsFrame, text="Cadastrar Novo", command=cadastarEstoque)
  deletarEstoqueBtn = Button(actionsFrame, text="Deletar Selecionado", command=deletarEstoque)
  editarEstoqueBtn = Button(actionsFrame, text="Editar Selecionado", command=editarEstoque)

  cadastrarBtn.pack(side=LEFT)
  deletarEstoqueBtn.pack(side=LEFT)
  editarEstoqueBtn.pack(side=LEFT)
  actionsFrame.pack()

  mostrarWindow.mainloop()

def cadastrar(tabela):
  def marcaSelect():
    global produtoId
    var = selecionarProduto()
    print(var)
    produtoInput.insert(0, var['Descricao'])
    produtoId = var['codigo']

  # Funcao que cria janela de cadastar novo produto
  cadastrarWindow = Toplevel()

  # Frame do formulario de produto
  cadastrarForm = Frame(cadastrarWindow)
  qtdLabel = Label(cadastrarForm, text="Quantidade")
  qtdInput = Entry(cadastrarForm)
  produtoLabel = Label(cadastrarForm, text="Produto")
  produtoInput = Entry(cadastrarForm)
  produtoButton = Button(cadastrarForm, text="Selecionar", command=marcaSelect)
  precoLabel = Label(cadastrarForm, text="Preço")
  precoInput = Entry(cadastrarForm)
  dtValidadeLabel = Label(cadastrarForm, text="Data de Validade")
  dtValidadeInput = Entry(cadastrarForm)
  qtdLabel.grid(row=0, column=0)
  qtdInput.grid(row=0, column=1)
  produtoLabel.grid(row=1, column=0)
  produtoInput.grid(row=1, column=1)
  produtoButton.grid(row=1, column=2)
  precoLabel.grid(row=2, column=0)
  precoInput.grid(row=2, column=1)
  dtValidadeLabel.grid(row=3, column=0)
  dtValidadeInput.grid(row=3, column=1)

  cadastrarForm.pack()

  # Frame de acoes do formulario
  def cadastrarEstoque():
    global produtoId
    if (produtoId > -1):
      insertData = {"Quantidade": qtdInput.get(), "Validade": expirationDateParser(dtValidadeInput.get()), "Produto_codigo": produtoId, "Preco": moneyParser(precoInput.get())}
      ret = db.insereEstoque(insertData)
      produtoId = -1
      if (ret != None):
        cadastrarWindow.quit()
        cadastrarWindow.destroy()
        updateTable(tabela)
      else:
        print("erro")
    return ret

  estoqueActionsFrame = Frame(cadastrarWindow)
  cadastrarEstoqueBtn = Button(estoqueActionsFrame, text="Cadastar", command=cadastrarEstoque)
  cadastrarEstoqueBtn.pack(side=LEFT)
  estoqueActionsFrame.pack()

  cadastrarWindow.mainloop()

def editar(data, tabela):
  # Funcao que chama janela de cadastar novo produto
  editarWindow = Toplevel()

  # Frame do formulario de produto
  editarForm = Frame(editarWindow)
  nomeLabel = Label(editarForm, text="Nome da Estoque")
  nomeInput = Entry(editarForm)
  nomeInput.insert(0, data["Nome"])
  nomeLabel.grid(row=0, column=0)
  nomeInput.grid(row=0, column=1)

  editarForm.pack()

  # Frame de acoes do formulario
  def editarEstoque():
    data["Nome"] = nomeInput.get()
    db.atualizarLinhaTabela(tableName, data)
    editarWindow.quit()
    editarWindow.destroy()
    updateTable(tabela)

  estoqueActionsFrame = Frame(editarWindow)
  editarEstoqueBtn = Button(estoqueActionsFrame, text="Atualizar", command=editarEstoque)
  editarEstoqueBtn.pack(side=LEFT)
  estoqueActionsFrame.pack()


  editarWindow.mainloop()


def selecionar():
  # funcao que chama a janela de estoque
  data = getTable()
  selecionarWindow = Toplevel()
  estoqueFrame = Frame(selecionarWindow)
  tabelaEstoque = TableCanvas(estoqueFrame, data=data, read_only=TRUE)

  # Frame de busca
  buscarFrame = criarBuscarFrame(selecionarWindow, tabelaEstoque)
  buscarFrame.pack()

  # Frame da tabela de estoque
  tabelaEstoque.show()
  estoqueFrame.pack()

  # Frame de actions
  def retornarSelecionado():
    global selected
    selected = tabelaEstoque.get_currentRecord()
    selecionarWindow.quit()
    selecionarWindow.destroy()

  actionsFrame = Frame(selecionarWindow)
  cadastrarBtn = Button(actionsFrame, text="Escolher selecionado", command=retornarSelecionado) #tabelaEstoque.showAll)

  cadastrarBtn.pack(side=LEFT)
  actionsFrame.pack()

  selecionarWindow.mainloop()
  return selected
