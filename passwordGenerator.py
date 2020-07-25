#Write a password generator in Python. Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

import timeit
import random

def main():
    pwd_length =  random.randint(8, 17)
    new_pwd = ""
    while len(new_pwd) < pwd_length:
        random_num = random.randint(33, 127)
        new_pwd+= chr(random_num)
    print(new_pwd)
    print(timeit.timeit())

if __name__ == "__main__":
    main()