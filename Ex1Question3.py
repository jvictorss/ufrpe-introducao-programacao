# Uma Empresa de vendas de softwares paga a seu vendedor um fixo de
# R$ 800,00 por mês, mais uma comissão de 25% pelo seu valor de
# vendas no mês. Faça um algoritmo que leia o valor da venda e
# determine o salário total do funcionário. Mostre as informações que você
# achar necessário.

salario = 800
meta = int(input("Insira a meta do vendedor deste mês: "))
vendas = int(input("Insira o montante vendido pelo vendedor este mês: "))

if vendas >= meta:
    comissao = vendas * 0.25
    comissao += salario
    print(f"O vendedor bateu a meta! Parabéns!")
    print(f"O salário do vendedor este mês será de R$ {comissao}")
else:
    print(f"O vendedor não bateu a meta. Que pena!")
    print(f"O salário do vendedor será de apenas R$ {salario}")