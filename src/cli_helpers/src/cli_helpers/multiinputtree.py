from .inputtree import InputTree

# --------------------------------------
#
# Multiple input tree: an array goes to another array and so on.
# It is based and uses the InputTree class.
#
# --------------------------------------
class MultiInputTree():

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


  def input(self, choices: dict, prompt=None, selection=None):
    # To store the sequence of choices
    choicesHistory: list(str) = []

    print("D: A", choices)
    print("D: B", self.dictSearch(choices, ["A", "B", "C", 1]))

    # Check dictionary keys, first level
    print("D: ", choices.keys())

    # history: list[int] = []

    it: InputTree = InputTree(tree=self.tree, maxLen=self.maxLen, minLen=self.minLen,
      separator=self.separator, itemSeparator=self.itemSeparator, indentation=self.indentation)

    a = it.input(list(choices.keys()))




  def history(self, choices: list[list[str]], history: list[int],
    pointer: int = 0, start: int = 0, values: list[str] = []) -> None:

    values.append(choices[start + history[pointer]][history[pointer]])

    # if pointer == 0:
    #   start = 1
    # else:
    #   for i in range(start, start + len(choices[pointer - 1])):
    #     start += len(choices[i])

    #   start -= 1

    self.history(choices, history, pointer + 1, start, values)




  def dictSearch(self, d: dict, path: list[str]) -> any:
    print("D: ", 0)

    elem = d

    for x in path:
      if type(elem) is list:
        elem = elem[x]
      else:
        elem = elem.get(x)

    return elem
