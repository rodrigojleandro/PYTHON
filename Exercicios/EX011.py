
########################################################################################

# DESAFIO: 011
# TÍTULO: Pintando parede
# AULA: 07
# EXERCÍCIO: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2

########################################################################################

larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt

print("Sua parede tem a dimensão de {} x {} e a sua área é de {}m2.".format(larg, alt, area))

tinta = area /2
print("Para pintar essa parede, você precisará de {}l de tinta.".format(tinta))