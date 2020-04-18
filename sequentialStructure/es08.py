# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# Make a Program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show your total salary for that month.

hourlyWage = float(input('\nHow much salary do you earn per hour? US$'))
workedHours = float(input('\nHow many hours do you work in this month? '))
salaryMonth = hourlyWage * workedHours
print('\nYour salary this month is: US${:.2f}'.format(salaryMonth))
