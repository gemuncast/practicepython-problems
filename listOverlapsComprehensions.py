#Take two lists, say for example these two:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are 
# common between the lists (without duplicates). Make sure your program works on two 
# lists of different sizes. Write this using at least one list comprehension.
#1- Randomly generate two lists to test this

import random

c=[random.randint(1, 100) for i in range (random.randint(1, 15))]
d=[random.randint(1, 100) for i in range (random.randint(1, 15))]
print(c)
print(d)
print(f"{list(set([i for i in c if i in d]))}")