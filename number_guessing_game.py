#!/usr/bin/env python3
# Created by Artur Grigoryev
# Created on May 20, 2021
# This file runs the number guessing game


def main():
    # Function that runs the game
    my_number = 5
    print("Welcome to guess the number!\n")
    # User input
    user_number = int(input("Input a number from 0-9: "))
    # Process
    if user_number == my_number:
        # Output
        print("You have guessed the correct number!")
    else:
        print("Try again next time!")


if __name__ == "__main__":
    main()
