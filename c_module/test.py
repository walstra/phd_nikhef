'''
\brief Example program which uses the hello module.
'''

import hello

# a Python function
def sum(a,b):
    return a+b

print ("Result from myFunction:", hello.my_set_callback(sum))
hello.say_hello("to all")

