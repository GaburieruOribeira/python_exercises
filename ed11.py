# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# - Salários até R$ 280,00 (incluindo) : aumento de 20%
# - Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - Salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# - O salário antes do reajuste;
# - O percentual de aumento aplicado;
# - O valor do aumento;
# - O novo salário, após o aumento.


689/5000
# Tabajara Organizations decided to give their employees a salary increase and hired them to develop the program that will calculate the adjustments.
# Make a program that receives an employee's salary and readjust it according to the following criteria, based on the current salary:
# - Salaries up to R $ 280.00 (including): 20% increase
# - Salaries between R $ 280.00 and R $ 700.00: 15% increase
# - Salaries between R $ 700.00 and R $ 1500.00: 10% increase
# - Salaries from R $ 1500.00 onwards: 5% increase After the increase is made, inform on the screen:
# - The salary before the adjustment;
# - The percentage of increase applied;
# - The amount of the increase;
# - The new salary, after the increase.

salary = float(input("\nEnter the salary: R$"))

if salary <= 280.00:
    readjustment = salary + ((salary * 20) / 100)
    increaseValue = readjustment - salary
    print("""\nSalary before readjustment: R${:.2f}
Increase percentage: 20%
Increase value: R${:.2f}
New salary: R${:.2f}""".format(salary, increaseValue, readjustment))

elif salary > 280.00 and salary <= 700.00:
    readjustment = salary + ((salary * 15) / 100)
    increaseValue = readjustment - salary
    print("""\nSalary before readjustment: R${:.2f}
Increase percentage: 15%
Increase value: R${:.2f}
New salary: R${:.2f}""".format(salary, increaseValue, readjustment))

elif salary > 700.00 and salary <= 1500.00:
    readjustment = salary + ((salary * 10) / 100)
    increaseValue = readjustment - salary
    print("""\nSalary before readjustment: R${:.2f}
Increase percentage: 10%
Increase value: R${:.2f}
New salary: R${:.2f}""".format(salary, increaseValue, readjustment))

else:
    readjustment = salary + ((salary * 5) / 100)
    increaseValue = readjustment - salary
    print("""\nSalary before readjustment: R${:.2f}
Increase percentage: 5%
Increase value: R${:.2f}
New salary: R${:.2f}""".format(salary, increaseValue, readjustment))
