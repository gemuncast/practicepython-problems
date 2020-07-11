#Ask the user for a number and determine whether the number is prime or not. 

import random

random_num = random.randint(2, 100)
print(random_num)
count=0
for i in range(2, random_num):
    if random_num%i == 0:
        count+=1
        break
if count==0:
    print("prime")
else:
    print("not prime")



#this is a very bad solution, it should be better try ti divide number by 2,3,5,7 and 11