# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

areaToBePainted = float(input("\nEnter the size of the area to be painted(m²): "))
inkCover = ( 1 / 3 ) * areaToBePainted
paintCans = inkCover / 18
inkPrice = paintCans * 80
print("\nPaint cans to be purchased: {}\nTotal Price: R${:.2f}".format(paintCans, inkPrice))
