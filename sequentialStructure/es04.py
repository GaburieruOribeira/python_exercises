# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Make a Program that asks for the 4 bimonthly notes and shows the average.

medias = []
medias.append(input('\nEnter the first average: '))
medias.append(input('Enter the second average: '))
medias.append(input('Enter the third average: '))
medias.append(input('Enter the fourth average: '))
medias_float = []
try:
    for item in medias:
        medias_float.append(float(item))
    sum = (medias_float[0] + medias_float[1] + medias_float[2] + medias_float[3]) / len(medias)
    print('\nThe final average is: {}'.format(sum))
except ValueError:
    print('\nYou did not enter a number.')
