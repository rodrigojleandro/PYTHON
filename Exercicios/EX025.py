
########################################################################################

# DESAFIO: 025
# TÍTULO: Procurando uma string dentro de outra
# AULA:
# EXERCÍCIOS: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

########################################################################################

nome = str(input("Qual o seu nome completo? ")).strip()
print("Seu nome tem Silva? {}".format('SILVA' in nome.upper()))


