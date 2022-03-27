nome = input("Insira seu nome:")
idade = int(input("Insira sua idade:"))

if idade <= 10:
    print(f"O plano de saúde de {nome} custará R$ 30,00 por mês.")
elif 10 < idade <= 29:
    print(f"O plano de saúde de {nome} custará R$ 60,00 por mês.")
elif 29 < idade <= 45:
    print(f"O plano de saúde de {nome} custará R$ 120,00 por mês.")
elif 45 < idade <= 59:
    print(f"O plano de saúde de {nome} custará R$ 150,00 por mês.")
elif 59 < idade <= 65:
    print(f"O plano de saúde de {nome} custará R$ 250,00 por mês.")
elif idade > 65:
    print(f"O plano de saúde de {nome} custará R$ 400,00 por mês.")