import pandas as pd
from meses import *

dict_planilha = {}
PLANILHA_FATURA_CARTAO = "fatura_cartao.xlsx"

def registrar():
    while True:
        try:
            mes = int(input('Digite o número do mês da compra (0 para sair): '))
            if mes == 0:
                print('Voltando ao menu...')
                print('-----------------------------------------')
                print()
                break
            elif mes >= 1 and mes <= 12:
                n_parcelas = int(input('Digite o número de parcelas da compra: '))
                if n_parcelas == 1:
                    preco = int(input('Digite o valor da compra: '))
                    registrar_compra_uma_parcela(mes, preco)
                elif n_parcelas > 1:
                    preco = int(input('Digite o valor da compra: '))
                    registrar_compra_mais_parcelas(mes, preco, n_parcelas)
                else:
                    print('Digite um número de parcelas válido')
            else:
                print('Digite um mês válido.')
        except ValueError as v:
            print('Digite valores válidos', v)


def registrar_compra_uma_parcela(mes, preco,):
    mes_extenso = meses[mes - 1]
    if mes_extenso not in dict_planilha:
        dict_planilha[mes_extenso] = []
    dict_planilha[mes_extenso].append(preco)


def registrar_compra_mais_parcelas(mes_inicial, preco, n_parcelas):
    valor_parcela = preco / n_parcelas 

    for i in range(n_parcelas):
        current_mes_index = (mes_inicial - 1 + i) % 12 
        mes_extenso = meses[current_mes_index]

        if mes_extenso not in dict_planilha:
            dict_planilha[mes_extenso] = []
        dict_planilha[mes_extenso].append(valor_parcela)

def load_info_from_excel():
    for meses, faturas in dict_planilha.items():
        df = pd.DataFrame(meses, faturas)
        df.to_excel(PLANILHA_FATURA_CARTAO, index=False)

def exibir():
    print()
    for meses, faturas in dict_planilha.items():
        print(meses, faturas)
    print()

if __name__ == '__main__':
    registrar()
    exibir()
