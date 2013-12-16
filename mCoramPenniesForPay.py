# Program name: mCoramPenniesForPay.py
# Author: Melissa Coram
# Date last updated: 10/24/2013
# Purpose: Calculates and displays the daily salary and total pay earned.

def main():
    # Get the number of days from the user.
    print('You start a job working for one penny a day and your pay doubles every day thereafter.')
    days = int(input('How many days do you work? '))
    # Print header
    print('Day\tSalary\t\t\tTotal Pay')
    print('------------------------------------------------')
    # Run function to calculate salary.
    create_table(days)

# Function to calculate salary.
def create_table(days):
    # Initialize total pay to zero.
    totalPay = 0
    # Initialize salary to $0.01.
    salary = .01
    # Loop to calculate and display the salary earned each day and total amount earned.
    for x in range(days):
        # Add salary to total pay.
        totalPay += salary
        # Display current day's salary and total amount earned including the current day.
        print(x + 1, '\t$', format(salary, '10,.2f'), '\t\t$', format(totalPay, '10,.2f'))
        # Double salary for the next day's pay.
        salary *= 2

# Run main function.
main()
