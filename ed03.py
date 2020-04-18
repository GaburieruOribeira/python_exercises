# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

gender = str(input("""What's your gender:
F - Feminine
M - Masculine
+ Choose a letter: """))

if gender.lower() == "m" or gender.lower() == "masculine":
    print("\nWelcome sir!")

elif gender.lower() == "f" or gender.lower() == "feminine":
    print("\nWelcome miss!")

else:
    print("\nThis gender does not exist. Please try again")
