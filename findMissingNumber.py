def find_missing_number(sequence):
  """
  Finds the missing number in a sorted sequence of consecutive integers, assuming there is only one missing number.

  Args:
      sequence: A sorted list of consecutive integers with one missing number.

  Returns:
      The missing number, or -1 if the sequence is not valid.
  """
  if len(sequence) < 2:
    return -1  # Sequence is too short to be valid

  # Handle cases where the missing number is at the beginning or end
  if sequence[0] != 1:
    return sequence[0] - 1  # Missing number at the beginning
  if sequence[-1] != len(sequence):
    return len(sequence)  # Missing number at the end

  # Calculate expected difference and check for potential invalid sequence (non-consecutive elements)
  expected_difference = sequence[-1] - sequence[0]
  for i in range(1, len(sequence)):
    if sequence[i] != sequence[i - 1] + 1:
      return -1  # Invalid sequence (non-consecutive elements)

  return -1  # No missing number found (valid consecutive sequence)

# Example usage
sequence = [1, 3, 4, 5, 7]
missing_number = find_missing_number(sequence)
if missing_number != -1:
  print("The missing number in the sequence is:", missing_number)
else:
  print("The sequence is valid or has multiple missing numbers.")
