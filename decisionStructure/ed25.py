# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# - "Telefonou para a vítima?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - "Devia para a vítima?"
# - "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

# Make a program that asks a person 5 questions about a crime. The questions are:
# - "Did you call the victim?"
# - "Were you at the crime scene?"
# - "Do you live near the victim?"
# - "Should it be for the victim?"
# - "Have you worked with the victim?"
# The program must ultimately issue a rating on the person's participation in the crime.
# If the person responds positively to 2 questions, he should be classified as "Suspect", between 3 and 4 as "Accomplice" and 5 as "Assassin".
# Otherwise, it will be classified as "Innocent".

questions = ["\nDid you call the victim?", "\nWere you at the crime scene?", "\nDo you live near the victim?", "\nShould it be for the victim?", "\nHave you worked with the victim?"]
answers = []

for i in range(5):
    print(questions[i])
    answers.append(input("Answer with YES or NO: "))

answers = [element.lower() for element in answers]
affirmative = answers.count("yes")

if affirmative == 2:
    print("\nSuspect")
elif affirmative == 3 or affirmative == 4:
    print("\nAccomplice")
elif affirmative == 5:
    print("\nAssassin")
else:
    print("\nInnocent")
