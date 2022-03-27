"""
Uma cidade classifica um índice de poluição menor que 35 como agradável;
de 35 até 60 desagradável e acima de 60 perigoso. Escreva um programa em
Python que lê um número real representando o índice de poluição e imprime
a classificação adequada para ele.
"""

indice = float(input("Insira o índice atual de poluição: "))

if indice < 35:
    print("A qualidade do ar é considerada AGRADÁVEL")
elif 35 <= indice <= 60:
    print("A qualidade do ar é considerada DESAGRADÁVEL")
elif indice > 60:
    print("Está PERIGOSO o ar desta cidade!")

