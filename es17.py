# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1) Comprar apenas latas de 18 litros;
# 2) Comprar apenas galões de 3,6 litros;
# 3) Misturar latas e galões, de forma que o preço seja o menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

try:
    areaToBePainted = float(input("\nEnter the size of the area to be painted(m²): "))
    inkCover = ( 1 / 6 ) * areaToBePainted # Quantidade de tinta a ser comprada
    inkCover_ceil = math.ceil(float(inkCover * 1.1))
    print("\nInk to be purchased: {:.2f}L".format(inkCover))
    purchaseOption = int(input("""\n+ Purchasing Options:
1) Buy only 18L cans;
2) Buy only 3.6L gallons;
3) Mix cans and gallons.
Enter purchase type number: """)) # Escolher opção de compra
    options = [1, 2, 3]

    while not 1 <= purchaseOption <= 3:
        purchaseOption = int(input("\nChoose an option from 1 to 3: "))

    if purchaseOption == options[0]:
        paintCans = inkCover / 18 # Qtd de Latas de tinta
        paintCans_ceil = math.ceil(paintCans)
        paintCans_price = paintCans_ceil * 80.00 # Preço das latas
        print("\nCans to be purchased: {}\nTotal amount payable: R${}".format(paintCans_ceil, paintCans_price))
    elif purchaseOption == options[1]:
        paintGallons = inkCover / 3.6 # Qtd de Galões de tinta
        paintGallons_ceil = math.ceil(paintGallons)
        paintGallons_price = paintGallons_ceil * 25.00 # Preço dos galões
        print("\nGallons to be purchased: {}\nTotal amount payable: R${}".format(paintGallons_ceil, paintGallons_price))

    elif purchaseOption == options[2]:
        a1 = int(inkCover_ceil / 18)
        a2 = inkCover_ceil % 18
        a3 = math.ceil(a2 / 3.6)
        a4 = ((a1 * 80)+(a3 * 25))
        print("\nCans to be purchased: {}\nGallons to be purchased: {}\nTotal amount payable: R${:.2f}".format(a1, a3, a4))

except ValueError:
    print("\nYou have entered invalid values. Please try again.")
