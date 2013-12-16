# Program name: mCoramAutomobileCosts.py
# Author: Melissa Coram
# Date last updated: 9/13/2013
# Purpose: Prints monthly and yearly automobile expenses.

def main():
    # Collect information from the user.
    print('Please enter your monthly costs for operating your automobile.')
    loan_cost = float(input('How much is your loan payment? '))
    insurance_cost = float(input('How much is your insurance payment? '))
    gas_cost = float(input('How much do you spend on gas? '))
    oil_cost = float(input('How much do you spend on oil? '))
    tire_cost = float(input('How much do you spend on tires? '))
    maintenance_cost = float(input('How much do you spend on maintenance? '))
    # Pass collected information to the calculate_expenses function to determine totals.
    calculate_expenses(loan_cost, insurance_cost, gas_cost, oil_cost, tire_cost, maintenance_cost)

# Adds costs input from user to calculate total monthly expenses and total yearly expenses,
# then displays totals.
def calculate_expenses(loan, ins, gas, oil, tires, maintenance):
    monthly_expense = loan + ins + gas + oil + tires + maintenance
    yearly_expense = monthly_expense * 12
    print('Your total montly automobile expense is $', format(monthly_expense, ',.2f'), sep='')
    print('Your total yearly automobile expense is $', format(yearly_expense, ',.2f'), sep='')

# Runs the main program.
main()
    
    
