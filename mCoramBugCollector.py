# Program name: mCoramBugCollector.py
# Author: Melissa Coram
# Date last updated: 10/17/2013
# Purpose: Calculates the number of bugs collected in a week.

def main():
    # Run the bug_coll function.
     bug_coll()

# Asks the user to input the number of bugs collected for each day of the week and adds 
# it to the weekly total.
def bug_coll():
    # Initialize accumlator variable to track number of bugs collected each day.
    total = 0
    # Ask the user seven times for the number of bugs collected
    for num in range(7):
        print("Day ", num + 1, ".", sep='')
        count = int(input("Enter the number of bugs collected: "))
        # Accumulate number of bugs collected.
        total += count
    # Display number of bugs collected for the seven days.
    print(total, "bugs were collected this week.")

# Run main program.    
main()
