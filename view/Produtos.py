from tkintertable import TableCanvas, TableModel, Filtering
from tkinter import *
from tkinter import ttk
from collections import OrderedDict
from .Helpers import criarBuscarFrame, criarDateSelectorFrame
from . import config as db
from .Marcas import selecionar as selecionarMarca
import random

tableName = "Produto"
selected = {}
marcaId = -1

def getTable():
  table = db.listarTudoTabela(tableName)
  if table == []:
    data = { 1: {"codigo": "", "Descricao": "", "Linha": "", "Marca_idMarca": ""} }
  else:
    # data = { i : table[i] for i in range(0, len(table) ) }
    data = {}
    for i in range(0, len(table) ):
      data[i] = table[i]
      data[i]["Marca_idMarca"] = db.selecionarLinha("Marca", data[i]["Marca_idMarca"])["Nome"]
  return data

def updateTable(tabela):
  tabela.model.importDict(getTable())
  tabela.redraw()

def mostrar():
  # funcao que chama a janela de produto
  data = getTable()
  mostrarWindow = Toplevel()
  produtoFrame = Frame(mostrarWindow)
  tabelaProduto = TableCanvas(produtoFrame, data=data, read_only=TRUE)

  # Frame de busca
  buscarFrame = criarBuscarFrame(mostrarWindow, tabelaProduto)
  buscarFrame.pack()

  # Frame da tabela de produto
  tabelaProduto.show()
  produtoFrame.pack()

  # Frame de actions
  def cadastarProduto():
    cadastrar(tabelaProduto)

  def deletarProduto():
    selected = tabelaProduto.get_currentRecord()["codigo"]
    db.apagarLinhaTabela(tableName, selected)
    tabelaProduto.deleteRow()
    updateTable(tabelaProduto)

  def editarProduto():
    selected = tabelaProduto.get_currentRecord()
    print(selected["codigo"])
    editar(selected, tabelaProduto)
  
  actionsFrame = Frame(mostrarWindow)
  cadastrarBtn = Button(actionsFrame, text="Cadastrar Novo", command=cadastarProduto)
  deletarProdutoBtn = Button(actionsFrame, text="Deletar Selecionado", command=deletarProduto)
  editarProdutoBtn = Button(actionsFrame, text="Editar Selecionado", command=editarProduto)

  cadastrarBtn.pack(side=LEFT)
  deletarProdutoBtn.pack(side=LEFT)
  editarProdutoBtn.pack(side=LEFT)
  actionsFrame.pack()

  mostrarWindow.mainloop()

def cadastrar(tabela):
  def marcaSelect():
    global marcaId
    var = selecionarMarca()
    print(var)
    marcaInput.delete(0, END)
    marcaInput.insert(0, var['Nome'])
    marcaId = var['codigo']

  # Funcao que cria janela de cadastar novo produto
  cadastrarWindow = Toplevel()

  # Frame do formulario de produto
  cadastrarForm = Frame(cadastrarWindow)
  codLabel = Label(cadastrarForm, text="Código do Produto")
  codInput = Entry(cadastrarForm)
  descricaoLabel = Label(cadastrarForm, text="Descrição do Produto")
  descricaoInput = Entry(cadastrarForm)
  linhaLabel = Label(cadastrarForm, text="Linha do Produto")
  linhaInput = Entry(cadastrarForm)
  marcaLabel = Label(cadastrarForm, text="Marca do Produto")
  marcaInput = Entry(cadastrarForm)
  marcaButton = Button(cadastrarForm, text="Selecionar", command=marcaSelect)
  codLabel.grid(row=0, column=0)
  codInput.grid(row=0, column=1)
  descricaoLabel.grid(row=1, column=0)
  descricaoInput.grid(row=1, column=1)
  linhaLabel.grid(row=2, column=0)
  linhaInput.grid(row=2, column=1)
  marcaLabel.grid(row=3, column=0)
  marcaInput.grid(row=3, column=1)
  marcaButton.grid(row=3, column=2)


  cadastrarForm.pack()

  # Frame de acoes do formulario
  def cadastrarProduto():
    global marcaId
    if (marcaId > -1):
      insertData = { "codigo": codInput.get(), "Descricao": descricaoInput.get(), "Linha": linhaInput.get(), "Marca_idMarca": marcaId }
      ret = db.insereProduto(insertData)
      marcaId = -1
      if (ret != None):
        cadastrarWindow.quit()
        cadastrarWindow.destroy()
        updateTable(tabela)
      else:
        print("erro")
    return ret

  produtoActionsFrame = Frame(cadastrarWindow)
  cadastrarProdutoBtn = Button(produtoActionsFrame, text="Cadastar", command=cadastrarProduto)
  cadastrarProdutoBtn.pack(side=LEFT)
  produtoActionsFrame.pack()

  cadastrarWindow.mainloop()

def editar(data, tabela):
  def marcaSelect():
    global marcaId
    var = selecionarMarca()
    print(var)
    marcaInput.delete(0, END)
    marcaInput.insert(0, var['Nome'])
    marcaId = var['codigo']

  # Funcao que chama janela de cadastar novo produto
  editarWindow = Toplevel()

  # Frame do formulario de produto
  editarForm = Frame(editarWindow)
  codLabel = Label(editarForm, text="Código do Produto")
  codInput = Entry(editarForm)
  descricaoLabel = Label(editarForm, text="Descrição do Produto")
  descricaoInput = Entry(editarForm)
  linhaLabel = Label(editarForm, text="Linha do Produto")
  linhaInput = Entry(editarForm)
  marcaLabel = Label(editarForm, text="Marca do Produto")
  marcaInput = Entry(editarForm)
  marcaButton = Button(editarForm, text="Selecionar", command=marcaSelect)
  codInput.insert(0, data["codigo"])
  descricaoInput.insert(0, data["Descricao"])
  linhaInput.insert(0, data["Linha"])
  marcaInput.insert(0, data["Marca_idMarca"])
  codLabel.grid(row=0, column=0)
  codInput.grid(row=0, column=1)
  descricaoLabel.grid(row=1, column=0)
  descricaoInput.grid(row=1, column=1)
  linhaLabel.grid(row=2, column=0)
  linhaInput.grid(row=2, column=1)
  marcaLabel.grid(row=3, column=0)
  marcaInput.grid(row=3, column=1)
  marcaButton.grid(row=3, column=2)

  editarForm.pack()

  # Frame de acoes do formulario
  def editarProduto():
    global marcaId
    print(marcaInput.get())
    querry = db.doQuerry("Marca", "Nome", marcaInput.get())
    print(querry)
    marcaId = querry["codigo"] 
    ret = None
    if (marcaId > -1):
      insertData = { "codigo": codInput.get(), "Descricao": descricaoInput.get(), "Linha": linhaInput.get(), "Marca_idMarca": marcaId }
      ret = db.insereProduto(insertData)
      marcaId = -1
      if (ret != None):
        editarWindow.quit()
        editarWindow.destroy()
        updateTable(tabela)
      else:
        print("erro")
    return ret

  produtoActionsFrame = Frame(editarWindow)
  editarProdutoBtn = Button(produtoActionsFrame, text="Atualizar", command=editarProduto)
  editarProdutoBtn.pack(side=LEFT)
  produtoActionsFrame.pack()


  editarWindow.mainloop()


def selecionar():
  # funcao que chama a janela de marca
  data = getTable()
  selecionarWindow = Toplevel()
  produtoFrame = Frame(selecionarWindow)
  tabelaProduto = TableCanvas(produtoFrame, data=data, read_only=TRUE)

  # Frame de busca
  buscarFrame = criarBuscarFrame(selecionarWindow, tabelaProduto)
  buscarFrame.pack()

  # Frame da tabela de produto
  tabelaProduto.show()
  produtoFrame.pack()

  # Frame de actions
  def cadastarProduto():
    cadastrar(tabelaProduto)

  def retornarSelecionado():
    global selected
    selected = tabelaProduto.get_currentRecord()
    selecionarWindow.quit()
    selecionarWindow.destroy()

  actionsFrame = Frame(selecionarWindow)
  selecionarBtn = Button(actionsFrame, text="Escolher selecionado", command=retornarSelecionado) #tabelaProduto.showAll)
  cadastrarBtn = Button(actionsFrame, text="Novo produto", command=cadastarProduto)

  selecionarBtn.pack(side=LEFT)
  cadastrarBtn.pack(side=LEFT)
  actionsFrame.pack()

  selecionarWindow.mainloop()
  return selected
