# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

medias = []
medias.append(input('\nDigite a primeira média: '))
medias.append(input('Digite a segunda média: '))
medias.append(input('Digite a terceira média: '))
medias.append(input('Digite a quarta média: '))
medias_float = []
try:
    for item in medias:
        medias_float.append(float(item))
    sum = (medias_float[0] + medias_float[1] + medias_float[2] + medias_float[3]) / len(medias)
    print('\nA média final é: {}'.format(sum))
except ValueError:
    print('\nVocê não digitou um número')
