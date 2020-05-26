
###############################################################################################################

# DESAFIO: 015
# TÍTULO: Aluguel de Carros
# AULA: 07
# EXERCÍCIO: Escreve um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar. Sabendo que o carro custa R$60,00 por dia e
# R$0,15 por KM rodado.

###############################################################################################################

dias = int(input("Qtde de dias alugados: "))
km = float(input("Quantos KM rodados?: "))
pgto = (dias * 60) + (km * 0.15)
print("-" * 26)
print(" Total a pagar: R${:.2f}".format(pgto))
print("-" * 26)