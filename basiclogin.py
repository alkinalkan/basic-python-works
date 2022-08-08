from re import T

submit = int(input("Hello! Welcome to Calculator. Lutfen bir sayi girisi yapiniz:"))
fact = 1

while True:
    operator = input("islem seciniz: + - / * ! q\n")
    if operator == "+":
        number = int(input("Sayi giriniz:"))
        submit += number
        print(submit)
    if operator == "-":
        number = int(input("Sayi giriniz:"))
        submit -= number
        print(submit)
    if operator == "/":
        number = int(input("Sayi giriniz:"))
        submit /= number
        submit = int(submit)
        print(submit)
    if operator == "*":
        number = int(input("Sayi giriniz:"))
        submit *= number
        print(submit)
    if operator == "!":
        print("Halihazirda bulunan sayinin faktoriyeli:")
        for i in range(1, submit + 1):
            fact = fact * i
            submit = fact
        print(fact)
        fact = 1
    if operator == "q":
        print("Hesap makinesini kullandiginiz icin tesekkurler. Son ciktiniz: {}".format(submit))
        break
