# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
# Make a Program that reads a number and displays the corresponding day of the week. (1-Sunday, 2-Monday, etc.), if you enter another value, an invalid value should appear.

try:
    number = int(input("\nEnter a number: "))

    if number == 1:
        print("\nDomingo")
    elif number == 2:
        print("Segunda")
    elif number == 3:
        print("Terça")
    elif number == 4:
        print("\nWednesday")
    elif number == 5:
        print("\nQuinta")
    elif number == 6:
        print("\nFriday")
    elif number == 7:
        print("\nSábado")
    else:
        print("\nInvalid Number.")

except ValueError:
    print("\nInvalid Value.")
