# Program Name: mcSalesPrediction.py
# Author: Melissa Coram
# Date last updated: August 27, 2013
# Purpose: Calculates and displays profit based on projected sales.

# Get the projected sales from the user, formatted as a floating point number
projectedSales = float(input('Enter the projected amount of total sales: '))

#Calculate profit by multiplying projected sales by 23 percent
profit = projectedSales * .23

#Display the profit, rounded to two decimal places
print('The projected profit amount is $', format(profit, '.2f'))
