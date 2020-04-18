# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
# Make a Program that asks for a whole number and determine if it is even or odd. Tip: use the module operator (rest of the division).

number = int(input("\nEnter a number: "))
if number % 2 == 0:
    print("\nThis number is even.")
else:
    print("\nThis number is odd.")
