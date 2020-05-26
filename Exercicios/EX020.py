
###############################################################################################################

# DESAFIO: 019
# TÍTULO: Sorteando uma ordem na lista
# AULA:
# EXERCÍCIO: O mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

###############################################################################################################

import random
aluno1 = str(input("Nome do Aluno 01: "))
aluno2 = str(input("Nome do Aluno 02: "))
aluno3 = str(input("Nome do Aluno 03: "))
aluno4 = str(input("Nome do Aluno 04: "))
lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print("Ordem de apresentação: {}.".format(lista))