#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("ingrese number: "))
new_array = []
for i in range (1,num+1):
    if num%i==0:
        new_array.append(i)

print(new_array)

print(f"{[i for i in range (1,num+1) if num%i==0]}")