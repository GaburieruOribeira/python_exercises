# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# - "Telefonou para a vítima?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - "Devia para a vítima?"
# - "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

questions = ["\nTelefonou para a vítima?", "\nEsteve no local do crime?", "\nMora perto da vítima?", "\nDevia para a vítima?", "\nJá trabalhou com a vítima?"]
answers = []

for i in range(5):
    print(questions[i])
    answers.append(input("Answer with YES or NO: "))

answers = [element.lower() for element in answers]
affirmative = answers.count("yes")

if affirmative == 2:
    print("\nSuspeita")
elif affirmative == 3 or affirmative == 4:
    print("\nCúmplice")
elif affirmative == 5:
    print("\nAssassino")
else:
    print("\nInocente")
