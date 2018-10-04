#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:08:44 2018
inheritance with function override
@author: tacowalstra
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
        super().__init__(3)

    def dispSides(self): #OVERRIDED FUNCION!!!!
        print("Overriding dispSides function")
        for i in range(3):
            print("Side ", i+1," = " ,self.sides[i])

if __name__ == "__main__":
    t = Triangle()    
    t.inputSides()
    t.dispSides()
    