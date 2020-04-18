# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7*altura) - 58

personHeight = float(input("\nEnter your height: "))
idealWeight = ( 72.7 * personHeight ) - 58
print("\nYour ideal weight is: {:.2f}Kg".format(idealWeight))
