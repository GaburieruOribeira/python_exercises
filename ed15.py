# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

side1 = float(input("\nEnter the first side of the triangle: "))
side2 = float(input("\nEnter the second side of the triangle: "))
side3 = float(input("\nEnter the third side of the triangle: "))

if (side1 + side2) > side3 or (side1 + side3) > side2 or (side2 + side3) > side1:
    if side1 == side2 and side2 == side3:
        print("\nThis is an equilateral triangle.")
    elif side1 != side2 and side1 != side3 and side2 != side3:
        print("\nThis is a scalene triangle.")
    else:
        print("\nThis is an isosceles triangle.")
else:
    print("\nWith these values, it is not possible to create a triangle.")
