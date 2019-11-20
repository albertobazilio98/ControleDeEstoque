from tkintertable import TableCanvas, TableModel
from tkinter import *
from tkinter import ttk
from collections import OrderedDict

#lib que gera dados aleatórios remover quando tiver os dados do banco
from tkintertable.Testing import sampledata
import random


data = sampledata()

def mostrar():
  # funcao que chama a janela de estoque
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

  # Frame da tabela de produto
  produtosFrame = Frame(mostrarWindow)
  tabelaEstoque = TableCanvas(produtosFrame, data=data, read_only=TRUE)
  tabelaEstoque.show()
  produtosFrame.pack()

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
  codLabel = Label(cadastrarForm, text="Código do Produto")
  codInput = Entry(cadastrarForm)
  decricaoLabel = Label(cadastrarForm, text="Descrição")
  decricaoInput = Entry(cadastrarForm)
  linhaLabel = Label(cadastrarForm, text="Linha")
  linhaInput = Entry(cadastrarForm)
  marcaLabel = Label(cadastrarForm, text="Marca")
  marcaInput = ttk.Combobox(cadastrarForm, values=['avon', 'natura', 'abelha rainha'])

  codLabel.grid(row=0, column=0)
  codInput.grid(row=0, column=1)
  decricaoLabel.grid(row=1, column=0)
  decricaoInput.grid(row=1, column=1)
  linhaLabel.grid(row=2, column=0)
  linhaInput.grid(row=2, column=1)
  marcaLabel.grid(row=3, column=0)
  marcaInput.grid(row=3, column=1)

  cadastrarForm.pack()

  # Frame de acoes do formulario
  def cadastrarProduto():
    print("batata")
  produtoEstoqueActions = Frame(cadastrarWindow)
  cadastrarProdutoBtn = Button(produtoEstoqueActions, text="Cadastar", command=cadastrarProduto)

  cadastrarProdutoBtn.pack(side=LEFT)
  produtoEstoqueActions.pack()


  cadastrarWindow.mainloop()