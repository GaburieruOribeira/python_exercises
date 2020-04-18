# Faça um Programa que peça um número e então mostre a mensagem: O número informado foi [número].
# Make a Program that asks for a number and then displays the message: The number entered was [number].

number = input('\nEnter a number: ')
try:
    number1 = int(number)
    if number1 == int(number):
        print('\nThe number entered was: {}'.format(number))
except ValueError:
    print('\nYou did not enter a number.')
