# O dono de uma sapataria deseja engraxar todos os sapatos que ele tem
# na loja dele. Ajude-o escrevendo um programa que dado o número de
# pares de sapato, retorne: o número de sapatos, o tempo que levará para
# que todos os sapatos sejam engraxados e o gasto que ele terá.
# Sabendo que ele tem a disposição apenas um engraxate, que demora
# 30 minutos por sapato e cobra R$ 25,00 por hora.

pares = int(input("Insira a quantidade de pares de sapatos: "))
tempoPares = 1
valorHora = 25

tempoHoras = pares * tempoPares
despesaFinal = pares * valorHora

print(f"O engraxate levará {tempoHoras} horas para finalizar e a despesa será de R$ {despesaFinal}.")