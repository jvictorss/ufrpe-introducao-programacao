"""Sabemos que um triângulo é formado por três lados que possuem uma
determinada medida, mas essas não podem ser escolhidas
aleatoriamente como os lados de um quadrado ou de um retângulo, é
preciso seguir uma regra. Só existirá um triângulo se, somente se, os
seus lados obedeceram à seguinte regra: um de seus lados deve ser
maior que o valor absoluto (módulo) da diferença dos outros dois lados e
menor que a soma dos outros dois lados. Veja o resumo da regra
abaixo:
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
Exemplo:
Com os três segmentos de reta medindo 5cm, 10cm e 9cm, podemos formar
um triângulo?

Vamos aplicar a regra da condição de existência de um triângulo para todos os
lados.
|10 – 9| < 5 < 10 + 9
1 < 5 <19 (VERDADEIRO)
|9 – 5| < 10 < 9 + 5
4 < 10 < 14 (VERDADEIRO)
|5 – 10| < 9 < 10 + 5
5 < 9 < 15 (VERDADEIRO)"""

a = int(input("Insisra o 1º lado do triângulo: "))
b = int(input("Insisra o 2º lado do triângulo: "))
c = int(input("Insisra o 3º lado do triângulo: "))

teste1 = abs(b-c) < a < b + c
teste2 = abs(a-c) < b < a + c
teste3 = abs(a-b) < c < a + b

if teste1 and teste2 and teste3:
    print("VERDADEIRO")
else:
    print("FALSO")