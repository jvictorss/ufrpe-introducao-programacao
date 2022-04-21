def numeroSementes(popDesejada):
    numSementes = popDesejada / (0.95 * 0.9 * 1)

    print(f"A população desejada de plantas é {popDesejada}. Para isto precisaria de {numSementes} número de sementes.")


numeroSementes(10)
