import math
from utils import shortenString

# --------------------------------------
#
# Sequential input based on a set of options.
#
# --------------------------------------
class InputTree:
  """
  CLI input to select a value from a list, segmenting the list in groups
  selectable by numbers, allowing for back navigation, until individual elements
  of the list are individually selectable.
  """

  def __init__(self, tree=9, maxLen=None, minLen=None, separator=" - ",
    itemSeparator=": "):
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
    """
    self.tree = max(min(tree, 9), 2)
    self.maxLen = maxLen
    self.minLen = minLen
    self.separator = separator
    self.itemSeparator = itemSeparator
    self.history = []
    self.finish = None


  def input(self, choices):
    """
    Fire the input process.

    Args:
        choices (string list): List of options to choose from.

    Returns:
        string: The final choice.
    """
    choices = [ x.strip() for x in choices ]

    listSet = sorted(list(set(choices)))

    return self._process(listSet)[0]


  def _print(self, choices):
    """
    Print the choices, depending on if it is still a list of possible options or
    a single item.

    Args:
        choices (string list): List of possible options.
    """
    print()

    # Print will depend on if the list is single element
    # or not
    for i, v in enumerate(choices):
      if len(v) == 1:
        print("%s%s%s" % (i + 1, self.itemSeparator,
          shortenString(v[0], self.maxLen, self.minLen)))
      else:
        print("%s%s%s%s%s" % (i + 1, self.itemSeparator,
          shortenString(v[0], self.maxLen, self.minLen),
          self.separator,
          shortenString(v[-1], self.maxLen, self.minLen)))

    if len(self.history) > 0:
      print("0:  Go back")


  def _process(self, choices):
    """
    Internal recursive method to process shrinking list of options.

    Args:
        choices (string list): Available choices.

    Returns:
        string list: The filtered list of strings.
    """
    if len(choices) == 1:
      return choices

    else:
      segmentSize = len(choices) / self.tree

      segments = [ math.floor(i/segmentSize) for i, v in enumerate(choices) ]

      currentIndex = -1
      blocks = []
      b = []

      for i in range(0, len(choices)):
        if segments[i] > currentIndex:
          blocks.append(b)
          currentIndex = segments[i]
          b = []

        b.append(choices[i])

      blocks = [ *blocks[1:], b ]

      self._print(blocks)
      print()
      a = self._inputChoice()

      if isinstance(a, list):
        return a

      else:
        selectedIndex = int(a) - 1

        self.history.append(choices)

        return self._process(blocks[selectedIndex])


  def _inputChoice(self):
    """
    Controls the input of the option.

    Returns:
        string: The input.
    """
    o = True

    while o:
      o = False
      a = input()

      if len(a) > 0:
        a = a[0]

        if a.isnumeric() and a != "":
          if a == "0" and len(self.history) > 0:
            b = self.history.pop()

            return self._process(b)

          return a

        else:
          o = True

      else:
        o = True
