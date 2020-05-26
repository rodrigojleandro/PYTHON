
###############################################################################################################

# DESAFIO: 018
# TÍTULO: Seno, cosseno e tangente
# AULA: 08
# EXERCÍCIO: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

###############################################################################################################

import math
angulo = float(input("Digite o ângulo que deseja: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print(" {}º >>> SENO: {:.2F}".format(angulo, seno))
print(" {}º >>> COSSENO: {:.2F}".format(angulo, cosseno))
print(" {}º >>> TANGENTE: {:.2F}".format(angulo, tangente))

