# Create a basic text-based calculator that allows the user to perform a single arithmetic operation on two numbers. The calculator should support addition and subtraction.

# Here are the requirements:

# Prompt the user to enter the first number.
# Prompt the user to enter the second number.
# Ask the user whether they want to perform addition or subtraction by entering "+" or "-".
# Based on the user's choice, calculate and display the result.

# Numbers
num_one = int(input('Enter first number: '))
num_two = int(input('Enter second number: '))

# Operation
operation = input("What operation do you want to perform (+ or -): ")

if(operation == "-"):
    print(num_one - num_two)

else:
    print(num_one + num_two)
