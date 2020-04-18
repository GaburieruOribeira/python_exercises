# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

celsius = float(input("\nEnter degrees in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("\nThe degrees in Fahrenheit is: {:.1f}ºF".format(fahrenheit))
