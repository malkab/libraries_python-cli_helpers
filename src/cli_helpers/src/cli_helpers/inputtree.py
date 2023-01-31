import math
from sshkeyboard import listen_keyboard, stop_listening
from .shorten_string import shorten_string
import typing

# --------------------------------------
#
# Sequential input based on a set of options.
#
# --------------------------------------
class InputTree:
  """CLI input to select a value from a list, segmenting the list in groups
  selectable by numbers, allowing for back navigation, until individual elements
  of the list are individually selectable.

  Raises:
      TypeError: When the supplied input to the input method is not a list.
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
    self.minLen: typing.Any = minLen
    self.separator = separator
    self.itemSeparator = itemSeparator
    self.history = []
    self.finish = None
    self.indentation = indentation

    self.keyPressed: typing.Any = None


  # --------------------------------------
  #
  # Main method.
  #
  # --------------------------------------
  def input(self, choices, prompt=None, selection=None) -> typing.Any:
    """
    Fire the input process.

    Args:
        choices (string list): List of options to choose from.
        prompt (string, optional): Optional prompt, defaults to None.
        selection (string, optinal): Prefix message after a selection.
          If None, nothing will be displayed

    Returns:
        string: The final choice.
    """
    # Reset
    self.history = []
    self.finish = None
    self.multiSelected = False

    if not isinstance(choices, list):
      raise TypeError("parameter choices must be a list")

    choices = [ (str(x)).strip() for x in choices ]

    listSet = sorted(list(set(choices)))

    if len(listSet) > 0:
      if prompt and len(listSet) > 1:
        print(prompt)

      out = self._process(listSet)[0]

      if selection:
        print("%s%s" % (selection, out))

      return out

    else:
      return None

  # --------------------------------------
  #
  # Print the choices.
  #
  # --------------------------------------
  def _print(self, choices):
    """
    Print the choices, depending on if it is still a list of possible options or
    a single item.

    Args:
        choices (string list): List of possible options.
    """
    # Print will depend on if the list is single element
    # or not
    if self.multiSelected:
      print()

    # Start adding a blank line to the new selection blocks
    self.multiSelected = True

    for i, v in enumerate(choices):
      if len(v) == 1:
        print("%s%s%s%s" % (" "*self.indentation, i + 1, self.itemSeparator,
          shorten_string(v[0], self.maxLen, self.minLen)))
      else:
        print("%s%s%s%s%s%s" % (" "*self.indentation, i + 1, self.itemSeparator,
          shorten_string(v[0], self.maxLen, self.minLen),
          self.separator,
          shorten_string(v[-1], self.maxLen, self.minLen)))

    if len(self.history) > 0:
      print("%s0%sGo back" % (" "*self.indentation, self.itemSeparator))

  # --------------------------------------
  #
  # Internal recursive method to process shrinking list of options.
  #
  # --------------------------------------
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

      # Ask for option, but taking into account the number of
      # available options
      a = self._inputChoice(len(blocks))

      if isinstance(a, list):
        return a

      else:
        selectedIndex = int(a) - 1

        self.history.append(choices)

        return self._process(blocks[selectedIndex])

  # --------------------------------------
  #
  # Check for key press.
  #
  # --------------------------------------
  def _keyPress(self):
    def press(key):
      self.keyPressed = key
      stop_listening()

    listen_keyboard(
      on_press=press
    )

  # --------------------------------------
  #
  # Input of an option.
  #
  # --------------------------------------
  def _inputChoice(self, lenBlocks):
    """
    Controls the input of the option.

    Returns:
        string: The input.
    """
    while True:
      # o = False

      self._keyPress()

      if self.keyPressed.isnumeric() and self.keyPressed != "":
        if self.keyPressed == "0" and len(self.history) > 0:
          b = self.history.pop()

          return self._process(b)

        # If the pressed number is less than available options, keep in the
        # loop
        if int(self.keyPressed) <= lenBlocks:
          return self.keyPressed
