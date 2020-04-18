# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# - Média de Aproveitamento  Conceito
# - Entre 9.0 e 10.0        A
# - Entre 7.5 e 9.0         B
# - Entre 6.0 e 7.5         C
# - Entre 4.0 e 6.0         D
# - Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

note1 = float(input("\nEnter the first note: "))
note2 = float(input("\nEnter the second note: "))

media = (note1 + note2) / 2

if media >= 9.0 and media <= 10.0:
    print("\nMedia: {:.1f}\nNote: A\nResult: Approved".format(media))
elif media < 9.0 and media >= 7.5:
    print("\nMedia: {:.1f}\nNote: B\nResult: Approved".format(media))
elif media < 7.5 and media >= 6.0:
    print("\nMedia: {:.1f}\nNote: C\nResult: Approved".format(media))
elif media < 6.0 and media >= 4.0:
    print("\nMedia: {:.1f}\nNote: D\nResult: Disapproved".format(media))
elif media < 4.0 and media >= 0:
    print("\nMedia: {:.1f}\nNote: E\nResult: Disapproved".format(media))
else:
    print("\nInvalid Values.")
