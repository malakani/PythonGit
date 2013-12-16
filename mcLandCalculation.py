# Program name: mcLandCalculation.py
# Author: Melissa Coram
# Date last updated: 9/6/2013
# Purpose: Calculates and displays square footage as acres

# Get the number of square feet from the user
squareFeet = float(input('Enter the number of square feet: '))

# Calulate the number of acres by dividing the square footage by 43560
acres = squareFeet / 43560

# Display the number of acres
print(squareFeet, "square feet is equal to", acres, "acres.")
