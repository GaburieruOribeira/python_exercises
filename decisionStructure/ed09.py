# Faça um Programa que leia três números e mostre-os em ordem decrescente.
# Make a Program that reads three numbers and shows them in descending order.

numbers = []

for i in range(3):
    numbers.append(int(input("\nEnter a number: ")))

numbers.sort()
numbers.reverse()
print("\nThe numbers in descending order: " + str(numbers))
