nome = input("Insira o nome do funcionário: ")
salAtual = int(input("Insira seu salário atual: "))

if 0 <= salAtual <= 400:
    novoSalario = salAtual + (salAtual*0.15)
    print(f"O salário de {nome} teve 15% de aumento. Antes o salário era de R$ {salAtual} e agora será de R$ {novoSalario}.")
elif 400 < salAtual <= 700:
    novoSalario = salAtual + (salAtual * 0.12)
    print(f"O salário de {nome} teve 12% de aumento. Antes o salário era de R$ {salAtual} e agora será de R$ {novoSalario}.")
elif 700 < salAtual <= 1000:
    novoSalario = salAtual + (salAtual * 0.10)
    print(f"O salário de {nome} teve 10% de aumento. Antes o salário era de R$ {salAtual} e agora será de R$ {novoSalario}.")
elif 1000 < salAtual <= 1800:
    novoSalario = salAtual + (salAtual * 0.07)
    print(f"O salário de {nome} teve 7% de aumento. Antes o salário era de R$ {salAtual} e agora será de R$ {novoSalario}.")
elif 1800 < salAtual <= 2500:
    novoSalario = salAtual + (salAtual * 0.04)
    print(f"O salário de {nome} teve 4% de aumento. Antes o salário era de R$ {salAtual} e agora será de R$ {novoSalario}.")
elif salAtual >= 2500:
    novoSalario = salAtual
    print(f"O Salário de {nome} não sofreu alterações. Permanece de R$ {novoSalario}.")
