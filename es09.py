# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Make a Program that asks for the temperature in degrees Fahrenheit, transform and show the temperature in degrees Celsius.

fahrenheit = float(input('\nEnter degrees in Fahrenheit: '))
celsius = (5 * (fahrenheit - 32) / 9)
print("\nThe degrees in Celsius is: {:.1f}ºC".format(celsius))
