# Create a Python program that calculates and displays the monthly payment for a loan based on the principal amount, annual interest rate, and the loan term (in months).

# Here are the requirements:

# Prompt the user to enter the principal amount (the initial loan amount).
# Prompt the user to enter the annual interest rate (as a percentage).
# Prompt the user to enter the loan term in years and then convert it to months.
# Calculate the monthly interest rate by dividing the annual interest rate by 12 and converting it to a decimal.
# Use the formula for calculating a monthly payment of a fixed-rate loan:

from math import floor 

def calc_loan_payment():
    principal = int(input("Enter principal amount: "))
    annual_interest_rate = int(input("Enter annual interest rate: ")) # Number is expressed as percentage
    loan_term = int(input("Enter duration of loan: ")) * 12 # Number entered will be converted to months

    monthly_interest_rate = (annual_interest_rate / 12) / 100

    if (principal == None):
        print("Enter principal")

    print(floor(principal * monthly_interest_rate))


calc_loan_payment()