from tkintertable import TableCanvas, TableModel
from tkinter import *
from collections import OrderedDict

import view.config as db

import view.Estoque as estoque
import view.Produtos as produtos
import view.Clientes as clientes
import view.Marcas as marcas

# teste, remover dps
data = {'a': '0.25', 'b': "0.26", 'c': 0.6, 'd': 0.88, 'e': 0.78}
data = str(data)
main = Tk()

table = db.listarTudoTabela("Produto")
print(table)

mostrarEstoqueBtn = Button(main, text="Mostrar Estoque", command=estoque.mostrar)
mostrarProdutosBtn = Button(main, text="Mostrar Produtos", command=produtos.mostrar)
mostrarClientesBtn = Button(main, text="Mostrar Clientes", command=clientes.mostrar)
mostrarMarcasBtn = Button(main, text="Mostrar Marcas", command=marcas.mostrar)
mostrarEstoqueBtn.pack()
mostrarProdutosBtn.pack()
mostrarClientesBtn.pack()
mostrarMarcasBtn.pack()

main.mainloop()