import turtle

def fibonacci(n):
  """
  Calculates the nth Fibonacci number.

  Args:
      n: The index of the Fibonacci number to be calculated.

  Returns:
      The nth Fibonacci number.
  """
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

def draw_fibonacci_spiral(n, angle):
  """
  Draws the Fibonacci spiral using the Turtle graphics library.

  Args:
      n: The number of iterations (length of the spiral).
      angle: The turning angle between squares.
  """
  t = turtle.Turtle()
  t.speed(0)  # Set turtle speed to fastest

  for i in range(n):
    side_length = fibonacci(i)
    t.forward(side_length)
    t.right(angle)
    t.left(3 * angle / 2)  # Turn  right and then left by 60 degrees

  # Hide the turtle and keep the window open
  t.hideturtle()
  turtle.done()

# Example usage
n = int(input("Enter the number of iterations: "))
angle = int(input("Enter the turning angle between squares (degrees): "))
draw_fibonacci_spiral(n, angle)
