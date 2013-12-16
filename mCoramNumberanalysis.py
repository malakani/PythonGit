# Program name: mCoramNumberanalysis.py
# Author: Melissa Coram
# Date last updated: 12/4/2013
# Purpose: Obtains a list of 20 numbers from the users and displays the lowest and
# highest numbers in the list as well as the total and average of the numbers.

def main():
    # constant variable for the amount of numbers in the list
    LIST_LENGTH = 20
    # create empty list
    numberList = []
    # This loop prompts the user to enter a number.  The amount of numbers the user is
    # prompted to enter is based on the constant LIST_LENGTH.  The numbers input by the
    # user are assigned to a list.
    print('Enter', LIST_LENGTH, 'numbers.')
    for x in range(LIST_LENGTH):
        inputStr = 'Number ' + str(x + 1) + ': '
        newNumber = int(input(inputStr))
        numberList.append(newNumber)
    # runs the minMax function
    minMax(numberList)
    # runs the totalAndAverage function
    totalAndAverage(numberList)

# This function gets the minimum and maximum values in the list and displays the values.
def minMax(newList):
    print(min(newList), 'is the lowest number in the list.')
    print(max(newList), 'is the highest number in the list.')

# This function utilizes a loop to total the numbers in the list via an accumulator and
# determines the length to obtain the average of the numbers.  The total and average are
# then displayed.
def totalAndAverage(newList):
    # initilize accumulator variable
    total = 0
    # loop through list to obtain total
    for number in newList:
        total += number
    # obtain the average
    average = total / len(newList)
    # display results
    print('The total of the numbers is ', total, '.', sep='')
    print('The average of the numbers is ', average, '.', sep='')


# runs main function    
main()
    

