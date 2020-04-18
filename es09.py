# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input('\nEnter degrees in Fahrenheit: '))
celsius = (5 * (fahrenheit - 32) / 9)
print("\nThe degrees in Celsius is: {:.1f}ºC".format(celsius))
