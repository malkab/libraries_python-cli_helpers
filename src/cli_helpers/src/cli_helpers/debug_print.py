# --------------------------------------
#
# Very silly debug print output.
#
# --------------------------------------
def debug_print(descriptor: str, *args: list[str]):
  """A very silly debug print output.

  Args:
      descriptor (str): A general descriptor of the debug print.
      *args (list[str]): A list of messages to print.
  """
  print("\n-----------------------------------------------------")
  print(descriptor)

  for message in args:
    print()
    print(message)

  print("-----------------------------------------------------\n")
