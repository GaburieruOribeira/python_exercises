# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

radius = float(input('\nEnter the radius of the circle: '))
area = math.pi * radius ** 2
print('\nThe area of the circle is: {:.2f}'.format(area))
