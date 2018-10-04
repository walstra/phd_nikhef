#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 10:22:19 2018
Properties example
@author: tacowalstra
"""

class TemperatureControl:
    def __init__(self,temp = 0):
        self.temperature = temp
        
        
    def getTemperature(self):
        print("Getting temperature: ", self.__temperature)
        return self.__temperature
    
    def setTemperature(self, value):
        if value < -273.0:
            print("Cannot set the temperature below -273C")
            return
        print("Setting the temperature to: ", value)
        self.__temperature = value
    
    temperature = property(getTemperature, setTemperature)
    #property (fGet, fSet, fDel, fDoc)
    
if __name__ == "__main__":
    t = TemperatureControl()
    t.temperature
    t.temperature  = -81.9