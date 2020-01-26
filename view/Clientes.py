from tkintertable import TableCanvas, TableModel, Filtering
from tkinter import *
from tkinter import ttk
from collections import OrderedDict
from .Helpers import criarBuscarFrame, criarDateSelectorFrame
from . import config as db

#lib que gera dados aleatórios remover quando tiver os dados do banco
from tkintertable.Testing import sampledata
import random

tableName = "Cliente"
selected = {}

def getTable():
  table = db.listarTudoTabela(tableName)
  if table == []:
    data = { 1: {"codigo": "", "Nome": "", "Telefone": ""} }
  else:
    data = { i : table[i] for i in range(0, len(table) ) }
  return data

def updateTable(tabela):
  tabela.model.importDict(getTable())
  tabela.redraw()

def mostrar():
  # funcao que chama a janela de cliente
  data = getTable()
  mostrarWindow = Toplevel()
  clienteFrame = Frame(mostrarWindow)
  tabelaCliente = TableCanvas(clienteFrame, data=data, read_only=TRUE)

  # Frame de busca
  buscarFrame = criarBuscarFrame(mostrarWindow, tabelaCliente)
  buscarFrame.pack()

  # Frame da tabela de cliente
  tabelaCliente.show()
  clienteFrame.pack()

  # Frame de actions
  def cadastarCliente():
    cadastrar(tabelaCliente)

  def deletarCliente():
    selected = tabelaCliente.get_currentRecord()["codigo"]
    db.apagarLinhaTabela(tableName, selected)
    updateTable(tabelaCliente)

  def editarCliente():
    selected = tabelaCliente.get_currentRecord()
    print(selected["codigo"])
    editar(selected, tabelaCliente)
  
  actionsFrame = Frame(mostrarWindow)
  cadastrarBtn = Button(actionsFrame, text="Cadastrar Novo", command=cadastarCliente)
  deletarClienteBtn = Button(actionsFrame, text="Deletar Selecionado", command=deletarCliente)
  editarClienteBtn = Button(actionsFrame, text="Editar Selecionado", command=editarCliente)

  cadastrarBtn.pack(side=LEFT)
  deletarClienteBtn.pack(side=LEFT)
  editarClienteBtn.pack(side=LEFT)
  actionsFrame.pack()

  mostrarWindow.mainloop()

def cadastrar(tabela):
  # Funcao que cria janela de cadastar novo produto
  cadastrarWindow = Toplevel()

  # Frame do formulario de produto
  cadastrarForm = Frame(cadastrarWindow)
  nomeLabel = Label(cadastrarForm, text="Nome do Cliente")
  nomeInput = Entry(cadastrarForm)
  phoneLabel = Label(cadastrarForm, text="Telefone do Cliente")
  phoneInput = Entry(cadastrarForm)
  nomeLabel.grid(row=0, column=0)
  nomeInput.grid(row=0, column=1)
  phoneLabel.grid(row=1, column=0)
  phoneInput.grid(row=1, column=1)

  cadastrarForm.pack()

  # Frame de acoes do formulario
  def cadastrarCliente():
    insertData = {"Nome": nomeInput.get(), "Telefone": phoneInput.get()}
    ret = db.insereCliente(insertData)
    print(ret)
    cadastrarWindow.quit()
    cadastrarWindow.destroy()
    updateTable(tabela)
    return ret

  clienteActionsFrame = Frame(cadastrarWindow)
  cadastrarClienteBtn = Button(clienteActionsFrame, text="Cadastar", command=cadastrarCliente)
  cadastrarClienteBtn.pack(side=LEFT)
  clienteActionsFrame.pack()

  cadastrarWindow.mainloop()

def editar(data, tabela):
  # Funcao que chama janela de cadastar novo produto
  editarWindow = Toplevel()

  # Frame do formulario de produto
  editarForm = Frame(editarWindow)
  nomeLabel = Label(editarWindow, text="Nome do Cliente")
  nomeInput = Entry(editarWindow)
  phoneLabel = Label(editarWindow, text="Telefone do Cliente")
  phoneInput = Entry(editarWindow)
  nomeLabel.grid(row=0, column=0)
  nomeInput.grid(row=0, column=1)
  phoneLabel.grid(row=1, column=0)
  phoneInput.grid(row=1, column=1)

  editarForm.pack()

  # Frame de acoes do formulario
  def editarCliente():
    data["Nome"] = nomeInput.get()
    data["Telefone"] = phoneInput.get()
    db.atualizarLinhaTabela(tableName, data)
    editarWindow.quit()
    editarWindow.destroy()
    updateTable(tabela)

  clienteActionsFrame = Frame(editarWindow)
  editarClienteBtn = Button(clienteActionsFrame, text="Atualizar", command=editarCliente)
  editarClienteBtn.pack(side=LEFT)
  clienteActionsFrame.pack()


  editarWindow.mainloop()


def selecionar():
  # funcao que chama a janela de cliente
  data = getTable()
  selecionarWindow = Toplevel()
  clienteFrame = Frame(selecionarWindow)
  tabelaCliente = TableCanvas(clienteFrame, data=data, read_only=TRUE)

  # Frame de busca
  buscarFrame = criarBuscarFrame(selecionarWindow, tabelaCliente)
  buscarFrame.pack()

  # Frame da tabela de cliente
  tabelaCliente.show()
  clienteFrame.pack()

  # Frame de actions
  def retornarSelecionado():
    global selected
    selected = tabelaCliente.get_currentRecord()
    selecionarWindow.quit()
    selecionarWindow.destroy()

  actionsFrame = Frame(selecionarWindow)
  cadastrarBtn = Button(actionsFrame, text="Escolher selecionado", command=retornarSelecionado) #tabelaCliente.showAll)

  cadastrarBtn.pack(side=LEFT)
  actionsFrame.pack()

  selecionarWindow.mainloop()
  return selected
