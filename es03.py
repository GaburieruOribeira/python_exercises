# Faça um Programa que peça dois números e imprima a soma.

try:
    num1 = int(input('\nDigite um número: '))
    num2 = int(input('Digite outro número: '))
    sum = num1 + num2
    print('\n{} + {} = {}'.format(num1, num2, sum))
except ValueError:
    print('\nVocê não digitou um número')
