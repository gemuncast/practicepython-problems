#Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether 
# they guessed too low, too high, or exactly right.
#1- Keep the game going until the user types “exit”
#2- Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

random_num = random.randint(1, 10)
count = 1

while True:
    guess_num = random.randint(1, 10)
    if random_num == guess_num:
        print("exactly right")
        print(guess_num)
        break
    elif random_num > guess_num:
        print("too high")
    elif random_num < guess_num:
        print("too low")
    elif random_num == "exit":
        break
    count+=1

print(count)