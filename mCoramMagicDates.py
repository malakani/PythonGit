# Program name: mCoramMagicDates.py
# Author: Melissa Coram
# Date last updated: October 4, 2013
# Purpose: Accepts a date from the user and determines and displays whether the date is a magic date.

# Get the month, day, and year from the user and send these values to the check_magic function.
def main():
    month = int(input('Enter the month: '))
    day = int(input('Enter the day: '))
    year = int(input('Enter the last two digits of the year: '))
    check_magic(month, day, year)

# Determines and displays if a date is a magic date or if it is not a magic date.
def check_magic(mm, dd, yy):
    # If the month multiplied by the day is equal to the year, the date is a magic date.
    if (mm * dd) == yy:
        print(mm, '/', dd, '/', yy, ' is a magic date.', sep='')
    else:
        print(mm, '/', dd, '/', yy, ' is not a magic date.', sep='')

# Runs the main program.
main()
