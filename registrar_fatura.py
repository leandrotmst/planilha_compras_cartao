import pandas as pd
from meses import *

dict_planilha = {}
PLANILHA_FATURA_CARTAO = "fatura_cartao.xlsx"

def registrar():
    while True:
        try:
            mes = int(input('Digite o número do mês da compra (0 para sair): '))
            if mes == 0:
                print('Registro de gastos finalizado. Voltando ao menu principal.')
                print('-----------------------------------------')
                print()
                break
            elif mes >= 1 and mes <= 12:
                n_parcelas = int(input('Digite o número de parcelas da compra: '))
                if n_parcelas == 1:
                    preco = float(input('Digite o valor da compra: '))
                    registrar_compra_uma_parcela(mes, preco)
                elif n_parcelas > 1:
                    preco = float(input('Digite o valor da compra: '))
                    registrar_compra_mais_parcelas(mes, preco, n_parcelas)
                else:
                    print('Digite um número de parcelas válido')
            else:
                print('Digite um mês válido.')
        except ValueError as v:
            print('Digite valores válidos', v)


def registrar_compra_uma_parcela(mes, preco):
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
    global dict_planilha
    try:
        df = pd.read_excel(PLANILHA_FATURA_CARTAO)
        dict_planilha.clear()
        
        for mes, group in df.groupby('Mês'):
            faturas_validas = []
            for fatura_valor in group['Fatura']:
                try:
                    faturas_validas.append(float(fatura_valor))
                except ValueError:
                    pass
            dict_planilha[mes] = faturas_validas

    except FileNotFoundError:
        print(f"Arquivo '{PLANILHA_FATURA_CARTAO}' não encontrado. Iniciando com dados vazios.")
    except Exception as e:
        print(f"Erro ao carregar dados do Excel: {e}")

def save_info_to_excel():
    data_for_df = []
    for mes, faturas_list in dict_planilha.items():
        for fatura in faturas_list:
            data_for_df.append({'Mês': mes, 'Fatura': fatura})
        
        total_mes = sum(faturas_list)
        data_for_df.append({'Mês': mes, 'Fatura': f"Total: {total_mes:.2f}"})

    if not data_for_df:
        print("Nenhum dado para salvar na planilha.")
        return

    df = pd.DataFrame(data_for_df)
    try:
        df.to_excel(PLANILHA_FATURA_CARTAO, index=False)
        print(f"Dados salvos em '{PLANILHA_FATURA_CARTAO}' com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar dados no Excel: {e}")

def exibir():
    print()
    if not dict_planilha:
        print("Nenhuma fatura registrada ainda.")
        print()
        return

    for mes, faturas in dict_planilha.items():
        print(f"Mês: {mes}")
        for fatura in faturas:
            print(f"  - R$ {fatura:.2f}")
        total_mes = sum(faturas)
        print(f"  Total do mês: R$ {total_mes:.2f}")
        print("-" * 30)
    print()

if __name__ == '__main__':
    load_info_from_excel()
    registrar()
    exibir()
    save_info_to_excel()