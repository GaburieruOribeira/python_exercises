# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

squareSide = float(input('\nEnter the size of the one side of the square: '))
squareArea = squareSide * squareSide
doubledArea = squareArea * 2
print("\nSquare area: {:.1f}\nDoubled area: {:.1f}".format(squareArea, doubledArea))
