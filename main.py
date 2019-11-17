from tkintertable import TableCanvas, TableModel
from tkinter import *
from collections import OrderedDict
#lib que gera dados aleatórios remover quando tiver os dados do banco
from tkintertable.Testing import sampledata
import random

data = sampledata()

def mostrarEstoque():
  # funcao que chama a janela de estoque
  mostrarEstoqueWindow = Toplevel()

  # Frame de busca
  def buscar():
    print("batata")
  buscaFrame = Frame(mostrarEstoqueWindow)
  buscaInput = Entry(buscaFrame)
  buscaBtn = Button(buscaFrame, text="Buscar", command=buscar)
  buscaInput.pack(side=LEFT)
  buscaBtn.pack(side=LEFT)

  buscaFrame.pack()

  # Frame da tabela de estoque
  estoqueFrame = Frame(mostrarEstoqueWindow)
  tabelaEstoque = TableCanvas(estoqueFrame, data=data)
  tabelaEstoque.show()
  estoqueFrame.pack()

  mostrarEstoqueWindow.mainloop()

main = Tk()

mostrarEstoqueBtn = Button(main, text="Mostrar Estoque", command=mostrarEstoque)
mostrarEstoqueBtn.pack()

main.mainloop()