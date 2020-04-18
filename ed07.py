# Faça um Programa que leia três números e mostre o maior e o menor deles.

numbers = []

for i in range(3):
    numbers.append(input("\nEnter a number: "))

print("\nThe highest number is {}, and the lowest number is {}".format(max(numbers), min(numbers)))
