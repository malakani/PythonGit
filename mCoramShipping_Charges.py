# Program name: mCoramShipping_Charges.py
# Author: Melissa Coram
# Date last updated: October 11, 2013
# Purpose: Calculates and displays shipping charges based on package weight entered by user.

# Shipping rate per pound for packages that weigh 1 pound or less.
RATE_A = .9

# Shipping rate per pound for packages that weigh more than 1 pound, but not more than 2 pounds.
RATE_B = 1.1

# Shipping rate per pound for packages that weigh more than 2 pounds, but not more than 6 pounds.
RATE_C = 2.2

# Shipping rate per pound for packages that weigh more than 6 pounds, but not more than 10 pounds.
RATE_D = 3.7

# Shipping rate per pound for packages that weigh more than 10 pounds.
RATE_E = 3.8

def main():
    # Get package weight from user.
    weight = float(input('Enter the weight of the package in pounds: '))
    # Determine rate and calculate charges.
    if weight > 10:
        charges = weight * RATE_E
    elif weight > 6:
        charges = weight * RATE_D
    elif weight > 2:
        charges = weight * RATE_C
    elif weight > 1:
        charges = weight * RATE_B
    else:
        charges = weight * RATE_A
    # Display shipping charges.    
    print('The shipping charge for this package is $', format(charges, ',.2f'), sep='')

# Run main program.
main()
                                      
