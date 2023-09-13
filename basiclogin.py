# Python Program for calculation operations.
# It includes summation, subtraction, division, multiplication, exponentiation, modulus, and factorial.

# Take the initial number as input from the user
submit = int(input("Hello! Welcome to the Calculator Program. Please input a number: "))
fact = 1  # Initialize a variable to store factorial

while True:
    # Ask the user to choose an operator
    operator = input("Please choose an operator: + - / * ^ % ! q\n")
    
    # Addition operation
    if operator == "+":
        number = int(input("Please input a number for summation: "))
        submit += number  # Add the number to the current total
        print(submit)  # Print the updated total
        
    # Subtraction operation
    elif operator == "-":
        number = int(input("Please input a number for subtraction: "))
        submit -= number  # Subtract the number from the current total
        print(submit)  # Print the updated total
        
    # Division operation
    elif operator == "/":
        number = int(input("Please input a number for division: "))
        submit /= number  # Divide the current total by the number
        submit = int(submit)  # Convert the result to an integer
        print(submit)  # Print the updated total
        
    # Multiplication operation
    elif operator == "*":
        number = int(input("Please input a number for multiplication: "))
        submit *= number  # Multiply the current total by the number
        print(submit)  # Print the updated total
        
    # Exponentiation operation
    elif operator == "^":
        number = int(input("Please input a number for exponentiation: "))
        submit **= number  # Raise the current total to the power of the number
        print(submit)  # Print the updated total
        
    # Modulus operation
    elif operator == "%":
        number = int(input("Please input a number for modulus: "))
        submit %= number  # Calculate the modulus of the current total and the number
        print(submit)  # Print the updated total
        
    # Factorial operation
    elif operator == "!":
        print("Please input a number for factorial operation: ")
        old_submit = submit
        for i in range(1, submit + 1):
            fact *= i  # Calculate the factorial of the current total
            submit = fact  # Update the total with the factorial result
        print("{}! = {}".format(old_submit, submit))  # Print the factorial result
        fact = 1  # Reset the factorial variable
        
    # Quit the calculator
    elif operator == "q":
        print("Thanks for using the calculator.\nYour last output: {}".format(submit))
        break  # Exit the calculator loop
