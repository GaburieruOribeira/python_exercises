# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

withdrawalAmount = int(input("\nThe minimum value is R$10 and the maximum R%600\nEnter withdrawal Amount: R$"))
notes = [1, 5, 10, 50, 100]
hundred = int(withdrawalAmount / 100)
withdrawalAmount = withdrawalAmount - (hundred*100)
fifty = int(withdrawalAmount / 50)
withdrawalAmount = withdrawalAmount - (fifty * 50)
ten = int(withdrawalAmount / 10)
withdrawalAmount = withdrawalAmount - (ten * 10)
five = int(withdrawalAmount / 5)
withdrawalAmount = withdrawalAmount - (five * 5)
one = withdrawalAmount

print("""Notas de R$100,00: {}
Notas de R$50,00: {}
Notas de R$10,00: {}
Notas de R$5,00: {}
Notas de R$1,00: {}""".format(hundred, fifty, ten, five, one))
