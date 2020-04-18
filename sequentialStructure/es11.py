# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) O produto do dobro do primeiro com metade do segundo.
# b) A soma do triplo do primeiro com o terceiro.
# c) O terceiro elevado ao cubo.

# Make a Program that asks for 2 whole numbers and a real number. Calculate and show:
# a) The product of double the first with half the second.
# b) The sum of triple the first with the third.
# c) The third cubed.

num1 = float(input("\nEnter the first integer number: "))
num2 = float(input("\nEnter the second integer number: "))
num3 = float(input("\nEnter the real number: "))
multiplication = (num1 * 2) * (num2 / 2)
sum = (num1 * 3) + num3
cube = num3 ** 3
print("\nA) {:.1f}\nB) {:.2f}\nC) {:.2f}".format(multiplication, sum, cube))
