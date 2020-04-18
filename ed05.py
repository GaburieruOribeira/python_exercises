# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

def AverageCalculation():
    note1 = float(input("\nEnter the first note: "))
    note2 = float(input("\nEnter the second note: "))
    media = float((note1 + note2) / 2)
    print("\nYour final average is: {}".format(media))

AverageCalculation()
