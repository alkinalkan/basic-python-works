# Python Program for calculation operations.
# It includes summation, extraction, division, multipication and factorial.

submit = int(input("Hello! Welcome to Calculator Program. Please input a number:"))
fact = 1

while True:
    operator = input("Please choose operator: + - / * ! q\n")
    if operator == "+":
        number = int(input("Please input a number for summation:"))
        submit += number
        print(submit)
    if operator == "-":
        number = int(input("Please input a number for extraction:"))
        submit -= number
        print(submit)
    if operator == "/":
        number = int(input("Please input a number for division:"))
        submit /= number
        submit = int(submit)
        print(submit)
    if operator == "*":
        number = int(input("Please input a number for multipication:"))
        submit *= number
        print(submit)
    if operator == "!":
        print("Please input a number for factorial operation:")
        old_submit = submit
        for i in range(1, submit + 1):
            fact = fact * i
            submit = fact
        print("{}! = {}".format(old_submit, submit))
        fact = 1
    if operator == "q":
        print("Thanks for using calculator.\nYour last output: {}".format(submit))
        break
