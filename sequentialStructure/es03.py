# Faça um Programa que peça dois números e imprima a soma.
# Make a program that asks for two numbers and prints the sum.

try:
    num1 = int(input('\nEnter a number: '))
    num2 = int(input('Enter another number: '))
    sum = num1 + num2
    print('\n{} + {} = {}'.format(num1, num2, sum))
except ValueError:
    print('\nYou did not enter a number.')
