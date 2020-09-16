# -*- coding: utf-8 -*-
"""
Description:
The primary goal of this file is to demonstrate a simple python program
to classify triangles.

@author: Christopher McKenzie

Results:
I fixed the classifyTriangle function and all of the
predefine tests, along with my additional tests, passed.

Reflection:
This was the first time I had been given buggy code to fix and at least
for this assignment, it came easily to me. I already had many different
ideas of how to break the code from the previous assignments, so I did
not run into any problems; everything worked. Also, it was my first
time using bash to run Python code, so I was glad to finally be given
the opportunity to do so.

Honor Pledge:
I pledge my honor that I have abided by the Stevens Honor System.

Detailed Results:
My technique was simply testing the program first to see what errors
occurred. Then, since the program was small, I added print statements
by the error statements to see which ones were triggered. From there,
I read carefully through the program to catch any errors. 

I assumed that the correct number of parameters were always entered,
and that there could not be an Isosceles Right Triangle or a Scalene
Triangle.

My test inputs included 2 examples of every type of triangle, and 2
different examples of how to initiate each error condition specified.

My tests and their results confirmed that I had fixed the buggy
classifyTriangle program, and that it could accurately classify
a triangle.
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
         
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or \
        ((b ** 2) + (c ** 2)) == (a ** 2) or \
        ((c ** 2) + (a ** 2)) == (b ** 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isosceles'
