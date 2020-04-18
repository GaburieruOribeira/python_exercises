# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# Make a program for reading a student's two partial grades.
# The program should calculate the average achieved per student and present:
# The message "Approved", if the average achieved is greater than or equal to seven;
# The message "Failed", if the average is less than seven;
# The message "Approved with Distinction", if the average is equal to ten.

def AverageCalculation():
    note1 = float(input("\nEnter the first note: "))
    note2 = float(input("\nEnter the second note: "))
    media = float((note1 + note2) / 2)
    print("\nYour final average is: {}".format(media))

AverageCalculation()
