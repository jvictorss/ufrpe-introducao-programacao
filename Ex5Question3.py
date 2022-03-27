"""
Uma loja que trabalha com crediário funciona da seguinte maneira: se o
pagamento ocorre até o dia do vencimento, o cliente ganha 10% de desconto
e é avisado que o pagamento está em dia. Se o pagamento é realizado até 5
dias após o vencimento, o cliente perde o desconto, e se o pagamento atrasa
mais de cinco dias, é cobrada uma multa de 2% por dia de atraso. Faça um
programa em Python que lê o dia do vencimento, o dia do pagamento e o valor da
prestação e calcule o valor a ser pago pelo cliente, exibindo as devidas mensagens.
Obs.: suponha que todo vencimento ocorre até o dia dez de cada mês e os clientes
nunca deixam para pagar no mês seguinte.
"""

vencimento = 10
diaPagamento = int(input("Insira a data, em número, de hoje: "))
valorPrestacao = float(input("Insira o valor da prestacao: "))
novoDiaPagamento = diaPagamento-vencimento

if diaPagamento <= vencimento:
    valorPrestacao *= 0.9
    print("Você está com o pagamento em dias. Recebeu 10% de desconto.")
    print(f"O valor que pagará será R$ {valorPrestacao}.")
elif diaPagamento <= vencimento+5:
    print(f"Hoje é dia {diaPagamento}. Você está {novoDiaPagamento} dias atrasado. Mas tudo bem.")
    print("O seu pagamento será integral, mas também não tem juros.")
    print(f"O valor da sua prestação será de R$ {valorPrestacao}.")
else:
    multa = ((valorPrestacao * 0.02) * (diaPagamento - vencimento))
    valorPrestacao += multa
    print(f"Hoje é dia {diaPagamento}. Você está {novoDiaPagamento} dias atrasado.")
    print("Infelizmente haverá cobrança de multa de 2% ao dia.")
    print(f"A multa será de R$ {multa}. E o novo valor de pagamento será R$ {valorPrestacao}.")

