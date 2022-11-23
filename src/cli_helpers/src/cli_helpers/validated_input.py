def validated_input(prompt=None, validation=None, default=None):
  """
  Validated input, with optional validator.

  Args:
      prompt (string, optional): Prompt. Defaults to None.
      validation (lambda, optional): Lambda function to validate input. Defaults to None.
      default (string, optional): If exists, value will be returned if validation is not passed. Defaults to None.

  Returns:
      string: The input string result.
  """

  # Define a default validation that just returns True
  if not validation:
    validation = lambda x: True

  # Repeat until validation is passed
  while True:
    out = input(prompt)

    try:
      if validation(out):
        return out
      else:
        if default:
          return default
    except:
      if default:
        return default
