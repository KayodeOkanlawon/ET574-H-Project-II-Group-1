import unittest
from my_math import factorial, abs, floor, perimeter_of_rectangle

# ==========================================
# Student A Tests for Student B & C (Safwan)
# ==========================================

# Test cases for Student B's function (Kayode)
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

# Test cases for Student C's function (Jordan)
class TestAbs(unittest.TestCase):

    def test_abs_negative(self):
        # Typical case - negative number becomes positive
        self.assertEqual(abs(-5), 5)

    def test_abs_zero(self):
        # Edge case - zero should return zero
        self.assertEqual(abs(0), 0)

    def test_abs_string_input(self):
        # Invalid input
        with self.assertRaises(TypeError):
            abs("hello")

# ===============================
# Student B Tests (Kayode)
# Testing: Student A and Student C functions
# ===============================

class TestFloor(unittest.TestCase):
        def test_floor_normal(self):
        self.assertEqual(floor(3.7), 3)