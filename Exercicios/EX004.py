
###############################################################################################################

# DESAFIO: 004
# TÍTULO: Dissecando uma variável
# AULA: 06
# EXERCÍCIO: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ela.

###############################################################################################################

a = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um número?", a.isnumeric())
print("É alfabético? ,", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Esta em maiúsculas?", a.islower())
print("Esta em minúsculas?", a.isupper())
print("Esta capitalizada?", a.istitle())
