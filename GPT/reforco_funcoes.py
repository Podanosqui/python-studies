def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if n1 < 0 or n2 < 0 or n3 < 0:
        return None
    return media

m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
m3 = float(input('Digite a terceira nota: '))

resultado = calcular_media(m1, m2, m3)

if resultado is None:
    print("Erro")

else:
    print(f'A média é de: {resultado:.2f}')