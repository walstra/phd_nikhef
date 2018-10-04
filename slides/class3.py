#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:36:27 2018
basic class example inheritance
@author: walstra
"""

#our PARENT CLASS
class Polygon:
    def __init__(self, number_of_sides):
        self.n = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]
        
    def inputSides (self):
        self.sides = [float(input("enter sides: " + str(i+1) + " : ")) for i in range(self.n)]
        
    def dispSides(self):
        for i in range(self.n):
            print("Side ", i+1," = " ,self.sides[i])

#a subclass
class Triangle(Polygon):
    def __init__(self):
        super().__init__(3) #!!!!! call the init of the parent class

    def findArea(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return area

if __name__ == "__main__":
    t = Triangle()    
    t.inputSides()
    t.dispSides()
    print("Area: ",t.findArea())    