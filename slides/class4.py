#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 09:53:59 2018
constructor of a Python class
@author: tacowalstra
"""

class Point(object):
    __maxInst = 4
    __instCreated = 0
    def __new__(cls, *args, **kwargs):
        print("Inside the function 'new'")
        if cls.__instCreated >= cls.__maxInst:
            print("Cannot create a more instances")
            return -1
        cls.__instCreated += 1
        obj = super().__new__(cls)
        return obj
    
    def __init__(self, x, y):
        print("Inside the function 'init'")
        self.x = x
        self.y = y
        
    def distance(self):
        return(self.x**2 + self.y**2)**0.5
        
if __name__ == "__main__":
    p1 = Point(3,4)
    p2 = Point(3,4)    
    p3 = Point(3,4)    
    p4 = Point(3,4)    
    p5 = Point(3,4)    
    
    print("distance: ",p1.distance())
            