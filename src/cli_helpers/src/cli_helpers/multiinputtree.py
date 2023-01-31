from .inputtree import InputTree

# --------------------------------------
#
# Multiple input tree: an array goes to another array and so on.
# It is based and uses the InputTree class.
#
# It accepts a dictionary with the following structure:
#
# ```Python
# c= {
#   "A": {
#     "B": {
#       "C": [ 0, 1, 2 ],
#       "D": [ 3, 4, 5 ]
#     },
#     "E": {
#       "F": [ 6, 7, 8 ],
#     }
#   },
#   "H": {
#     "I": [ 9, 10 ],
#   }
# }
# ```
# --------------------------------------
class MultiInputTree():
  """This class allows to select an item from a dictionary with multiple levels,
  using the class InputTree to drive the selection process. It accept the
  same options as the InputTree class.

  The choices dictionary must have the following structure:

  ```Python
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
  ```

  Example code:

  ```Python
  c: dict = {
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

  mit: MultiInputTree = MultiInputTree(tree=9, separator="", maxLen=20,
    minLen=5, itemSeparator="  ")

  a: int = mit.input(c)
  ```
  """

  def __init__(self, tree=9, maxLen=None, minLen=None, separator=" - ",
    itemSeparator=": ", indentation=0):
    """
    Constructor.

    Args
        tree (int, optional): Number of groups to use while asking for inputs.
        Defaults to 9, minimum of 2.
        maxLen (int, optional): Max length of items. Defaults to None.
        minLen (int, optional): Min length of items. Defaults to None.
        separator (str, optional): Separator of items. Defaults to " - ".
        itemSeparator (str, optional): Separator between the item number and the
        options. Defaults to ": ".
        indentation (int, optional): Number of spaces to indent. Defaults to 0.
    """
    self.tree = max(min(tree, 9), 2)
    self.maxLen = maxLen
    self.minLen = minLen
    self.separator = separator
    self.itemSeparator = itemSeparator
    self.finish = None
    self.indentation = indentation

    self.keyPressed = None

  # --------------------------------------
  #
  # Input function to start the whole process.
  #
  # --------------------------------------
  def input(self, choices: dict, prompt=None, selection=None) -> any:
    """Launches the selection process.

    "choices" is a dictionary with the following structure:

    ```Python
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
    ```

    Args:
        choices (dict): The dictionary with the choices.
        prompt (string, optional): Optional prompt, defaults to None.
        selection (string, optinal): Prefix message after a selection.
          If None, nothing will be displayed

    Returns:
        any: The final choice.
    """
    # To store the sequence of choices
    dict_search_path: list(str) = []

    # An InputTree instance
    it: InputTree = InputTree(tree=self.tree, maxLen=self.maxLen,
      minLen=self.minLen, separator=self.separator,
      itemSeparator=self.itemSeparator, indentation=self.indentation)

    # Get the first item in the path
    current_item = self._dict_search(choices, dict_search_path)

    # Search while there is a next item in the path
    while current_item is not None:

      # If the current item in the path is a list, we have reached the end.
      # Get the last option and bail out of the loop.
      if isinstance(current_item, list):
        final_item = it.input(current_item, prompt=prompt, selection=selection)
        break

      else:
        # If not, there must be another dict. Get keys and keep searching.
        dict_search_path.append(it.input(list(current_item.keys()), prompt=prompt))

        # Get the next item in the path for the next loop
        current_item = self._dict_search(choices, dict_search_path)

    # Return the final item
    return final_item



  # --------------------------------------
  #
  # Searches inside a dictionary using a path of keys.
  #
  # --------------------------------------
  def _dict_search(self, d: dict, path: list[str]) -> any:
    """Searches for a value in a dictionary using a path of keys.
    If the last element of the path is an integer, it will be used as an index
    to search in a list.

    If the path is an empty list, the dictionary itself will be returned.

    Args:
        d (dict): The dict to search into.
        path (list[str]): The path of keys to search.

    Returns:
        any: The value found.
    """
    elem = d

    for x in path:
      if type(elem) is list:
        elem = elem[x]
      else:
        elem = elem.get(x)

    return elem
