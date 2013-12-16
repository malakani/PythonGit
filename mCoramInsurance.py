# Program name: mCoramInsurance.py
# Author: Melissa Coram
# Date last updated: September 21, 2013
# Purpose:  Asks user to enter the replacement cost of a building and determines the amount of insurance needed.

# global constant for the percentage of insurance recommended
INSURANCE_PERCENTAGE = .8

# main program
def main():
    # get the replacement cost of the building
    replacementCost = float(input('Enter the replacement cost of the building: '))
    # pass replacement cost to compute_insurance function for calculation and display
    compute_insurance(replacementCost)

# calculates and displays the amount of insurance recommended for a building
def compute_insurance(cost):
    insuranceAmt = cost * INSURANCE_PERCENTAGE
    print('The amount of insurance recommneded for your building is $', format(insuranceAmt, ',.2f'), sep='')

# start the program
main()
