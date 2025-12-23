nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
tem_convite = input("Tem convite? (s/n): ") == "s"
vip = input("É VIP? (s/n): ") == "s"

if (idade >= 18 and tem_convite) or vip:
    print(f"Acesso permitido, {nome}")
else:
    print(f"Acesso negado, {nome}")