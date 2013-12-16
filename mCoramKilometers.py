# Program name: mCoramKilometers.py
# Author: Melissa Coram
# Date last updated: September 21, 2013
# Purpose: Accepts a distance in kilometers and outputs the distance in kilometers
# and miles.

# main program
def main():
    # get the distance in kilometers
    distance = int(input('Enter the distance in kilometers: '))
    # pass distance to compute_miles function for calculation and display
    compute_miles(distance)
    # print message
    print('Kilometers XXXXX is equal to XXXXX miles')

# converts kilometers to miles and displays the distance in both forms
def compute_miles(kilometers):
    miles = kilometers * 0.6214
    print('The distance in kilometers is', kilometers)
    print('The distance in miles is', miles)

# start the program
main()
