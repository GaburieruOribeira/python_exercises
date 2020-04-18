# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
# Make a Program that asks for a date in the format dd / mm / yyyy and determine if it is a valid date.

day = int(input("\nEnter a day: "))
month = int(input("\nEnter a month: "))
year = int(input("\nEnter a year: "))

valid = False

# Months with 31 days
if month==1 or month==3 or month==5 or month==7 or month==9 or month==10 or month==12:
    if day <= 31:
        valid = True
# Months with 30 days
elif month==4 or month==6 or month==9 or month==11:
    if day <= 30:
        valid = True
elif month==2:
    # Test if is leap year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if day <= 29:
            valid = True
        elif day <= 28:
            valid = True

if valid == True:
    print("\nValid Date.")
else:
    print("\nInvalid Date.")
