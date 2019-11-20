from tkintertable import TableCanvas, TableModel
from tkinter import *
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

  # Frame da tabela de estoque
  estoqueFrame = Frame(mostrarWindow)
  tabelaEstoque = TableCanvas(estoqueFrame, data=data, read_only=TRUE)
  tabelaEstoque.show()
  estoqueFrame.pack()

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
  qtdLabel = Label(cadastrarForm, text="Quantidade")
  qtdInput = Entry(cadastrarForm)
  dataEntradaLabel = Label(cadastrarForm, text="Data de entrada")
  dataEntradaInput = Entry(cadastrarForm)
  validadeLabel = Label(cadastrarForm, text="Validade")
  validadeInput = Entry(cadastrarForm)
  precoLabel = Label(cadastrarForm, text="Preço")
  precoInput = Entry(cadastrarForm)

  codLabel.grid(row=0, column=0)
  codInput.grid(row=0, column=1)
  qtdLabel.grid(row=1, column=0)
  qtdInput.grid(row=1, column=1)
  dataEntradaLabel.grid(row=2, column=0)
  dataEntradaInput.grid(row=2, column=1)
  validadeLabel.grid(row=3, column=0)
  validadeInput.grid(row=3, column=1)
  precoLabel.grid(row=4, column=0)
  precoInput.grid(row=4, column=1)

  cadastrarForm.pack()

  # Frame de acoes do formulario
  def cadastrarProduto():
    print(codInput.get())
  produtoEstoqueActions = Frame(cadastrarWindow)
  cadastrarProdutoBtn = Button(produtoEstoqueActions, text="Cadastar", command=cadastrarProduto)

  cadastrarProdutoBtn.pack(side=LEFT)
  produtoEstoqueActions.pack()


  cadastrarWindow.mainloop()