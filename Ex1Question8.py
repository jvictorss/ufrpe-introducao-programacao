# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
# calcular e escrever o valor correspondente em graus Celsius (baseado
# na fórmula abaixo):
#C/5 = (F-32)/9
# Obs: Para testar se a solução está correta saiba que 100o C = 212 F
import time

grausF = int(input("Insira os graus em Fahrenheit: "))
grausC = ((grausF-32)/9)*5
print("Convertendo para Celsius")
time.sleep(3)
print("Terminando a conversão...")
time.sleep(2)
print("Finalizado!")
print(f"{grausF} graus Fahrenheit em Celsius resulta em: {grausC} graus Celsius")



