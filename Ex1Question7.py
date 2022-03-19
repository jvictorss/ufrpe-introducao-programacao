# O custo ao consumidor de um carro novo, é a soma do custo de fábrica
# com a percentagem do revendedor e com o custo dos impostos
# (aplicados ao custo de fábrica). Supondo que a percentagem do
# revendedor seja de 25% do custo de fábrica e que os impostos custam
# 45 % do custo de fábrica, faça um algoritmo que leia o valor de custo de
# fábrica e determine o preço final do automóvel (custo ao consumidor).

custoFabrica = int(input("Insira o valor de fábrica do veículo: "))
custoRevendedor = custoFabrica * 0.25
impostos = custoFabrica * 0.45
valorFinal = custoFabrica + custoRevendedor + impostos

print(f"O valor final do carro, adicionados R$ {impostos} de impostos e R$ {custoRevendedor} de custo de venda é de: R$ {valorFinal}")