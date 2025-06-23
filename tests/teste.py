# Adicionar as compras já nos meses registrados.
# if e elif

# faturas = {}

# mes = input('mes: ')
# preco = int(input('valor: '))
# for i in range(3):
#     faturas[mes] = f'{preco} ' * i

# print(faturas)

dict_planilha = {'janeiro': [10, 20, 30, 50],
                 'fevereiro': [11, 23, 52523]}

segundo_mes = 'fevereiro'

dict_planilha[segundo_mes].append(500)
for meses,faturas in dict_planilha.items():
    print(meses, faturas)
