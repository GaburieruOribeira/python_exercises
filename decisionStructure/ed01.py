# Faça um Programa que peça dois números e imprima o maior deles.
# Make a Program that asks for two numbers and prints the largest one.

num1 = int(input("\nEnter the first nummber: "))
num2 = int(input("\nEnter the second nummber: "))

if num1 > num2:
    print("\nNumber {} is greater than number {}".format(num1, num2))

elif num1 < num2:
    print("\nNumber {} is less than number {}".format(num1, num2))

else:
    print("\nNumber {} is equal to the number {}".format(num1, num2))

