numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print(numeros)

soma = 0 

for total in numeros:
    soma = soma + total

media = soma / len(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")
