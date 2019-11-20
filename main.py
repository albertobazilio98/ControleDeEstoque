from tkintertable import TableCanvas, TableModel
from tkinter import *
from collections import OrderedDict

import view.Estoque as estoque
import view.Produtos as produtos
import view.Clientes as clientes
import view.Marcas as marcas

main = Tk()

mostrarEstoqueBtn = Button(main, text="Mostrar Estoque", command=estoque.mostrar)
mostrarProdutosBtn = Button(main, text="Mostrar Produtos", command=produtos.mostrar)
mostrarClientesBtn = Button(main, text="Mostrar Clientes", command=clientes.mostrar)
mostrarMarcasBtn = Button(main, text="Mostrar Marcas", command=marcas.selecionar)
mostrarEstoqueBtn.pack()
mostrarProdutosBtn.pack()
mostrarClientesBtn.pack()
mostrarMarcasBtn.pack()

main.mainloop()