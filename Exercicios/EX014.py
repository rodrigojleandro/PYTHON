
###############################################################################################################

# DESAFIO: 014
# TÍTULO: Conversor de Temperaturas
# AULA: 07
# EXERCÍCIO: Escreva um programa qu converta uma temperatura digitada em ºC e converta para ºF.

###############################################################################################################

temp = int(input("Digite a temperatura em ºC: "))
f =((1.8*temp))+32 #Fahrenheit
k = (temp + 273) #kelvin
print(" Celsius: {:.1f} ºc \n Fahrenheit: {:.0f} ºf \n Kelvin: {:.0f} K.".format(temp,f,k))
