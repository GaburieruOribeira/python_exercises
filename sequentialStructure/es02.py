# Faça um Programa que peça um número e então mostre a mensagem: O número informado foi [número].
# Make a Program that asks for a number and then displays the message: The number entered was [number].

number = input('\nInforme um número: ')
try:
    number1 = int(number)
    if number1 == int(number):
        print('\nO número informado foi: {}'.format(number))
except ValueError:
    print('\nVocê não digitou um número.')
