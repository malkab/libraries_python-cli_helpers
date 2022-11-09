# --------------------------------------
#
# Shortens a string and adapt it to a
# min / max length
#
# --------------------------------------
def shortenString(string, maxLen, minLen=0):
  """
  Shortens (and optionally pads) a string to a given length.

  Args:
      string (string): The string to process.
      maxLen (int): The max length.
      minLen (int, optional): The min length. Defaults to 0.

  Returns:
      string: The modified string.
  """
  if maxLen == None:
    return string

  if minLen < maxLen:
    minLen = maxLen

  if len(string) > maxLen:
    s = string[:maxLen-3]+"..."
  else:
    s = string

  if len(s) < minLen:
    fs = "%s%s" % (s, " "*(minLen - len(s)))
  else:
    fs = s

  return fs
