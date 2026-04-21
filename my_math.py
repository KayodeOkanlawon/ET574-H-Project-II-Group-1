# ===============================
# Student A Functions (Safwan)
# ===============================

def floor(x):
    """
    Function Name: floor
    Purpose: Returns the largest integer less than or equal to x (rounds down).
    Parameters: x (int or float) - the number to floor
    Return Value: int - the largest integer <= x
    """
    if type(x) not in (int, float):
        raise TypeError("Input must be a number")
    
    # If x is already a whole number, return it as int
    if x == int(x):
        return int(x)
    
    # For positive numbers, just chop the decimal
    if x > 0:
        return int(x)
    
    # For negative numbers, chop the decimal then subtract 1
    # e.g. floor(-3.2) should be -4, not -3
    else:
        return int(x) - 1


def hypotenuse(a, b):
    """
    Function Name: hypotenuse
    Purpose: Returns the length of the hypotenuse of a right triangle
             given the lengths of the two other sides, using the
             Pythagorean theorem (c = sqrt(a^2 + b^2)).
    Parameters: a (int or float) - length of first side
                b (int or float) - length of second side
    Return Value: float - the length of the hypotenuse
    """
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both inputs must be numbers")
    if a <= 0 or b <= 0:
        raise ValueError("Side lengths must be positive")
    
    # Calculate a^2 + b^2 without using math module
    sum_of_squares = (a ** 2) + (b ** 2)
    
    # Implement sqrt manually using Newton's method
    guess = sum_of_squares / 2
    for _ in range(1000):
        guess = (guess + sum_of_squares / guess) / 2
    
    return guess

# ===============================
# Student B Functions (Kayode)
# ===============================

def factorial(n):
    """
    Function Name: factorial
    Purpose: Calculates factorial of n
    Parameters: n (int)
    Return Value: int
    """

    if type(n) is not int:
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Input must be non-negative")

    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
def area_of_circle(r):
    """
    Function Name: area_of_circle
    Purpose: Calculates the area of a circle given radius r
    Parameters: r (int or float)
    Return Value: float
    """

    if type(r) not in (int, float):
        raise TypeError("Radius must be a number")

    if r < 0:
        raise ValueError("Radius cannot be negative")

    pi = 3.14159
    area = pi * (r ** 2)

    return area


# ===============================
# Student C Functions (Jordan)
# ===============================
def abs(x):
    """
    Function Name: abs
    Purpose: Returns the absolute value of x (its distance from zero), making it non-negative.
    Parameters: x (int or float) - the number to find the absolute value of
    Return Value: int or float - the non-negative value of x
    """
    if type(x) not in (int, float):
        raise TypeError("Input must be a number")

    # If x is negative, flip the sign
    if x < 0:
        return -x

    # If x is zero or positive, return as is
    return x

def perimeter_of_rectangle(l, w):
    """
    Function Name: perimeter_of_rectangle
    Purpose: Returns the perimeter of a rectangle given its length and width.
    Parameters: l (int or float) - the length of the rectangle
                w (int or float) - the width of the rectangle
    Return Value: int or float - the perimeter of the rectangle (2 * (l + w))
    """
    if type(l) not in (int, float) or type(w) not in (int, float):
        raise TypeError("Input must be a number")

    # Length and width must be positive
    if l <= 0 or w <= 0:
        raise ValueError("Length and width must be greater than zero")

    # Perimeter formula: 2 * (length + width)
    return 2 * (l + w)