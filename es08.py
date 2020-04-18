# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hourlyWage = float(input('\nHow much salary do you earn per hour? US$'))
workedHours = float(input('\nHow many hours do you work in this month? '))
salaryMonth = hourlyWage * workedHours
print('\nYour salary this month is: US${:.2f}'.format(salaryMonth))
