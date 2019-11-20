from tkintertable import TableCanvas, TableModel
from tkinter import *
from collections import OrderedDict

#lib que gera dados aleatórios remover quando tiver os dados do banco
from tkintertable.Testing import sampledata
import random


data = sampledata()

def mostrar():
  # funcao que chama a janela de cliente
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

  # Frame da tabela de cliente
  clienteFrame = Frame(mostrarWindow)
  tabelaCliente = TableCanvas(clienteFrame, data=data, read_only=TRUE)
  tabelaCliente.show()
  clienteFrame.pack()

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
  nomeLabel = Label(cadastrarForm, text="Nome do Cliente")
  nomeInput = Entry(cadastrarForm)
  phoneLabel = Label(cadastrarForm, text="Telefone")
  phoneInput = Entry(cadastrarForm)

  nomeLabel.grid(row=0, column=0)
  nomeInput.grid(row=0, column=1)
  phoneLabel.grid(row=1, column=0)
  phoneInput.grid(row=1, column=1)

  cadastrarForm.pack()

  # Frame de acoes do formulario
  def cadastrarProduto():
    print(nomeInput.get())
  produtoClienteActions = Frame(cadastrarWindow)
  cadastrarProdutoBtn = Button(produtoClienteActions, text="Cadastar", command=cadastrarProduto)

  cadastrarProdutoBtn.pack(side=LEFT)
  produtoClienteActions.pack()


  cadastrarWindow.mainloop()