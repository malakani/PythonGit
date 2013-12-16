# Program name: mCoramDistanceTraveled.py
# Author: Melissa Coram
# Date last updated: 10/24/2013
# Purpose: Calculates and displays the distance traveled per hour.

def main():
    # Get the speed and number of hours traveled from the user.
    speed = float(input("What is the speed of the vehicle in mph? "))
    hours = int(input("How many hours has it traveled? "))
    # Print header
    print('Hour\tDistance Traveled')
    print('-------------------------')
    # Run function to calculate distance traveled from user input.
    calc_distance(speed, hours)

# Function to calculate distance traveled.
def calc_distance(mph, time):
    # Loop to calculate and display the distance traveled for each hour traveled.
    for x in range(time):
        distance = mph * (x + 1)
        print(x + 1, '\t', format(distance, '8.1f'))

# Run main function.
main()
