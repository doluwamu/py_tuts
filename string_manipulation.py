# Create a program that asks the user to enter their first name and last name separately. Then, the program should concatenate these names and display a message. Additionally, it should count and display the total number of characters in the full name.

# Here are the requirements:

# Prompt the user to enter their first name and store it in a variable.
# Prompt the user to enter their last name and store it in a different variable.
# Concatenate the first name and last name to form the full name.
# Display a message that greets the user using their full name, for example, "Hello, John Doe!"
# Count and display the total number of characters in the full name (including spaces).

def string_manipulation():
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    full_name = f"{first_name} {last_name}"

    print(f"Hi {full_name}!")
    print(f"Your name is {full_name.__len__()} characters long")


string_manipulation()