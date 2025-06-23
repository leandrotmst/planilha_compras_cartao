# Adicionar as compras já nos meses registrados.
# if e elif

faturas = {}

mes = input('mes: ')
preco = int(input('valor: '))
for i in range(3):
    faturas[mes] = f'{preco} ' * i

print(faturas)