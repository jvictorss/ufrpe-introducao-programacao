"""
Crie um programa em Python que simule um menu de 5 opções. Ao
digitar a opção desejada o programa deverá imprimir na tela:
'Você escolheu a opção X' e aguardar que o usuário pressione
alguma tecla para encerrar o programa. O programa não deverá
aceitar opções que não fazem parte do menu.
Menu: [1] - Cadastrar
      [2] - Pesquisar
      [3] - Remover
      [4] - Editar
      [5] - Sair
"""
print("Olá. Seja bem-vindo(a)!")
print("Qual das opções abaixo no nosso menu, você escolhe?")
print("Menu: [1] - Cadastrar")
print("      [2] - Pesquisar")
print("      [3] - Remover")
print("      [4] - Editar")
print("      [5] - Sair")

opcaoMenu = int(input())
if opcaoMenu == 1:
    print("Você escolheu a opção CADASTRAR.")
    sair = input()
    print("Encerrando o programa. Saindo...")
elif opcaoMenu == 2:
    print("Você escolheu a opção PESQUISAR.")
    sair = input()
    print("Encerrando o programa. Saindo...")
elif opcaoMenu == 3:
    print("Você escolheu a opção REMOVER.")
    sair = input()
    print("Encerrando o programa. Saindo...")
elif opcaoMenu == 4:
    print("Você escolheu a opção EDITAR.")
    sair = input()
    print("Encerrando o programa. Saindo...")
elif opcaoMenu == 5:
    print("Você escolheu a opção SAIR.")
    print("Até breve!")
    sair = input()
    print("Encerrando o programa. Saindo...")
elif opcaoMenu == input():
    print("Encerrando o programa. Saindo...")
else:
    print("Opção inválida.")
