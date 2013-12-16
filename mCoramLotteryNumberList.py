# Program name: mCoramLotteryNumberList.py
# Author: Melissa Coram
# Date last updated: 11/19/2013
# Purpose: Generates a lottery number consisting of six numbers between 0 and 99
# and displays each number separately.

def main():
    # import random module
    import random
    # constant variable for the length of the lottery number
    NUMBER_LENGTH = 6
    # create empty list
    lotteryList = []
    # This loop appends a random number between 0 and 99 to lotteryList.
    # The number of loop interations depends on the length of the lottery number.
    for x in range(NUMBER_LENGTH):
        lotteryList.append(random.randint(0,99))
    # This loop displays each number on a separate line.
    for element in lotteryList:
        print(element)
    
# runs main program
main()
    
    
    
    
