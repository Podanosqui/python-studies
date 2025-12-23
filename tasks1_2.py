nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 12:
    classificacao = "Criança"
elif idade < 18:
    classificacao = "Adolescente"
elif idade < 64:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"
    
print(f"{nome} é {classificacao}")