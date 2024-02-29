import unittest
from spiral import fibonacci, draw_fibonacci_spiral  # Replace with your script name

class TestFibonacci(unittest.TestCase):
  def test_fibonacci_base_cases(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)

  def test_fibonacci_positive_values(self):
    self.assertEqual(fibonacci(5), 5)
    self.assertEqual(fibonacci(10), 55)

  def test_fibonacci_negative_values(self):
    with self.assertRaises(ValueError):
      fibonacci(-1)

class TestDrawFibonacciSpiral(unittest.TestCase):
  def test_draw_fibonacci_spiral(self):
    # Simulate drawing the spiral and assert the expected behavior
    # (difficult to directly test drawing functionality)
    draw_fibonacci_spiral(5, 90)  # Call the function with example values

if __name__ == '__main__':
  unittest.main()