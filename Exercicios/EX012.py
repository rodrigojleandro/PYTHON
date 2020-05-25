
###############################################################################################################

# DESAFIO: 012
# TÍTULO: Calculando desconto
# AULA: 07
# EXERCÍCIO: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

###############################################################################################################

preco = float(input("Qual é o preço do produto? R$"))
desconto = float(input("De quanto é o desconto?  "))
novo = preco - (preco * desconto /100)

print("Produto sem desconto: R${:.2f} \nDesconto: {:.0f}% \nValor Total: R${:.2f}".format(preco, desconto, novo))