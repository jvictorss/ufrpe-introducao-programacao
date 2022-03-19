# Em uma pizzaria, cada copo de refrigerante custa R$ 0,80 e uma pizza
# mista grande custa R$10,00 mais R$1,50 por tipo de cobertura pedida
# (queijo, presunto, banana, etc.). Uma turma vai à pizzaria e pede uma
# determinada quantidade de copos de refrigerante e uma pizza grande
# com uma determinada quantidade de coberturas. Faça um algoritmo que
# leia a quantidade de copos de refrigerante, a quantidade de coberturas e
# calcule a conta. Leia também a quantidade de pessoas que estão à
# mesa e calcule quanto cada um deve pagar (não esqueça os 10% do
# garçom).

copoRefri = 0.8
pizzaGrande = 10
valorCobertura = 1.5

qtdPessoas = int(input("Quantas pessoas vieram? > "))
if qtdPessoas <= 8:
    print("Uma pizza é suficiente para alimentar todos")
    totalPizzas = pizzaGrande
else:
    qtdPizzas = int(input("Quantas pizzas serão necessárias? >"))
    totalPizzas = qtdPizzas * pizzaGrande

print("E as coberturas? Temos de queijo, presunto, calabresa e banana")
qtdCobertura = int(input("Agora escolha quantas bordas quererão (de 1 a 4): >"))
totalCobertura = qtdCobertura * valorCobertura

qtdRefrigerante = int(input("Quantos copos de refrigerante? >"))
totalRefrigerante = qtdRefrigerante * copoRefri

contaSemGorjeta = totalPizzas + totalCobertura + totalRefrigerante
gorjeta = contaSemGorjeta * 0.1
totalConta = contaSemGorjeta + gorjeta
if qtdRefrigerante == qtdPessoas:
   rateioConta = totalConta / qtdPessoas
   print(f"O total da conta é {totalConta}.")
   print(f"Para cada membro da turma dá: {rateioConta}. Já contando a gorjeta.")
else:
   rateioRefri = ((totalPizzas/ qtdPessoas) * qtdRefrigerante) + totalRefrigerante + gorjeta
   naoBeberam = (totalPizzas/qtdPessoas) + gorjeta
   print(f"O total da conta é: {totalConta}.")
   print(f"O total da conta para quem quis refrigerante foi: R${rateioRefri}.")
   print(f"O total da conta para quem não quis refrigerante foi: R${naoBeberam}.")
