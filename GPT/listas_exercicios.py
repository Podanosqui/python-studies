notas = []

nota = float(input("Digite uma nota: "))
notas.append(nota)

nota1 = float(input("Digite uma segunda nota: "))
notas.append(nota1)

nota2 = float(input("Digite uma terceira nota: "))
notas.append(nota2)


def lista_notas(notas):
    if len(notas) == 0:
        return None

    return sum(notas) / len(notas)

# sum soma todos os valores da lista
# len retorna o tamanho da lista, no caso, 3 valores


resultado = lista_notas(notas)

if resultado is None:
    print("Nenhuma nota informada")
else:
    print(f"A média das notas é: {resultado:.2f}")