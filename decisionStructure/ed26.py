# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# - Álcool:
# - até 20 litros, desconto de 3% por litro;
# - acima de 20 litros, desconto de 5% por litro;
# - Gasolina:
# - até 20 litros, desconto de 4% por litro;
# - acima de 20 litros, desconto de 6% por litro;
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

# A gas station is selling fuel with the following discount table:
# - Alcohol:
# - up to 20 liters, 3% discount per liter;
# - above 20 liters, discount of 5% per liter;
# - Gasoline:
# - up to 20 liters, discount of 4% per liter;
# - above 20 liters, discount of 6% per liter;
# Write an algorithm that reads the number of liters sold, the type of fuel (coded as follows: A-alcohol, G-gasoline),
# calculate and print the amount to be paid by the customer knowing that the price of a liter of gasoline is R $ 2.50 the price of a liter of alcohol is R $ 1.90.

print("""\nDiscount Table:
+ Alcohol:
    - Up to 20 liters, 3% discount per liter;
    - Over 20 liters, 5% discount per liter;
+ Gasoline:
    - Up to 20 liters, 4% discount per liter;
    - Over 20 liters, 6% discount per liter;""")

options = input("""\nChoose an option:
A - Alcohol (R$2,50 / L)
G - Gasoline (R$1,90 / L)
+ Enter the letter of the option: """)

amountOfFuel = int(input("\nEnter the amount of fuel (L): "))
options = options.lower()

# Alcohol
if options == "a" or options == "alcohol":
    if amountOfFuel <= 20:
        price = float(amountOfFuel * 2.50)
        discountPrice = price - ((price * 3) / 100)
        print("\nTotal Price: R${:.2f}\nPrice with discount: R${:.2f}".format(price, discountPrice))

    else:
        price = float(amountOfFuel * 2.50)
        discountPrice = price - ((price * 5) / 100)
        print("\nTotal Price: R${:.2f}\nPrice with discount: R${:.2f}".format(price, discountPrice))

# Gasoline
elif options == "g" or options == "gasoline":
    if amountOfFuel <= 20:
        price = float(amountOfFuel * 2.50)
        discountPrice = price - ((price * 4) / 100)
        print("\nTotal Price: R${:.2f}\nPrice with discount: R${:.2f}".format(price, discountPrice))

    else:
        price = float(amountOfFuel * 2.50)
        discountPrice = price - ((price * 6) / 100)
        print("\nTotal Price: R${:.2f}\nPrice with discount: R${:.2f}".format(price, discountPrice))

else:
    print("\nInvalid Option.")
