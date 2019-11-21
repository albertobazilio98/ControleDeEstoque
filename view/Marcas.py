from tkintertable import TableCanvas, TableModel, Filtering
from tkinter import *
from tkinter import ttk
from collections import OrderedDict
from .Helpers import criarBuscarFrame, criarDateSelectorFrame

#lib que gera dados aleatórios remover quando tiver os dados do banco
from tkintertable.Testing import sampledata
import random


data = sampledata()

def mostrar():
  # funcao que chama a janela de marca
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
    cadastrar()

  def deletarMarca():
    selected = tabelaMarca.get_currentRecord()["a"]
    print(selected)

  def editarMarca():
    selected = tabelaMarca.get_currentRecord()
    print(selected["a"])
    editar(selected)
  
  actionsFrame = Frame(mostrarWindow)
  cadastrarBtn = Button(actionsFrame, text="Cadastrar Novo", command=cadastarMarca)
  deletarMarcaBtn = Button(actionsFrame, text="Deletar Selecionado", command=deletarMarca)
  editarMarcaBtn = Button(actionsFrame, text="Editar Selecionado", command=editarMarca)

  cadastrarBtn.pack(side=LEFT)
  deletarMarcaBtn.pack(side=LEFT)
  editarMarcaBtn.pack(side=LEFT)
  actionsFrame.pack()

  mostrarWindow.mainloop()

def cadastrar():
  # Funcao que chama janela de cadastar novo produto
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
    print(nomeInput.get())

  marcaActionsFrame = Frame(cadastrarWindow)
  cadastrarMarcaBtn = Button(marcaActionsFrame, text="Cadastar", command=cadastrarMarca)
  cadastrarMarcaBtn.pack(side=LEFT)
  marcaActionsFrame.pack()


  cadastrarWindow.mainloop()

def editar(data):
  # Funcao que chama janela de cadastar novo produto
  editarWindow = Toplevel()

  # Frame do formulario de produto
  editarForm = Frame(editarWindow)
  nomeLabel = Label(editarForm, text="Nome da Marca")
  nomeInput = Entry(editarForm)
  nomeInput.insert(0, data["a"])
  nomeLabel.grid(row=0, column=0)
  nomeInput.grid(row=0, column=1)

  editarForm.pack()

  # Frame de acoes do formulario
  def editarMarca():
    print(nomeInput.get())

  marcaActionsFrame = Frame(editarWindow)
  editarMarcaBtn = Button(marcaActionsFrame, text="Cadastar", command=editarMarca)
  editarMarcaBtn.pack(side=LEFT)
  marcaActionsFrame.pack()


  editarWindow.mainloop()


def selecionar():
  # funcao que chama a janela de marca
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
  def retornarSelecionado():
    selected = tabelaMarca.get_currentRecord()
    selecionarWindow.destroy()
    return selected


  actionsFrame = Frame(selecionarWindow)
  cadastrarBtn = Button(actionsFrame, text="Escolher selecionado", command=retornarSelecionado) #tabelaMarca.showAll)

  cadastrarBtn.pack(side=LEFT)
  actionsFrame.pack()

  selecionarWindow.mainloop()
  return None
