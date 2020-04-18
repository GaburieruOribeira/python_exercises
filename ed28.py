# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# -tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("""\nPrice Table:
                          Up to 5 Kg               Over 5 Kg
1 - Double Filet      R$ 4,90 per Kg          R$ 5,80 per Kg
2 - Rump              R$ 5,90 per Kg          R$ 6,80 per Kg
3 - Filet Steak       R$ 6,90 per Kg          R$ 7,80 per Kg

If you purchase with the Tabajara card you will also receive a 5% discount !!!""")

try:
    meatType = int(input("\nChoose a meat number (1 type): "))
    meatAmount = float(input("\nEnter the meat amount (Kg): "))

    # Double Filet:
    if meatType == 1:
        meatName = "Double Filet"
        if meatAmount <= 5.0:
           meatPrice = meatAmount * 4.90
        else:
            meatPrice = meatAmount * 5.80
    
    # Rump:
    elif meatType == 2:
        meatName = "Rump"
        if meatAmount <= 5.0:
           meatPrice = meatAmount * 5.90
        else:
            meatPrice = meatAmount * 6.80
   
    # Filet Steak:
    elif meatType == 3:
        meatName = "Filet Steak"
        if meatAmount <= 5.0:
           meatPrice = meatAmount * 6.90
        else:
            meatPrice = meatAmount * 7.80
    
    # Invalid Option:
    else:
        print("\nInvalid Number.")

    # Card Curchases:
    card = int(input("""\nChoose an option:
1 - Pay with the Tabajara card
2 - Do not pay with the Tabajara card
+ Enter the number of the option: """))

    # With Card:
    if card == 1:
        paymentType = "With Tabajara Card"
        discount = (meatPrice * 5) / 100

    # Without Card:
    elif card == 2:
        paymentType = "Without Tabajara Card"
        discount = 0.00

    # Invalid Option:
    else:
        print("\nInvalid Option")

    amountPayable = meatPrice - discount

    print("""\n
=========================================
+ Tax Coupon:

- Meat Type: {}
- Meat Amount: {}Kg
- Total Price: R${:.2f}
- Type of Payment: {}
- Discount Value: R${:.2f}
- Amount Payable: R${:.2f}
=========================================""".format(meatType, meatAmount, meatPrice, paymentType, discount, amountPayable))

except ValueError:
    print("\nInvalid Value.")
