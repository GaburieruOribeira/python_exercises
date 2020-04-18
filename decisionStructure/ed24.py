# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# - par ou ímpar;
# - positivo ou negativo;
# - inteiro ou decimal.

# Make a program that reads 2 numbers and then ask the user which operation he wants to perform. The result of the operation must be accompanied by a sentence that says whether the number is:
# - even or odd;
# - positive or negative;
# - integer or decimal.

num1 = float(input("\nEnter the first number: "))
num2 = float(input("\nEnter the second number: "))

option = int(input("""\nChoose an option:
1) Even or Odd;
2) Positive or Negative;
3) Integer or Decimal
+ Enter the number of the option: """))

# Control Variables
i = False
j = False

# Options Calculations
# Option 1:
if option == 1:
    if num1 % 2 == 0:
        i = True
    
    if num2 % 2 == 0:
        j = True
    
    # Option 1 exit
    if i and j:
        print("\nThe number {} is even, and the number {} is even.".format(num1, num2))
    elif i == False and j == True:
        print("\nThe number {} is odd, and the number {} is even.".format(num1, num2))
    elif i == True and j == False:
        print("\nThe number {} is even, and the number {} is odd.".format(num1, num2))
    else:
        print("\nThe number {} is odd, and the number {} is odd.".format(num1, num2))

# Option 2:
elif option == 2:
    if num1 >= 0:
        i = True

    if num2 >= 0:
        j = True

    # Option 2 exit
    if i and j:
        print("\nThe number {} is positive, and the number {} is positive.".format(num1, num2))
    elif i == False and j == True:
        print("\nThe number {} is negative, and the number {} is positive.".format(num1, num2))
    elif i == True and j == False:
        print("\nThe number {} is positive, and the number {} is negative.".format(num1, num2))
    else:
        print("\nThe number {} is negative, and the number {} is negative.".format(num1, num2))
        
# Option 3:
elif option == 3:
    if num1 - int(num1) == 0:
        i = True

    if num2 - int(num2) == 0:
        j = True

    #Option 3 exit
    if i and j:
        print("\nThe number {} is integer, and the number {} is integer.".format(num1, num2))
    elif i == False and j == True:
        print("\nThe number {} is decimal, and the number {} is integer.".format(num1, num2))
    elif i == True and j == False:
        print("\nThe number {} is integer, and the number {} is decimal.".format(num1, num2))
    else:
        print("\nThe number {} is decimal, and the number {} is decimal.".format(num1, num2))

# Invalid Option:
else:
    print("\nInvalid number. Please try again.")
