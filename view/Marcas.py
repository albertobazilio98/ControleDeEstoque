from tkintertable import TableCanvas, TableModel, Filtering
from tkinter import *
from tkinter import ttk
from collections import OrderedDict
from .Helpers import criarBuscarFrame, criarDateSelectorFrame
from . import config as db

#lib que gera dados aleatórios remover quando tiver os dados do banco
from tkintertable.Testing import sampledata
import random

tableName = "Marca"
selected = {}

def getTable():
  table = db.listarTudoTabela(tableName)
  if table == []:
    data = { 1: {"codigo": "", "Nome": ""} }
  else:
    data = { i : table[i] for i in range(0, len(table) ) }
  return data

def updateTable(tabela):
  tabela.model.importDict(getTable())
  tabela.redraw()

def mostrar():
  # funcao que chama a janela de marca
  data = getTable()
  mostrarWindow = Toplevel()
  marcaFrame = Frame(mostrarWindow)
  tabelaMarca = TableCanvas(marcaFrame, data=data, read_only=TRUE)

  # Frame de busca
  buscarFrame = criarBuscarFrame(mostrarWindow, tabelaMarca)
  buscarFrame.pack()

  # Frame da tabela de marca
  tabelaMarca.show()
  marcaFrame.pack()

  # Frame de actions
  def cadastarMarca():
    cadastrar(tabelaMarca)

  def deletarMarca():
    selected = tabelaMarca.get_currentRecord()["codigo"]
    db.apagarLinhaTabela(tableName, selected)
    updateTable(tabelaMarca)

  def editarMarca():
    selected = tabelaMarca.get_currentRecord()
    print(selected["codigo"])
    editar(selected, tabelaMarca)
  
  actionsFrame = Frame(mostrarWindow)
  cadastrarBtn = Button(actionsFrame, text="Cadastrar Novo", command=cadastarMarca)
  deletarMarcaBtn = Button(actionsFrame, text="Deletar Selecionado", command=deletarMarca)
  editarMarcaBtn = Button(actionsFrame, text="Editar Selecionado", command=editarMarca)

  cadastrarBtn.pack(side=LEFT)
  deletarMarcaBtn.pack(side=LEFT)
  editarMarcaBtn.pack(side=LEFT)
  actionsFrame.pack()

  mostrarWindow.mainloop()

def cadastrar(tabela):
  # Funcao que cria janela de cadastar novo produto
  cadastrarWindow = Toplevel()

  # Frame do formulario de produto
  cadastrarForm = Frame(cadastrarWindow)
  nomeLabel = Label(cadastrarForm, text="Nome da Marca")
  nomeInput = Entry(cadastrarForm)
  nomeLabel.grid(row=0, column=0)
  nomeInput.grid(row=0, column=1)

  cadastrarForm.pack()

  # Frame de acoes do formulario
  def cadastrarMarca():
    insertData = {"Nome": nomeInput.get()}
    ret = db.insereMarca(insertData)
    print(ret)
    cadastrarWindow.quit()
    cadastrarWindow.destroy()
    updateTable(tabela)
    return ret

  marcaActionsFrame = Frame(cadastrarWindow)
  cadastrarMarcaBtn = Button(marcaActionsFrame, text="Cadastar", command=cadastrarMarca)
  cadastrarMarcaBtn.pack(side=LEFT)
  marcaActionsFrame.pack()

  cadastrarWindow.mainloop()

def editar(data, tabela):
  # Funcao que chama janela de cadastar novo produto
  editarWindow = Toplevel()

  # Frame do formulario de produto
  editarForm = Frame(editarWindow)
  nomeLabel = Label(editarForm, text="Nome da Marca")
  nomeInput = Entry(editarForm)
  nomeInput.insert(0, data["Nome"])
  nomeLabel.grid(row=0, column=0)
  nomeInput.grid(row=0, column=1)

  editarForm.pack()

  # Frame de acoes do formulario
  def editarMarca():
    data["Nome"] = nomeInput.get()
    db.atualizarLinhaTabela(tableName, data)
    editarWindow.quit()
    editarWindow.destroy()
    updateTable(tabela)

  marcaActionsFrame = Frame(editarWindow)
  editarMarcaBtn = Button(marcaActionsFrame, text="Atualizar", command=editarMarca)
  editarMarcaBtn.pack(side=LEFT)
  marcaActionsFrame.pack()


  editarWindow.mainloop()


def selecionar():
  # funcao que chama a janela de marca
  data = getTable()
  selecionarWindow = Toplevel()
  marcaFrame = Frame(selecionarWindow)
  tabelaMarca = TableCanvas(marcaFrame, data=data, read_only=TRUE)

  # Frame de busca
  buscarFrame = criarBuscarFrame(selecionarWindow, tabelaMarca)
  buscarFrame.pack()

  # Frame da tabela de marca
  tabelaMarca.show()
  marcaFrame.pack()

  # Frame de actions
  def cadastarMarca():
    cadastrar(tabelaMarca)

  def retornarSelecionado():
    global selected
    selected = tabelaMarca.get_currentRecord()
    selecionarWindow.quit()
    selecionarWindow.destroy()

  actionsFrame = Frame(selecionarWindow)
  selecionarBtn = Button(actionsFrame, text="Escolher selecionado", command=retornarSelecionado) #tabelaMarca.showAll)
  cadastrarBtn = Button(actionsFrame, text="Nova marca", command=cadastarMarca)

  selecionarBtn.pack(side=LEFT)
  cadastrarBtn.pack(side=LEFT)
  actionsFrame.pack()

  selecionarWindow.mainloop()
  return selected
