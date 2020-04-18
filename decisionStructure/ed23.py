# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
# Make a program that asks for a number and inform if the number is an integer or a decimal. Tip: use a rounding function.

number = float(input("\nEnter a number: "))

if number - int(number) == 0:
    print("\nThis is an integer number.")
else:
    print("\nThis is a decimal number.")
