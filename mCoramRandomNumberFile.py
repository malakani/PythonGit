# Program name: mCoramRandomNumberFile.py
# Author: Melissa Coram
# Date last updated: 11/14/2013
# Purpose: Creates a file and writes a series of randoms numbers to the file.
# Reads the file, counts and totals the numbers in the file and displays the
# accumulated values and closes the file.

# import random module
import random

# global constant for random number file
RANDOM_FILE = 'randomNumbers.txt'

# Gets the quantity of required random numbers from the user and calls the
# function to create the file to store random numbers generated and the
# function to read the file and display the numbers and totals.
def main():
    quantity = int(input('How many random numbers do you want to generate? '))
    create_file(quantity)
    read_file()


# Creates a file and then generates random numbers in the range of 1 to 100
# in the quantity specified by the user.  Random numbers are then written to
# the file and the file is closed.
def create_file(quantity):
    randomNumFile = open(RANDOM_FILE, 'w')
    for x in range(quantity):
        randomNumFile.write(str(random.randint(1,100)) + '\n')
    randomNumFile.close()

# Opens the file of random numbers and reads and displays each number.
# Accumulates and displays the sum of all the numbers in the file as well as
# the number of numbers in the file.
def read_file():
    # set accumulators to zero
    total = 0
    count = 0
    # open file and read contents
    randomNumFile = open(RANDOM_FILE, 'r')
    for line in randomNumFile:
        number = int(line)
        print(number)
        # add to accumulators
        total += number
        count += 1
    # display results
    print(total, 'is the sum of the random numbers.')
    print('There are', count, 'random numbers in the file.')

# Runs main program.
main()
