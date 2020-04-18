# Faça um Programa que leia três números e mostre o maior deles.

numbers = []

for i in range(0, 3):
    numbers.append(input("\nEnter a number: "))

print("\nThe greater number is: {}".format(max(numbers)))
