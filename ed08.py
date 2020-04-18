# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prices = []

for i in range(3):
    prices.append(float(input("\nEnter a product price: ")))

print("\nThe best option is the R${:.2f} value product.".format(min(prices)))

