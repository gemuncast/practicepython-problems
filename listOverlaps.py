#write a program that returns a list that contains only the elements that are 
# common between the lists (without duplicates). Make sure your program works on 
# two lists of different sizes.
#Extras
#1-Randomly generate two lists to test this
#2-Write this in one line of Python

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(f"solution for #1 and #3 : \n{list(set([i for i in a if i in b]))}")

c = [random.randint(1, 10) for i in range (random.randint(1, 10))] 
d = [random.randint(1, 10) for i in range (random.randint(1, 10))]
print(f"solution for #2\n{c}\n{d}")
print(f"{list(set([i for i in c if i in d]))}")