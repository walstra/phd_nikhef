import random

def display_list(l):
   for value in l:
        print("**" * value)
   input("")

def bubblesort(l):
    for left in range(len(l)-1,0,-1):
        for i in range(left):
            if l[i] < l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
        display_list(l)
    return l

l = [random.randrange(1,50) for i in range(1,20)]
print(l)
import pdb; pdb.set_trace()
bubblesort(l)
print(l)

