# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
# Make a Program that asks for a number corresponding to a certain year and then inform if this year is leap or not.

year = int(input("\nEnter a year: "))
divisionBy4 = year % 4
divisionBy100 = year % 100
divisionBy400 = year % 400

if divisionBy4 == 0 and divisionBy100 != 0 or divisionBy400 == 0:
    print("\nThis is a leap year.")
else:
    print("\nThis isn't a leap year.")
