#Ask the user for a string and print out whether this string is a palindrome or not. 

trueP = "alala"
falseP = "nopes"

print(f"{True if trueP == trueP[::-1] else False }")
print(f"{True if falseP == falseP[::-1] else False }")

