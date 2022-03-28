renda = int(input("Insira sua renda anual: "))
qtdDependentes = int(input("Insira a quantidade de dependentes: "))

if renda <= 20000:
    print("A renda deste contribuinte não é base de cálculo para o IR")
elif 20000 < renda <= 50000:
    if qtdDependentes > 0:
        descontoIR = renda * 0.02 * qtdDependentes
        imposto = (renda - descontoIR) * 0.05
        print(f"A renda do contribuinte é de R$ {renda}. Ele tem {qtdDependentes} dependentes. "
              f" O desconto no IR foi de R$ {descontoIR}. E o imposto a ser recolhido é de R$ {imposto}.")
    else:
        imposto = renda * 0.05
        print(f"A renda do contribuinte é de R$ {renda}. Não há dependentes, então não houve desconto do IR."
              f" O imposto a ser recolhido é de R$ {imposto}.")
elif 50000 < renda <= 100000:
    if qtdDependentes > 0:
        descontoIR = renda * 0.02 * qtdDependentes
        imposto = (renda - descontoIR) * 0.1
        print(f"A renda do contribuinte é de R$ {renda}. Ele tem {qtdDependentes} dependentes. "
              f" O desconto no IR foi de R$ {descontoIR}. E o imposto a ser recolhido é de R$ {imposto}.")
    else:
        imposto = renda * 0.1
        print(f"A renda do contribuinte é de R$ {renda}. Não há dependentes, então não houve desconto do IR."
              f" O imposto a ser recolhido é de R$ {imposto}.")
elif 100000 < renda:
    if qtdDependentes > 0:
        descontoIR = renda * 0.02 * qtdDependentes
        imposto = (renda - descontoIR) * 0.15
        print(f"A renda do contribuinte é de R$ {renda}. Ele tem {qtdDependentes} dependentes. "
              f" O desconto no IR foi de R$ {descontoIR}. E o imposto a ser recolhido é de R$ {imposto}.")
    else:
        imposto = renda * 0.15
        print(f"A renda do contribuinte é de R$ {renda}. Não há dependentes, então não houve desconto do IR."
              f" O imposto a ser recolhido é de R$ {imposto}.")