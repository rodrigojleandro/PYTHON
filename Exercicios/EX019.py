
###############################################################################################################

# DESAFIO: 019
# TÍTULO: Sorteando uma ordem na lista
# AULA:
# EXERCÍCIO: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

###############################################################################################################

from random import choice

aluno1 = str(input("Aluno 01: "))
aluno2 = str(input("Aluno 02: "))
aluno3 = str(input("Aluno 03: "))
aluno4 = str(input("Aluno 04: "))
lista = [aluno1, aluno2, aluno3, aluno4]

escolha = choice(lista)

print("Aluno Escolhido: {}.".format(escolha))