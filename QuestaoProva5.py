salarios = []
count = 0
while count < 5:
    salario = int(input("Insira o salário: "))
    salarios.append(salario) # Fiz salarios.add(salario)
    count += 1

maiorSalario = max(salarios, key=int) # Fiz salarios.max()
mediaSalarial = sum(salarios) / len(salarios) # Fiz salarios.sum() / salarios.length()

print(f"A média salarial é de R$ {mediaSalarial}")
print(f"O maior salário é de R$ {maiorSalario}")