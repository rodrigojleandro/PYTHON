
########################################################################################

# DESAFIO: 013
# TÍTULO: Reajuste Salarial
# AULA: 07
# EXERCÍCIO: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15 %
# de desconto.

########################################################################################

sal = float(input("Qual é o salário do funcionário? R$ "))
val = float(input("Qual o valor do reajuste?  "))
novo = sal + (sal * val / 100)
print("\nSalário Atual: R$ {:.2f} \nNovo Salário: R$ {:.2f}".format(sal, novo))