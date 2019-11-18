from tkintertable import TableCanvas, TableModel
from tkinter import *
from collections import OrderedDict

import view.Estoque as estoque
import view.Produto as produtos

main = Tk()

mostrarEstoqueBtn = Button(main, text="Mostrar Estoque", command=estoque.mostrar)
mostrarProdutosBtn = Button(main, text="Mostrar Produtos", command=produtos.mostrar)
mostrarEstoqueBtn.pack()
mostrarProdutosBtn.pack()

main.mainloop()