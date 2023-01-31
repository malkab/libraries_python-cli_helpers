import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cli_helpers.src.cli_helpers.inputtree import InputTree

c = [
  "Agua",
  "Agua 0",
  "Agua 1",
  "Agua 2",
  "Agua 3",
  "Agua 4",
  "Agua 5",
  "Agua 6",
  "Agua 7",
  "Banana",
  "Alcornoque",
  "Alcornoque",
  "Alcornoque",
  "Alcornoque A",
  "Alcornoque B",
  "             Alcornoque C      ",
  "Alcornoque D",
  "Alcornoque E",
  "Alcornoque",
  "Batidora",
  "Docena",
  "Dulce",
  "Ejercicio",
  "Esmero",
  "Frenadol",
  "Gaita",
  "Carcabuey",
  "3j3jj2",
  "mmemrwe",
  "88j23j4",

]

a = InputTree(tree=9, separator="", maxLen=20, minLen=5, itemSeparator="  ").input(c)

# a = InputTree().input(c)

print("Choice: %s" % a)
