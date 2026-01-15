def calcular_desconto(valor, percentual):
    desconto = valor * (percentual / 100)
    valor_final = valor - desconto
    return valor_final, desconto

valor = float(input("Digite o valor a receber o desconto: "))
percentual = float(input("Digite o percentual de desconto: "))

valor_final, desconto = calcular_desconto(valor, percentual)

print(f"Valor final: R$ {valor_final:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
