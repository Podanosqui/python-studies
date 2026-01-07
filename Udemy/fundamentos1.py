# Criar um programa que calcule 5% de desconto

valorInt = float(input("Digite o valor a receber o desconto: "))

desconto = 0.05

valorDesconto = valorInt * desconto

valorInt = valorInt - valorDesconto

print(f'O valor final é de {valorInt}, e você recebeu {valorDesconto} de desconto')