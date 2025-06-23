import pandas as pd
from meses import *

# planilha = "fatura_cartao.xlsx"

planilha = {}

def registrar():
    while True:
        try:
            mes = int(input('Digite o número do mês da compra (0 para sair): '))
            if mes == 0:
                print('Obrigado, volte sempre!!')
                return 'EXIT_SYSTEM'
            elif mes > 0 and mes < 13:
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
        except:
            print('Digite valores válidos')


def registrar_compra_uma_parcela(mes, preco,):
    mes_extenso = meses[mes - 1]
    planilha[mes_extenso] = preco


def registrar_compra_mais_parcelas(mes, preco, n_parcelas):
    pass


def exibir():
    for meses, faturas in planilha:
        print(meses, faturas)

if __name__ == '__main__':
    registrar()
    exibir()