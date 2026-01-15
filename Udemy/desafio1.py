# Calcular quantos dias um preoduto duraria se a pessoa usar X porções por dia

produto = int(input('Digite quantos produtos a pessoa tem: '))

uso_por_dia = int(input('Digite quantos produtos a pessoa vai usar por dia: '))

dias_uso = int(produto / uso_por_dia)

print(f'O produto pode ser usado por: {dias_uso} dias')