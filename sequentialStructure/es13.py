# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a) Para homens: (72.7*h) - 58
# b) Para mulheres: (62.1*h) - 44.7

# Taking as input the height (h) of a person, build an algorithm that calculates your ideal weight, using the following formulas:
# a) For men: (72.7 * h) - 58
# b) For women: (62.1 * h) - 44.7

gender = input("\nWhat's your gender (male or female)? ")
if gender == "male":
    personHeight = float(input("\nEnter your height: "))
    personWeight = ( 72.7 * personHeight) - 58
    print("\nYour ideal weight is: {:.2f}Kg".format(personWeight))
elif gender == "female":
    personHeight = float(input("\nEnter your height: "))
    personWeight = ( 62.1 * personHeight) - 44.7
    print("\nYour ideal weight is: {:.2f}Kg".format(personWeight))
else:
    print("\nYou didn't enter your gender. Please try again.")
