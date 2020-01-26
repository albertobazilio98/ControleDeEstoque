from tkintertable import TableCanvas, TableModel, Filtering
from tkinter import *
from tkinter import ttk
import datetime
from collections import OrderedDict

def filtro(table, column, value):
  names = Filtering.doFiltering(table.model.filterBy, filters=[(column, value, "contains", "and")])
  table.model.filteredrecs = names
  table.filtered = True
  table.redrawTable()

def criarBuscarFrame(parent, table):
  # Frame de busca
  def buscar():
    filtro(table, colSelect.get(), buscaInput.get())

  buscaFrame = Frame(parent)
  buscaInput = Entry(buscaFrame)
  buscaBtn = Button(buscaFrame, text="Buscar", command=buscar)
  colSelect = ttk.Combobox(buscaFrame, values=table.model.columnNames)
  colSelect.pack(side=LEFT)
  buscaInput.pack(side=LEFT)
  buscaBtn.pack(side=LEFT)

  return buscaFrame

def criarDateSelectorFrame(parent):
  def getDate():
    dateSelectorFrame.date = "{}-{}-{}".format(anoSelector.get(),mesSelector.get(),diaSelector.get())
  dateSelectorFrame = Frame(parent)
  diaSelector = ttk.Combobox(dateSelectorFrame, values = [(I + 1) for I in range(31)])
  mesSelector = ttk.Combobox(dateSelectorFrame, values = [(I + 1) for I in range(12)])
  anoSelector = ttk.Combobox(dateSelectorFrame, values = [(I + 2019) for I in range(10)])
  selectBtn = Button(dateSelectorFrame, text="escolher data", command=getDate)
  diaSelector.pack(side=LEFT)
  mesSelector.pack(side=LEFT)
  anoSelector.pack(side=LEFT)
  selectBtn.pack(side=LEFT)

  return dateSelectorFrame

def criarValidadeSelectorFrame(parent):
  def getDate():
    dateSelectorFrame.date = "{}-{}-1".format(anoSelector.get(),mesSelector.get())
  dateSelectorFrame = Frame(parent)
  mesSelector = ttk.Combobox(dateSelectorFrame, values = [(I + 1) for I in range(12)])
  anoSelector = ttk.Combobox(dateSelectorFrame, values = [(I + 2019) for I in range(10)])
  selectBtn = Button(dateSelectorFrame, text="escolher data", command=getDate)
  mesSelector.pack(side=LEFT)
  anoSelector.pack(side=LEFT)
  selectBtn.pack(side=LEFT)

  return dateSelectorFrame

# parsers e formaters

def formatedMoney(money):
  return ("R$ " + str(money)).replace('.',',')

def formatedDate(date):
  return '/'.join((str(date).split('-'))[::-1])

def formatedExpirationDate(date):
  return formatedDate(date)[3:]

def moneyParser(money):
  return money.replace(',', '.')

def dateParser(date):
  date = date.split('/')
  date[-1] = "20" + date[-1]
  return '-'.join(date[::-1])

def expirationDateParser(date):
  return dateParser("01/" + date)