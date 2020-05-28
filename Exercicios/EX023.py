
########################################################################################

# DESAFIO: 023
# TÍTULO: Separando dígitos de um número
# AULA: 09
# EXERCÍCIOS: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
# dígitos separados.
# Ex.: Digite um número: 1834
#      Unidade: 4 | Dezena: 3 | Centena: 8 | Milhar: 1

########################################################################################

num = int(input("Digite um número entre 0 e 9999:  "))
if num < 0 or num > 9999:
    print("Número inválido. \nDigite um número entre 0 e 9999.")
else:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    print("\nVerificando {}.".format(num))
    print("\n| Milhar: {} | Centena: {} | Dezena: {} | Unidade: {} |".format(m, c, d, u ))


