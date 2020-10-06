#USE 'py -m unittest TestTriangle' INSTEAD OF 'python -m unittest TestTriangle'
#USE py -m coverage run TestTriangle.py
#Use py -m coverage report
# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Christopher McKenzie
"""

import unittest, math

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testScaleneRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Scalene Right triangle','3,4,5 is a Scalene Right triangle')
    def testScaleneRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene Right triangle','5,3,4 is a Scalene Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral triangle','1,1,1 should be equilateral')
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(50,50,50),'Equilateral triangle','50,50,50 should be equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2,4,4), 'Isosceles triangle', '2,4,4 is an Isosceles triangle')
    def testIsosceleRightTriangle(self):
        self.assertEqual(classifyTriangle(15,15,15*math.sqrt(2)), 'Isosceles Right triangle', '15,15,15*math.sqrt(2) is an Isosceles triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(9,13,14), 'Scalene triangle', '9,13,14 is a Scalene triangle')
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(18,28,39), 'Scalene triangle', '18,28,39 is a Scalene triangle')
    
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

