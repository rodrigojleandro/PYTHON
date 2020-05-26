
###############################################################################################################

# DESAFIO: 017
# TÍTULO: Catetos e hipotenusa
# AULA: 08
# EXERCÍCIO: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.

###############################################################################################################

import math
co = float(input("Comprimento do cateto oposto: ")) # Cateto Oposto
ca = float(input("Comprimento do cateto adjacente: ")) #ca = Cateto Adjacente
hi = math.hypot(co, ca) #hi = hipotenusa

print(" [+] HIPOTENUSA: {:.2F}".format(hi))
