
########################################################################################

# DESAFIO: 005
# TÍTULO: Antecessor e sucessor
# AULA: 07
# EXERCÍCIO: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor
# e seu antecessor.

########################################################################################

n = int(input('Digite um número:'))
a = n - 1
b = n + 1
print("Utilizando 2 variáveis. \n Analisando o valor {}, seu antecessor é {} e o sucessor é {}.".format(n, a, b))
print("utilizando 1 variável. \n Analisando o valor {}, seu antecessor é {} e o sucessor é {}.".format(n,(n-1),(n+1)))

