from tkintertable import TableCanvas, TableModel, Filtering
from tkinter import *
from collections import OrderedDict
from .Helpers import buscar
# from CustomSearchBar import *

#lib que gera dados aleatórios remover quando tiver os dados do banco
from tkintertable.Testing import sampledata
import random


data = sampledata()

def mostrar():
  # funcao que chama a janela de marca
  mostrarWindow = Toplevel()

  # Frame de busca
  def buscar():
    print("batata")
  
  buscaFrame = Frame(mostrarWindow)
  buscaInput = Entry(buscaFrame)
  buscaBtn = Button(buscaFrame, text="Buscar", command=buscar)
  buscaInput.pack(side=LEFT)
  buscaBtn.pack(side=LEFT)

  buscaFrame.pack()

  # Frame da tabela de marca
  marcaFrame = Frame(mostrarWindow)
  tabelaMarca = TableCanvas(marcaFrame, data=data, read_only=TRUE)
  tabelaMarca.show()
  marcaFrame.pack()

  # Frame de actions
  actionsFrame = Frame(mostrarWindow)
  cadastrarBtn = Button(actionsFrame, text="Cadastrar Novo", command=cadastrar)

  cadastrarBtn.pack(side=LEFT)
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
  def cadastrarProduto():
    print(nomeInput.get())
  produtoMarcaActions = Frame(cadastrarWindow)
  cadastrarProdutoBtn = Button(produtoMarcaActions, text="Cadastar", command=cadastrarProduto)

  cadastrarProdutoBtn.pack(side=LEFT)
  produtoMarcaActions.pack()


  cadastrarWindow.mainloop()

def selecionar():
  # funcao que chama a janela de marca
  mostrarWindow = Toplevel()

  # Frame de busca
  def buscarMarca():
    buscar(tabelaMarca, "a", "8")
  buscaFrame = Frame(mostrarWindow)
  buscaInput = Entry(buscaFrame)
  buscaBtn = Button(buscaFrame, text="Buscar", command=buscarMarca)
  buscaInput.pack(side=LEFT)
  buscaBtn.pack(side=LEFT)

  buscaFrame.pack()

  # Frame da tabela de marca
  marcaFrame = Frame(mostrarWindow)
  tabelaMarca = TableCanvas(marcaFrame, data=data, read_only=TRUE)
  tabelaMarca.show()
  marcaFrame.pack()

  # Frame de actions
  def retornarSelecionado():
    print(tabelaMarca.getSelectedColumn())

  actionsFrame = Frame(mostrarWindow)
  cadastrarBtn = Button(actionsFrame, text="Escolher selecionado", command=tabelaMarca.showAll)

  cadastrarBtn.pack(side=LEFT)
  actionsFrame.pack()

  mostrarWindow.mainloop()
