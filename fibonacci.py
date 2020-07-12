#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#Take this opportunity to think about how you can use functions. 
#Make sure to ask the user to enter the number of numbers in the sequence to generate.

def fibo(my_num):
    if my_num > 1 :
        return fibo(my_num-1) + fibo(my_num - 2)
    elif my_num == 1:
        return 1
    elif my_num == 0 :
        return 0

print(fibo(1))