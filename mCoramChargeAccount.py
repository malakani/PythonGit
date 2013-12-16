# Program name: mCoramChargeAccount.py
# Author: Melissa Coram
# Date last updated: 11/19/2013
# Purpose: Reads a list of account numbers and checks user input of account numbers
# against the list to see if it is a valid number.

def main():
    # Open account number file and read the file into a list.
    accountNumFile = open('charge_accounts.txt', 'r')
    accountNumList = accountNumFile.readlines()
    # Close the account file.
    accountNumFile.close()
    # Initialize the index variable.
    index = 0
    # This loop goes through each element in the list and strips the new line character.
    while index < len(accountNumList):
        accountNumList[index] = accountNumList[index].rstrip('\n')
        index += 1
    # Get an account number from the user.
    inputAccount = input('Enter a seven-digit account number: ')
    # Checks the account number against the numbers in the list obtained from the file
    # and displays whether the account number is valid (in the file) or not.
    if inputAccount in accountNumList:
        print(inputAccount, 'is a valid account number.')
    else:
        print(inputAccount, 'is not a valid account number.')

# Run the main program.
main()
    
