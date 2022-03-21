# def soma(num1, num2):
#     return num1 + num2
#
#
# num1 = int(input("Insira o primeiro número: "))
# num2 = int(input("Insira o segundo número: "))
#
# print("O resultado da soma é: ", soma(num1, num2))

# Média:
# Entrada:
lista = []
alunosAprovados = []
alunosReprovados = []
while len(alunosAprovados) < 5:
    nomeAluno = input("Insira o nome do aluno: ")
    nota1 = int(input("Insira a primeira nota: "))
    nota2 = int(input("Insira a segunda nota: "))
    lista.append(nota1)
    lista.append(nota2)

    # Procesamento
    mediaAluno = (nota1+nota2)/2
    if mediaAluno < 7:
        print(f"A média do aluno {nomeAluno} é: {mediaAluno}")
        print("-------------------------------------------------------")
        print(f"O aluno {nomeAluno} ainda não foi aprovado. Precisa fazer 3a VA.")
        print("-------------------------------------------------------")
        nota3 = int(input("Insira a terceira nota: "))
        lista.append(nota3)
        mediaAluno = (nota3 + max(lista))/2
        print(f"A nova média do aluno {nomeAluno} é: {mediaAluno}")
        print("-------------------------------------------------------")
    if mediaAluno >= 7:
        print(f"Aluno {nomeAluno} foi aprovado com média {mediaAluno}")
        print("-------------------------------------------------------")
        alunosAprovados.append(nomeAluno)
    else:
        print(f"O aluno {nomeAluno} precisará fazer a VA Final")
        print("-------------------------------------------------------")
        notaFinal = int(input("Insira a nota da VA Final: "))
        if ((mediaAluno + notaFinal)/2) >= 5:
            print(f"Aluno {nomeAluno} aprovado após VA Final")
            print("-------------------------------------------------------")
        else:
            print(f"Aluno {nomeAluno} reprovado.")
            print("-------------------------------------------------------")
            alunosReprovados.append(nomeAluno)


print(f"A lista de Alunos Aprovados contém: {alunosAprovados}")
print(f"A lista de Alunos Reprovados contém: {alunosReprovados}")
