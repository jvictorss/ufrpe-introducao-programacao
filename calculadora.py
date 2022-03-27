num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
print("Digite uma opção: ")
print("[1] - Soma")
print("[2] - Subtração")
print("[3] - Multiplicação")
print("[4] - Divisão")
print("[5] - Sair")
opcao = int(input())
resultado = None

if opcao == 1:
    resultado = num1 + num2
elif opcao == 2:
    resultado = num1 - num2
elif opcao == 3:
    resultado = num1 - num2
elif opcao == 4:
    resultado = num1 - num2
elif opcao == 5:
    print("Saindo da aplicação")
else:
    print("Opção inválida")

if opcao <= 0 or opcao > 5:
    print("Opção inválida")
else:
    print("O resultado é: ", resultado)
