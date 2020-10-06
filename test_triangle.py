#USE 'py -m unittest TestTriangle' INSTEAD OF 'python -m unittest TestTriangle'
#USE py -m coverage run TestTriangle.py
#Use py -m coverage report
# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Christopher McKenzie
"""

import unittest
import math
from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):


    """Tests if classify_triangle program is working properly."""


    def test_scalene_right_triangle(self):

        """Scalene Right Triangle tests."""

        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene Right triangle')
        self.assertEqual(classify_triangle(5, 3, 4), 'Scalene Right triangle')

    def test_equilateral_triangle(self):

        """Equilateral Triangle tests."""

        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral triangle')
        self.assertEqual(classify_triangle(50, 50, 50), 'Equilateral triangle')

    def test_isosceles_triangle(self):

        """Tests Isosceles Triangle and Isosceles Right Triangle."""

        self.assertEqual(classify_triangle(2, 4, 4), 'Isosceles triangle')
        self.assertEqual(classify_triangle(15, 15, 15 * math.sqrt(2)), 'Isosceles Right triangle')

    def test_scalene_triangle(self):

        """Tests Scalene Triangle."""

        self.assertEqual(classify_triangle(9, 13, 14), 'Scalene triangle')
        self.assertEqual(classify_triangle(18, 28, 39), 'Scalene triangle')

    def test_invalid_input(self):

        """Tests all invalid inputs."""

        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput')
        self.assertEqual(classify_triangle(-1, 1, 1), 'InvalidInput')
        self.assertEqual(classify_triangle(201, 201, 201), 'InvalidInput')
        self.assertEqual(classify_triangle(2, 2, "two"), 'InvalidInput')

    def test_not_a_triangle(self):

        """Tests inputs that are not valid triangles."""

        self.assertEqual(classify_triangle(1, 1, 3), 'NotATriangle')
        self.assertEqual(classify_triangle(2, 7, 9), 'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
