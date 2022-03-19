#Faça um algoritmo que leia a idade de uma pessoa expressa em anos,
#meses e dias e escreva a idade dessa pessoa expressa apenas em
#dias. Considerar ano com 365 dias e mês com 30 dias.

idadeAnos = int(input("Insira sua idade em anos: "))
idadeMeses = int(input("Agora insira quantos meses faz desde seu último aniversário: "))
idadeDias = int(input("E, por último, quantos dias: "))

idadeFinalDias = (idadeAnos * 365) + (idadeMeses * 30) + idadeDias

print(f"Você viveu até hoje {idadeFinalDias} dias")