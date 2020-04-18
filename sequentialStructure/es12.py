# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7*altura) - 58

# Using a person's height as input data, build an algorithm that calculates your ideal weight, using the following formula:
# (72.7 * height) - 58

personHeight = float(input("\nEnter your height: "))
idealWeight = ( 72.7 * personHeight ) - 58
print("\nYour ideal weight is: {:.2f}Kg".format(idealWeight))
