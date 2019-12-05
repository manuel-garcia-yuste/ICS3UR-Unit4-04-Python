# !/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# this program add number


import random


def main():
    # function makes user guess number

    # variable
    number = random.randint(1, 5)

    # process
    while True:
        # input
        try:
            guess = int(input("Guess the number between 1 and 5: "))
        except ValueError:
            print("Invalid input.")
            break
        if guess == number:
            # output
            print("You got it!")
            break
        else:
            print("You got it wrong!")


if __name__ == "__main__":
    main()
