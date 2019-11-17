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
  tabelaEstoque = TableCanvas(estoqueFrame, data=data)
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
  cadastrarProdutoEstoqueWindow = Toplevel()

  # Frame do formulario de produto
  produtoEstoqueForm = Frame(cadastrarProdutoEstoqueWindow)
  codProdutoLabel = Label(produtoEstoqueForm, text="Código do Produto")
  codProdutoInput = Entry(produtoEstoqueForm)
  qtdProdutoLabel = Label(produtoEstoqueForm, text="Quantidade")
  qtdProdutoInput = Entry(produtoEstoqueForm)
  dataEntradaProdutoLabel = Label(produtoEstoqueForm, text="Data de entrada")
  dataEntradaProdutoInput = Entry(produtoEstoqueForm)
  validadeProdutoLabel = Label(produtoEstoqueForm, text="Validade")
  validadeProdutoInput = Entry(produtoEstoqueForm)
  precoProdutoLabel = Label(produtoEstoqueForm, text="Preço")
  precoProdutoInput = Entry(produtoEstoqueForm)

  codProdutoLabel.grid(row=0, column=0)
  codProdutoInput.grid(row=0, column=1)
  qtdProdutoLabel.grid(row=1, column=0)
  qtdProdutoInput.grid(row=1, column=1)
  dataEntradaProdutoLabel.grid(row=2, column=0)
  dataEntradaProdutoInput.grid(row=2, column=1)
  validadeProdutoLabel.grid(row=3, column=0)
  validadeProdutoInput.grid(row=3, column=1)
  precoProdutoLabel.grid(row=4, column=0)
  precoProdutoInput.grid(row=4, column=1)

  produtoEstoqueForm.pack()

  # Frame de acoes do formulario
  def cadastrarProduto():
    print("batata")
  produtoEstoqueActions = Frame(cadastrarProdutoEstoqueWindow)
  cadastrarProdutoBtn = Button(produtoEstoqueActions, text="Cadastar", command=cadastrarProduto)

  cadastrarProdutoBtn.pack(side=LEFT)
  produtoEstoqueActions.pack()


  cadastrarProdutoEstoqueWindow.mainloop()