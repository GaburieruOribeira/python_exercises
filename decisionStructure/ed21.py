# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

# Make a program for an ATM. The program should ask the user for the withdrawal amount and then inform how many notes of each amount will be provided. The available grades will be 1, 5, 10, 50 and 100 reais. The minimum value is 10 reais and the maximum 600 reais. The program should not be concerned with the amount of banknotes on the machine.
# - Example 1: To withdraw the amount of 256 reais, the program provides two 100 notes, a 50 note, a 5 note and a 1 note;
# - Example 2: To withdraw the amount of 399 reais, the program provides three notes of 100, a note of 50, four notes of 10, a note of 5 and four notes of 1.

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

print("""R$100,00 notes: {}
R$50,00 notes: {}
R$10,00 notes: {}
R$5,00 notes: {}
R$1,00 notes: {}""".format(hundred, fifty, ten, five, one))
