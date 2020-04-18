# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numbers = []

for i in range(3):
    numbers.append(int(input("\nEnter a number: ")))

numbers.sort()
numbers.reverse()
print("\nThe numbers in descending order: " + str(numbers))
