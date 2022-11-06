import math

# --------------------------------------
#
# Sequential input.
#
# --------------------------------------
class InputTree:
  """
  erer
  """


  def __init__(self, tree=9):
    """
    erer
    """
    self.tree = max(min(tree, 9), 2)




  def input(self, choices):
    choices = [ x.strip() for x in choices ]

    listSet = sorted(list(set(choices)))


    return self._process(listSet)


  def _print(self, choices):
    for i, v in enumerate(choices):
      if isinstance(v, list):
        print("%s %s - %s" % (i + 1, v[0], v[-1]))
      else:
        print("%s %s" % (i + 1, v))


  def _process(self, choices):
    if len(choices) == 1:
      return choices[0]

    if len(choices) <= self.tree:
      self._print(choices)

      print()
      a = input()

      return choices[int(a) - 1]

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
    a = input()

    return self._process(blocks[int(a) - 1])
