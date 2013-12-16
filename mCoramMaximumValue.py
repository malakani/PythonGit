# Program name: mCoramMaximumValue.py
# Author: Melissa Coram
# Date last updated: 11/7/2013
# Purpose: Displays the maximum value of two integers.

# Displays a menu for the user.
def main():
    display_menu()

# Offers the user the choice to quit the program or get maximum value of two numbers.
def display_menu():
    # initialize flag variable
    menuSelection = '0'
    # loop until the user chooses the option to quit
    while menuSelection != '2':
        # display menu choices
        print('\tMenu')
        print('1) Get maximum of two values')
        print('2) Quit program')
        # get user selection
        menuSelection = input('Enter your choice: ')
        if menuSelection == '1':
            # run the get_max function and display the result
            print('The maximum of the two values is:', get_max())
        elif menuSelection == '2':
            # returns to the main function and ends the program
            print('Exiting the program...')
        else:
            # displays error message and displays menu again
            print('Error...invalid selection')

# gets two integer values from the users,compares the values, and displays the largest value.      
def get_max():
    value1 = int(input('Enter the first number: '))
    value2 = int(input('Enter the second number: '))
    if value1 > value2:
        largest = value1
    else:
        largest = value2
    return largest
    
# Runs the main program.
main()
