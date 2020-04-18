# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# A fruit tree is selling fruit with the following price list:
#                     Up to 5 Kg              Above 5 Kg
# Strawberry       R$2.50 per Kg           R$2.20 per Kg
# Apple            R$1.80 per kg           R$1.50 per kg
# If the customer buys more than 8 kg of fruit or the total purchase value exceeds R$25.00, he will also receive a 10% discount on this total.
# Write an algorithm to read the quantity (in Kg) of strawberries and the quantity (in Kg) of apples purchased and write the amount to be paid by the customer.

print("""\nPrice Table:
                    Up to 5 Kg               Over 5 Kg
Strawberry      R$ 2,50 per Kg          R$ 2,20 per Kg
Apple           R$ 1,80 per Kg          R$ 1,50 per Kg""")

strawberryAmount = float(input("\nEnter the amount of strawberries (Kg): "))
appleAmount = float(input("\nEnter the amount of apples (Kg): "))

if strawberryAmount <= 5.0:
    strawberryPrice = strawberryAmount * 2.50
else:
    strawberryPrice = strawberryAmount * 2.20

if appleAmount <= 5.0:
    applePrice = appleAmount * 1.80
else:
    applePrice = appleAmount * 1.50

totalAmount = strawberryAmount + appleAmount
totalValue = strawberryPrice + applePrice

if totalAmount > 8.0 or totalValue > 25.0:
    totalValue = totalValue - ((totalValue * 10) / 100)

print("\nTotal amount (Kg): {}Kg\nFinal price: R${:.2f}".format(totalAmount, totalValue))
