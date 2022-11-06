import math

# --------------------------------------
#
# Sequential input based on a set of options.
#
# --------------------------------------
class InputTree:
  """
  Select an item from list by segmenting
  it in groups and selecting recursively
  until a single item is finally selected.
  """


  def __init__(self, tree=9):
    """
    Constructor.

    Parameters
    ----------
    tree : number
        Number of items to segment choices.
    """
    self.tree = max(min(tree, 9), 2)
    self.history = []
    self.finish = None


  def input(self, choices):
    """
    Fire the input process.

    Parameters
    ----------
    choices : string list
        List of options to choose from.

    Returns
    -------
    string
        The final choice.
    """
    choices = [ x.strip() for x in choices ]

    listSet = sorted(list(set(choices)))

    return self._process(listSet)[0]


  def _print(self, choices):
    """
    Print the choices, depending on if it is still a list
    of possible options or a single item.

    Parameters
    ----------
    choices : list
        List of possible options.
    """
    print()

    # Print will depend on if the list is single element
    # or not
    for i, v in enumerate(choices):
      if len(v) == 1:
        print("%s:  %s" % (i + 1, v[0]))
      else:
        print("%s:  %s - %s" % (i + 1, v[0], v[-1]))

    if len(self.history) > 0:
      print("0:  Go back")


  def _process(self, choices):
    """
    Internal recursive method to process shrinking
    list of options.

    Parameters
    ----------
    choices : list of strings
        Available choices.

    Returns
    -------
    list of strings
        The filtered list of strings.
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

    Returns
    -------
    string
        The input.
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
