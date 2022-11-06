import math

# --------------------------------------
#
# Sequential input based on a set of options.
#
# --------------------------------------
class InputTree:
  """

  Docstring

  Attributes
  ----------
  exposure : float
      Exposure in seconds.

  Methods
  -------
  colorspace(c='rgb')
      Represent the photo in the given colorspace.
  gamma(n=1.0)
      Change the photo's gamma exposure.

  """

  def __init__(self, tree=9):
    """
    Docstring

    Parameters
    ----------
    var : type
        Doc

    Returns
    -------
    var
        Doc

    """
    self.tree = max(min(tree, 9), 2)
    self.history = []
    self.finish = None



  def input(self, choices):
    choices = [ x.strip() for x in choices ]

    listSet = sorted(list(set(choices)))

    return self._process(listSet)[0]





  def _print(self, choices):

    for i, v in enumerate(choices):
      if isinstance(v, list):
        print("%s:  %s - %s" % (i + 1, v[0], v[-1]))
      else:
        print("%s:  %s" % (i + 1, v))

    if len(self.history) > 0:
      print("\n0:  Go back")





  def _process(self, choices):

    print()
    print("D: 4444", choices)
    print()

    if len(choices) == 1:
      return choices

    # elif len(choices) <= self.tree:
    #   self._print(choices)

    #   print()
    #   a = self._inputChoice()

    #   return choices[int(a) - 1]

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

      print("D: JJJJJ", a)

      if isinstance(a, list):

        return a

      else:

        selectedIndex = int(a) - 1

        self.history.append(choices)

        return self._process(blocks[selectedIndex])






  def _inputChoice(self):
    a = input()

    if a == "0" and len(self.history) > 0:
      b = self.history.pop()

      return self._process(b) #self.history.pop())

    return a
