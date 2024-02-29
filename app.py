
def fibonacci_loop(n):
  """
  Generates the Fibonacci series up to a given number using a loop.

  Args:
      n: The number up to which the series should be generated.

  Returns:
      A list containing the Fibonacci numbers up to n.
  """

  if n < 0:
    raise ValueError("n must be non-negative")

  if n == 0:
    return []

  elif n == 1:
    return [0]

  fibonacci_series = [0, 1]
  for i in range(2, n + 1):
    next_number = fibonacci_series[i - 2] + fibonacci_series[i - 2]
    #if next_number != 0:
    fibonacci_series.append(next_number)
#this is a edited fibonacci series where instead of adding the last two numbers, we just add the 2nd last number twice
#which gives 2 to the power of n, also zeroes  are not included
  return fibonacci_series

# Example usage
n = int(input("Enter the number up to which you want the Fibonacci series: "))
fibonacci_series = fibonacci_loop(n)
print("Fibonacci series up to", n, ":", fibonacci_series)
