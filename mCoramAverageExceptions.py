# Program name: mCoramAverageExceptions.py
# Author: Melissa Coram
# Date last updated: 11/16/2013
# Purpose: Looks for the file name given by the user.  Reads the file, calculates 
# the average of the numbers in the file, and displays the results.

# Get file name from the user and pass it to the process_file function.
def main():
    filename = input('Enter the name of the file that you wish to process: ')
    process_file(filename)

def process_file(filename):
    # Try/except statement handle any exceptions.
    try:
        # open file
        inputfile = open(filename, 'r')
        # initialize accumlators for total and count in order to calculate average
        total = 0
        count = 0
        # read each line in the file and add the number to total accumlator and increase
        # count by 1
        for line in inputfile:
            number = int(line)
            total += number
            count += 1
        # calculate average of the numbers in file
        average = total / count
        # print results
        print('The average of the numbers in ', filename, ' is ', average, '.', sep='')
    # handles file input error
    except IOError as errorMessage:
        print(errorMessage)
    # handles value errors
    except ValueError as errorMessage:
        print(errorMessage)
    # handles any other exceptions
    except:
        print('An error has occured.')
        
# run main program
main()
        
            
