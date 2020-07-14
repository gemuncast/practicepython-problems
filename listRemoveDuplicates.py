#Write a program (function!) that takes a list and returns a new list 
# that contains all the elements of the first list minus all the duplicates.
#1- Write two different functions to do this - one using a loop and constructing a list, and another using sets.

import random

def LRDloop(my_array):
    new_array = []    
    for i in range(0,len(my_array)):
        if my_array[i] not in new_array:
            new_array.append(my_array[i])
    return new_array
    
def LRDset(my_array):
    return list(set([i for i in my_array]))


a = [1, 1, 2, 5, 3, 5, 8, 13, 89, 1, 21, 34, 55, 89]

print(LRDset(a))
print(LRDloop(a))