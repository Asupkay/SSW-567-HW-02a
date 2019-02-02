# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@auther: asupkay
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral')

    def testIsoscelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(5,5,3),'Isosceles')

    def testIsoscelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(3,7,3),'Isosceles')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(13,9,14),'Scalene')

    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(7.7,5,9),'Scalene')

    def testNotTriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,10),'NotATriangle')

    def testNotTriangleB(self): 
        self.assertEqual(classifyTriangle(150,1,1),'NotATriangle')

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(10,False,10),'InvalidInput')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(300,2,2),'InvalidInput')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

