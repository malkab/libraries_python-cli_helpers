import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cli_helpers.src.cli_helpers.multiinputtree import MultiInputTree

c= {
  "A": {
    "B": {
      "C": [ 0, 1, 2 ],
      "D": [ 3, 4, 5 ]
    },
    "E": {
      "F": [ 6, 7, 8 ],
    }
  },
  "H": {
    "I": [ 9, 10 ],
  }
}

mit = MultiInputTree(tree=9, separator="", maxLen=20, minLen=5, itemSeparator="  ")

mit.input(c, prompt="\nSelect: ", selection="Good choice! ")
