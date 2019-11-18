from tkintertable import TableCanvas, TableModel
from tkinter import *
from collections import OrderedDict

import view.Estoque as estoque
import view.Produtos as produtos
import view.Clientes as clientes

main = Tk()

mostrarEstoqueBtn = Button(main, text="Mostrar Estoque", command=estoque.mostrar)
mostrarProdutosBtn = Button(main, text="Mostrar Produtos", command=produtos.mostrar)
mostrarClientesBtn = Button(main, text="Mostrar Clientes", command=clientes.mostrar)
mostrarEstoqueBtn.pack()
mostrarProdutosBtn.pack()
mostrarClientesBtn.pack()

main.mainloop()