# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# - Desconto do IR:
# - Salário Bruto até 900 (inclusive) - isento
# - Salário Bruto até 1500 (inclusive) - desconto de 5%
# - Salário Bruto até 2500 (inclusive) - desconto de 10%
# - Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Make a program for the calculation of a payroll, knowing that the discounts are from the Income Tax, which depends on the gross salary (as shown in the table below) and 3% for the Union and that the FGTS corresponds to 11% of the Gross Salary , but it is not discounted (it is the company that deposits).
# Net Salary corresponds to Gross Salary less discounts.
# The program should ask the user for the value of their hour and the number of hours worked in the month.
# - IR Discount:
# - Gross Salary up to 900 (inclusive) - exempt
# - Gross Salary up to 1500 (inclusive) - 5% discount
# - Gross Salary up to 2500 (inclusive) - 10% discount
# - Gross Salary above 2500 - 20% discount Print the information on the screen, arranged according to the example below. In the example the hour value is 5 and the hour amount is 220.

hourlyWage = float(input('\nHow much salary do you earn per hour? R$'))
workedHours = float(input('\nHow many hours do you work in this month? '))
grossSalary = hourlyWage * workedHours

IR = (grossSalary * 5) / 100
INSS = (grossSalary * 10) / 100
FGTS = (grossSalary * 11) / 100
totalTaxes = IR + INSS
netSalary = grossSalary - totalTaxes

print("""\nGross Salary: ({} * {}) : R${:.2f}
(-) IR (5%)                 : R${:.2f}
(-) INSS (10%)              : R${:.2f}
FGTS (11%)                  : R${:.2f}
Total taxes                 : R${:.2f}
Net Salary                  : R${:.2f}""".format(hourlyWage, workedHours, grossSalary, IR, INSS, FGTS, totalTaxes, netSalary))
