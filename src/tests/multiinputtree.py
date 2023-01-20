import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cli_helpers.src.cli_helpers import MultiInputTree


TODO: HACERLO CON UN DICCIONARIO ANIDADO Y QUE EL PATH SEAN LAS PROPIAS CLAVES

c= {
  "A": {
    "B": {
      "C": 0,
      "D": 1
    },
    "E": {
      "F": 2,
    }
  },
  "H": {
    "I": 3,
  }
}

c = [
  [ "A" ],

  [ "B" ],

  [ "C" ],

  [ "D" ],

  [ "E" ],

  [ "F" ],

  [ "G", "H" ],
  [ "I", "J" ]
]

mit = MultiInputTree(tree=9, separator="", maxLen=20, minLen=5, itemSeparator="  ")

# a = InputTree().input(c)

# print("Choice: %s" % a)

mit.history(c, [ 0, 0, 0, 0, 0, 0, 0, 1, 1 ])
