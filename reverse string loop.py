def reverse_string_loop(s):
  """Reverses a string using a loop."""
  reversed_s = ""
  for char in s:
    reversed_s = char + reversed_s  # Prepend each character
  return reversed_s

# Example usage
my_string = "python"
reversed_string = reverse_string_loop(my_string)
print(f"Original: {my_string}, Reversed: {reversed_string}")
