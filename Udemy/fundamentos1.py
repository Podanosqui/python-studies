# Criar um programa que calcule 5% de desconto
preco = int(input('Digite o valor do produto: '))

desconto = int(input('Digite o desconto a ser aplicado: '))

novo_preco = preco - (preco * desconto / 100)
print(f'O valor com desconto é de R$ {novo_preco}')