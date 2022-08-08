submit = int(input("Hello! Welcome to Calculator. Please input a number:"))
fact = 1

while True:
    operator = input("Choose operator: + - / * ! q\n")
    if operator == "+":
        number = int(input("Please input a number:"))
        submit += number
        print(submit)
    if operator == "-":
        number = int(input("Please input a number:"))
        submit -= number
        print(submit)
    if operator == "/":
        number = int(input("Please input a number:"))
        submit /= number
        submit = int(submit)
        print(submit)
    if operator == "*":
        number = int(input("Please input a number:"))
        submit *= number
        print(submit)
    if operator == "!":
        print("Factorial of number is:")
        old_submit = submit
        for i in range(1, submit + 1):
            fact = fact * i
            submit = fact
        print("{}! = {}".format(old_submit, submit))
        fact = 1
    if operator == "q":
        print("Thanks for using calculator.\nYour last output: {}".format(submit))
        break
