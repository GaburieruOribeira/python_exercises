# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# Make a program that calculates the roots of a second degree equation, in the form ax2 + bx + c.
# The program should ask for the values of a, b and c and make the consistencies, informing the user in the following situations:
# - If the user inputs the value of A equal to zero, the equation is not of the second degree and the program should not ask for the other values, being closed;
# - If the calculated delta is negative, the equation has no real roots. Inform the user and close the program;
# - If the calculated delta is equal to zero, the equation has only one real root; inform the user;
# - If the delta is positive, the equation has two real roots; inform the user;

import math

a = float(input("\nEnter the A value: "))
if a == 0:
    print("\nThis equation isn't second degree.")
else:
    b = float(input("\nEnter the B value: "))
    c = float(input("\nEnter the C value: "))    
    delta = b * b - (4 * a * c)

    if delta < 0:
        print("\nDelta less than 0. Imaginary roots.")
    elif delta == 0:
        root = -b / (2 * a)
        print("Delta = 0 , root = ", root)
    else:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Roots: ", root1," and ", root2)
