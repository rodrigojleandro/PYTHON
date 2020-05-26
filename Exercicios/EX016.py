
###############################################################################################################

# DESAFIO: 016
# TÍTULO: Quebrando um número
# AULA: 08
# EXERCÍCIO: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# eX.: Digite um número 6.127. O número 6.127 tem a parte inteira 6.

###############################################################################################################

from math import trunc

num = float(input("Digite um valor qualquer: "))
print(" \n Valor Digitado: {} \n Porção inteira: {} ".format(num,trunc(num)))

print(" \n Valor Digitado: {} \n Porção inteira: {} ".format(num, int(num)))