from tkintertable import TableCanvas, TableModel
from tkinter import *
from collections import OrderedDict

import view.Estoque as estoque

main = Tk()

mostrarEstoqueBtn = Button(main, text="Mostrar Estoque", command=estoque.mostrar)
mostrarEstoqueBtn.pack()

main.mainloop()