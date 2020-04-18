# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# Make a Program that asks for the temperature in degrees Celsius, transform it and show it in degrees Fahrenheit.

celsius = float(input("\nEnter degrees in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("\nThe degrees in Fahrenheit is: {:.1f}ºF".format(fahrenheit))
