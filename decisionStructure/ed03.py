# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# Make a program that checks if a typed letter is "F" or "M". As the letter writes: F - Female, M - Male, Invalid Gender.

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
