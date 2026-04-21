import unittest
from my_math import factorial, area_of_circle

# ==========================================
# Student A Tests for Student B (Safwan)
# ==========================================

class TestFactorial(unittest.TestCase):

    def test_factorial_typical(self):
        # Typical case - 5! = 120
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        # Edge case - 0! is defined as 1
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        # Invalid input - negative numbers not allowed
        with self.assertRaises(ValueError):
            factorial(-1)


class TestAreaOfCircle(unittest.TestCase):

    def test_area_typical(self):
        # Typical case - radius 1, area should be ~3.14159
        self.assertAlmostEqual(area_of_circle(1), 3.14159, places=4)

    def test_area_zero_radius(self):
        # Edge case - radius 0 should return 0
        self.assertAlmostEqual(area_of_circle(0), 0.0, places=4)

    def test_area_negative_radius(self):
        # Invalid input - negative radius not allowed
        with self.assertRaises(ValueError):
            area_of_circle(-5)