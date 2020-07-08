#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#1 If the number is a multiple of 4, print out a different message.
#2 Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("enter a number :"))
check = int(input("enter a number :"))

if num%2==0:
    if num%4==0:
        print(f"{num} is even and multiple of 4!")
    else :
        print(f"{num} is even")
else :
    print(f"{num} is odd")

if num%check == 0:
    print(f"{num} is multiple of {check}!!!")
else :
    print(f"{num} is not a multiple of {check}")