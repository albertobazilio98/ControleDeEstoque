from tkinter import *

def criar():
  criarWindow = Toplevel()

  clienteSelectFrame = Frame(criarWindow)
  clienteSearchBtn = Button(clienteSelectFrame, text="Buscar Cliente")
  clienteSearchInput = Entry(clienteSelectFrame)

  clienteSearchInput.pack()
  clienteSelectFrame.pack()

  criarWindow.mainloop()