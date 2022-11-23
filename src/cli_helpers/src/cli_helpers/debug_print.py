# --------------------------------------
#
# Very silly debug print output.
#
# --------------------------------------
def debug_print(descriptor, *args):
  """A convenient debug print"""
  print("\n-----------------------------------------------------")
  print(descriptor)

  for message in args:
    print()
    print(message)

  print("-----------------------------------------------------\n")
