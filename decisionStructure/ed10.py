# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Make a Program that asks in which shift you study.
# Ask to type M-morning or V-Evening or N-Night.
# Print the message "Good morning!", "Good afternoon!" or good night!" or "Invalid Value!", as appropriate.

shift = str(input("""\nWhat's your turn:
M - Morning
A - Afternoon
N - Night
+ Choose a letter: """))

if shift.upper() == "M" or shift.upper() == "MORNING":
    print("\nGood Morning!")
elif shift.upper() == "A" or shift.upper() == "AFTERNOON":
    print("\nGood Afternoon!")
elif shift.upper() == "N" or shift.upper() == "NIGHT":
    print("\nGood Night!")
else:
    print("\nInvalid Value.")
