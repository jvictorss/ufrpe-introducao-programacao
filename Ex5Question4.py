"""
Faça um programa em Python para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
- a mensagem "Aprovado", se a média alcançada for maior ou igual a 7,0 (sete);
- a mensagem "Reprovado", se a média for menor que sete;
- a mensagem "Aprovado com distinção", se a média for igual a dez.
"""

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
media = (nota1+nota2)/2

if media == 10:
    print(f"A média foi {media}")
    print("Aprovado com distinção")
elif media < 7:
    print(f"A média foi {media}")
    print("Reprovado")
elif media >= 7:
    print(f"A média foi {media}")
    print("Aprovado")