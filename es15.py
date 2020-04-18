# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) Salário bruto.
# b) Quanto pagou ao INSS.
# c) Quanto pagou ao sindicato.
# d) O salário líquido.
# e) Calcule os descontos e o salário líquido, conforme a tabela abaixo:

hourlyWage = float(input('\nHow much salary do you earn per hour? R$'))
workedHours = float(input('\nHow many hours do you work in this month? '))
grossSalary = hourlyWage * workedHours
IR = (grossSalary * 11) / 100
INSS = (grossSalary * 8) / 100
Sind = (grossSalary * 5) / 100
netSalary = grossSalary - IR - INSS - Sind
print("\n+ Salário Líquido: R${:.2f}\n- IR (11%): R${:.2f}\n- INSS (8%): R${:.2f}\n- Sindicato (5%): R${:.2f}\n= Salário Liquido: R${:.2f}".format(grossSalary, IR, INSS, Sind, netSalary))
