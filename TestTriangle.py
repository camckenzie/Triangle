#USE 'py -m unittest TestTriangle' INSTEAD OF 'python -m unittest TestTriangle'
# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(50,50,50),'Equilateral','50,50,50 should be equilateral')

    def testIsosceleTriangleA(self):
        self.assertEqual(classifyTriangle(2,4,4), 'Isosceles', '2,4,4 is an Isosceles triangle')
    def testIsosceleTriangleB(self):
        self.assertEqual(classifyTriangle(8,8,3), 'Isosceles', '8,8,3 is an Isosceles triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(9,13,14), 'Scalene', '9,13,14 is a Scalene triangle')
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(18,28,39), 'Scalene', '18,28,39 is a Scalene triangle')
    
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput', '0,0,0 is an invalid input')
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-1,1,1), 'InvalidInput', '-1,-1,-1 is an invalid input')
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(201,201,201), 'InvalidInput', '201,201,201 is an invalid input')
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(2,2,"two"), 'InvalidInput', '2,2,two is an invalid input')
        
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,1,3), 'NotATriangle', '1,1,3 is not a triangle')
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(2,7,9), 'NotATriangle', '2,7,9 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

