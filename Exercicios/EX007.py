
########################################################################################

# DESAFIO: 007
# TÍTULO: Média Aritmética
# AULA: 07
# EXERCÍCIO: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
# a sua média.

########################################################################################

n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
media = (n1 + n2) / 2

print("A média entre {:.1f} e {:.1f} é igual a {:.1f}.".format(n1,n2, media))