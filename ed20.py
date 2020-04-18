# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# - A mensagem "Aprovado com Distinção", se a média for igual a 10.

note1 = float(input("\nEnter the first note: "))
note2 = float(input("\nEnter the second note: "))
note3 = float(input("\nEnter the third note: "))

media = (note1 + note2 + note3) / 3

if media == 10:
    print("\nMedia = {:.1f}\nApproved with distinction".format(media))
elif media >= 7:
    print("\nMedia = {:.1f}\nApproved".format(media))
else:
    print("\nMedia = {:.1f}\nDisapproved".format(media))
