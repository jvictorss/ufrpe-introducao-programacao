# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a
# média final deste aluno. Considerar que a média é ponderada e que o
# peso das notas é 2, 3 e 5.

nomeAluno = input("Digite o nome do aluno: ")
print("A nota 1 tem peso 2.")
nota1 = int(input("Digite a nota 1: "))
notaFinal1 = nota1 * 2
print(notaFinal1)
print("A nota 2 tem peso 3.")
nota2 = int(input("Digite a nota 2: "))
notaFinal2 = nota2 * 3
print(notaFinal2)
print("A nota 3 tem peso 5.")
nota3 = int(input("Digite a nota 3: "))
notaFinal3 = nota3 * 5
print(notaFinal3)

mediaPonderada = (notaFinal1 + notaFinal2 + notaFinal3)/(2+3+5)
print(f"A média de {nomeAluno} foi {mediaPonderada}")
if mediaPonderada >= 7:
    print(f"{nomeAluno} foi aprovado(a)!")
else:
    print(f"{nomeAluno} foi reprovado.")
