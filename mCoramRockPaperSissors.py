# Program name: mCoramMaximumValue.py
# Author: Melissa Coram
# Date last updated: 11/7/2013
# Purpose: Simulates a game of Rock, Paper, Sissors between the user and the computer.

# import the random library module
import random

# Chooses a random number between 1 and 3 to represent the computer's choice and asks
# the user to enter his or her choice.  Process repeats until user wins or loses.
def main():
    # initialize result value (1 = user wins, 2 = computer wins, 3 = tie)
    result = 3
    while result == 3:
        print("Let's play Rock, Papper, Sissors!")
        # generate a random number as computer's choice and assign appropriate value
        # 1 = Rock, 2 = Paper, 3 = Sissors
        comp_random = random.randint(1,3)
        if comp_random == 1:
            comp_choice = 'rock'
        elif comp_random == 2:
            comp_choice = 'paper'
        else:
            comp_choice = 'sissors'
        print("Enter 1 for Rock")
        print("Enter 2 for Paper")
        print("Enter 3 for Sissors")
        # initialize user_choice
        user_choice = 0
        # get user choice and validate input
        while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'sissors':
            user_input = input("Enter your choice: ")
            if user_input == '1' or user_input.lower() == 'rock':
                user_choice = 'rock'
            elif user_input == '2' or user_input.lower() == 'paper':
                user_choice = 'paper'
            elif user_input == '3' or user_input.lower() == 'sissors':
                user_choice = 'sissors'
            else:
                print("Error: Invalid choice")
        # print the computer's choice
        print("Computer's choice:", comp_choice)
        # determine the outcome of the game
        result = get_result(comp_choice, user_choice)
        # display whether the user wins, the computer wins, or if it is a tie
        if result == 1:
            print("User wins!")
        elif result == 2:
            print("Computer wins!")
        else:
            print("It's a tie! Play again!")
    
# Determines the winner.  Rock beats Sissors.  Sissors beats Paper.  Paper beats Rock.
# 1 = Rock, 2 = Paper, 3 = Sissors.  Returns a value to the main program representing
# a win by the user (1), a win by the computer (2), or a tie (3).
def get_result(comp_choice, user_choice):
    if comp_choice == user_choice:
        # user and computer chose the same thing, it's a tie
        return 3
    elif comp_choice == 'rock':
        if user_choice == 'paper':
            # user wins
            return 1
        else:
            # computer wins
            return 2
    elif comp_choice == 'paper':
        if user_choice == 'rock':
            # computer wins
            return 2
        else:
            # user wins
            return 1
    # if the computer chooses sissors
    else:
        if user_choice == 'rock':
            # user wins
            return 1
        else:
            # computer wins
            return 2

    
# Runs the main program.
main()
