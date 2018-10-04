#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:36:27 2018
basic class example
@author: walstra
"""
import datetime 

class UniversityPerson:
    
    def __init__(self, name, email, address, city, telephone, birthdate):
        self.name = name
        self.email = email
        self.address = address
        self.city = city
        self.telephone = telephone
        self.birthdate = birthdate
        
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, 
                                 self.birthdate.day):
            age -= 1
        return age    


if __name__ == "__main__":
    p = UniversityPerson("John", "j.doe@univ.nl",\
                     "12, Short Street", \
                     "Amsterdam","06 12345678", \
                     datetime.date(1992,3,12))        

    print("age:", p.age())     
        
