#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Sep 2022
# This program lets users guess the number

import constants


def main():
    # this function defines the two possibilities

    # input
    user_guess = int(input("Pick a number between 1-6: "))

    # process
    if user_guess == constants.CORRECT_ANSWER:
        print("You guessed the correct number!")

    if user_guess != constants.CORRECT_ANSWER:
        print("You guessed the wrong number! Try again!")

    print("\nDone.")


if __name__ == "__main__":
    main()
