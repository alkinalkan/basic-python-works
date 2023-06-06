# Python Program for calculation operations.
# It includes summation, subtraction, division, multiplication, exponentiation, modulus, and factorial.

submit = int(input("Hello! Welcome to the Calculator Program. Please input a number: "))
fact = 1

while True:
    operator = input("Please choose an operator: + - / * ^ % ! q\n")
    
    if operator == "+":
        number = int(input("Please input a number for summation: "))
        submit += number
        print(submit)
        
    elif operator == "-":
        number = int(input("Please input a number for subtraction: "))
        submit -= number
        print(submit)
        
    elif operator == "/":
        number = int(input("Please input a number for division: "))
        submit /= number
        submit = int(submit)
        print(submit)
        
    elif operator == "*":
        number = int(input("Please input a number for multiplication: "))
        submit *= number
        print(submit)
        
    elif operator == "^":
        number = int(input("Please input a number for exponentiation: "))
        submit **= number
        print(submit)
        
    elif operator == "%":
        number = int(input("Please input a number for modulus: "))
        submit %= number
        print(submit)
        
    elif operator == "!":
        print("Please input a number for factorial operation: ")
        old_submit = submit
        for i in range(1, submit + 1):
            fact *= i
            submit = fact
        print("{}! = {}".format(old_submit, submit))
        fact = 1
        
    elif operator == "q":
        print("Thanks for using the calculator.\nYour last output: {}".format(submit))
        break
