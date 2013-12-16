# Program name: mCoramRectangles.py
# Author: Melissa Coram
# Date last updated: September 26, 2013
# Purpose: Accepts the length and width of two rectangles and determines which has the greater area
# or if they are the same.

def main():
    # Get the length and width of two rectangles from the user.
    length1 = float(input('Enter the length of Rectangle 1: '))
    width1 = float(input('Enter the width of Rectangle 1: '))
    length2 = float(input('Enter the length of Rectangle 2: '))
    width2 = float(input('Enter the width of Rectangle 2: '))
    # Pass the length and width to the check_rectangles function to determine the area.
    check_rectangles(length1, width1, length2, width2)


# Calculates and displays the area of two rectangles and prints whether one rectangle has a greater
# area than another or if they are equal.
def check_rectangles(len1, wid1, len2, wid2):
    area1 = len1 * wid1
    area2 = len2 * wid2
    print('The area of Rectangle 1 is', area1)
    print('The area of Rectangle 2 is', area2)
    if area1 > area2:
        print('Rectangle 1 has a greater area than Rectangle 2.')
    elif area1 < area2:
        print('Rectangle 2 has a greater area than Rectangle 1.')
    else:
        print('Rectangle 1 has an area equal to Rectangle 2.')

# Runs the main program.
main()

    
