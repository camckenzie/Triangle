# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple python program
to classify triangles.

@author: Christopher McKenzie
"""

import math

def classify_triangle(side_a, side_b, side_c):
    """
    The program determines if the triangle is Scalene, Isosceles, or
    Equilateral, and if it is Right. If the inputs are invalid or do not
    create a valid triangle, an error message is returned.
    """

    # Verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if isinstance(side_a, str) or isinstance(side_b, str) or isinstance(side_c, str):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if side_a > 200 or side_b > 200 or side_c > 200:
        return 'InvalidInput'

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (side_a >= (side_b + side_c)) or \
        (side_b >= (side_a + side_c)) or \
        (side_c >= (side_a + side_b)):
        return 'NotATriangle'

    triangle: str = ""

    if side_a == side_b and side_b == side_a and side_b == side_c:
        triangle += 'Equilateral'
    #elif side_a != side_b and side_b != side_c and side_a != side_b:
    elif side_a not in (side_b, side_c) and \
        side_b not in (side_a, side_c) and \
        side_c not in (side_a, side_b):
        triangle += 'Scalene'

    else:
        triangle += 'Isosceles'

    #Conditions for Isosceles Right Triangle
    irt_a: bool = side_a == side_b and side_c == side_a * math.sqrt(2)
    irt_b: bool = side_a == side_c and side_b == side_a * math.sqrt(2)
    irt_c: bool = side_b == side_c and side_a == side_b * math.sqrt(2)

    if irt_a is True or \
        irt_b is True or \
        irt_c is True:
        return 'Isosceles Right triangle'

    if ((side_a ** 2) + (side_b ** 2)) == (side_c ** 2) or \
        ((side_b ** 2) + (side_c ** 2)) == (side_a ** 2) or \
        ((side_c ** 2) + (side_a ** 2)) == (side_b ** 2):
        triangle += ' Right'

    triangle += ' triangle'
    return triangle
