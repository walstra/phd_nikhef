#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:36:27 2018
basic class example
@author: walstra
"""
class Polygon:
    __maxSides = 5 #private variable!!
    __myprivVar = 8
    def __init__(self, number_of_sides):
        if number_of_sides >self.__maxSides:
            print("Number of sides > 5")
            return -1
        self.n = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]
        
    def inputSides (self):
        self.sides = [float(input("enter sides: " + str(i+1) + " : ")) for i in range(self.n)]
        
    def dispSides(self):
        for i in range(self.n):
            print("Side ", i+1," = " ,self.sides[i])

if __name__ == "__main__":
    p1 = Polygon(5)
    #print(p1.__myprivVar)
    print("Number of sides: ", p1.n)
 
    p1.n = 6
    p1.inputSides()
    print(p1.dispSides())
