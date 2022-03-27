idade = int(input("Insira a idade: "))

if idade <= 15:
    licencaPais = input("Possui licença dos pais? (Y/N)")
    if licencaPais == "Y":
        print("Parabéns, você está apto a ir pescar")
    else:
        print("Infelizmente você não está apto a pescar")
elif idade == 16:
    licenca = input("Possui licença (Y/N): ")
    if licenca == "Y":
        print("Parabéns, você está apto a ir pescar")
    else:
        print("Infelizmente você não está apto a pescar")
if idade > 16:
    print("Parabéns, você está apto a ir pescar")