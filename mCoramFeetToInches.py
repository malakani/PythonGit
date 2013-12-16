# Program name: mCoramFeetToInches.py
# Author: Melissa Coram
# Date last updated: 10/31/2013
# Purpose: Converts a length in feet to inches and displays result.

def main():
    # Get the number of feet
    feet = float(input("Enter the number of feet: "))
    # Print the number of feet and the number of inches.
    print(feet, "feet is equal to", feet_to_inches(feet), "inches.")

# Accepts the number of feet and calculates and returns the number of inches.
def feet_to_inches(feet):
    return feet * 12

# Runs the main program.
main()
