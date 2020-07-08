# Character Input

name = input("your name: ")
age = 2020 + (100 - int(input("your age: ")))
copies = int(input("how many times: "))

for i in range (copies):
    print(f"\n{name} you will turn 100 years the year {age}")