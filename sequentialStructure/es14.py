# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

# João Papo-de-Pescador, a good man, bought a microcomputer to control the daily income of his work.
# Every time he brings a weight of fish greater than that established by the fishing regulation of the state of São Paulo (50 kilos) he must pay a fine of R $ 4.00 per kilo in excess.
# João needs you to make a program that reads the variable weight (fish weight) and calculates the excess.
# Record in the excess variable the amount of kilos beyond the limit and in the fine variable the amount of the fine that João must pay.
# Print the program data with the appropriate messages.

fishWeight = float(input("\nEnter the weight of the fish: "))
excess = fishWeight - 50.0
fine = excess * 4.00
print("\nExcess: {:.2f}Kg\nFine price: R${:.2f}".format(excess, fine))
