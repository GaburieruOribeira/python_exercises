# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# Make a Program that asks for the radius of a circle, calculate and show its area.

import math

radius = float(input('\nEnter the radius of the circle: '))
area = math.pi * radius ** 2
print('\nThe area of the circle is: {:.2f}'.format(area))
