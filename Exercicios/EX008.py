
########################################################################################

# DESAFIO: 008
# TÍTULO: Conversor de Medidas
# AULA: 07
# EXERCÍCIO: Escreva um programa que leia um valor em metros e a exiba convertido em

########################################################################################

medida = float(input("Digite uma distância em metros: "))
cm = medida * 100
mm = medida * 1000

print("A media de {}m corresponde a: \n{} cm \n{} mm".format(medida,cm,mm))
