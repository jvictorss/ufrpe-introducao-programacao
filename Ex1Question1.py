#1. Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e
#ALTURA e apresente o valor do volume de uma caixa retangular. Utilize
#para o cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA *
#ALTURA.


comprimento = int(input("Insira o comprimento: "))
largura = int(input("Insira a largura: "))
altura = int(input("Insira a altura: "))

volume = comprimento * largura * altura

print(f"O volume da caixa é: {volume}")

