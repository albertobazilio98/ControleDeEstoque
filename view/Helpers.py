from tkintertable import TableCanvas, TableModel, Filtering
from collections import OrderedDict

def buscar(table, column, value):
  names = Filtering.doFiltering(table.model.filterBy, filters=[(column, value, "contains", "and")])
  table.model.filteredrecs = names
  table.filtered = True
  table.redrawTable()