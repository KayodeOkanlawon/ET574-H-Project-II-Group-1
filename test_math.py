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

    def test_floor_edge(self):
        self.assertEqual(floor(5), 5)

    def test_floor_negative(self):
        self.assertEqual(floor(-3.2), -4)


class TestPerimeter(unittest.TestCase):
    def test_perimeter_normal(self):
        self.assertEqual(perimeter_of_rectangle(5, 3), 16)

    def test_perimeter_edge(self):
        self.assertEqual(perimeter_of_rectangle(1, 1), 4)

    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter_of_rectangle(-2, 3)
            
            
#==========================================
# Student C Tests for Student A & B (Jordan)
# ==========================================

# Test cases for Student A's function (Safwan)
class TestHypotenuse(unittest.TestCase):
    def test_hypotenuse_typical(self):
        # Typical case - 3, 4, 5 right triangle
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)

    def test_hypotenuse_larger(self):
        # Typical case - 5, 12, 13 right triangle
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_hypotenuse_negative(self):
        # Invalid input - negative side length not allowed
        with self.assertRaises(ValueError):
            hypotenuse(-1, 4)


# Test cases for Student B's function (Kayode)
class TestAreaOfCircle(unittest.TestCase):
    def test_area_typical(self):
        # Typical case - radius of 5
        self.assertAlmostEqual(area_of_circle(5), 78.53975)

    def test_area_zero(self):
        # Edge case - radius of 0 should return 0
        self.assertAlmostEqual(area_of_circle(0), 0.0)

    def test_area_negative(self):
        # Invalid input - negative radius not allowed
        with self.assertRaises(ValueError):
            area_of_circle(-3)   