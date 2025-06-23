import utils as u
import registrar_fatura as rf

def main(menu: tuple):
    rf.load_info_from_excel() 
    while True:
        op = u.show_menu(menu, 1, 3)
        if op == 1:
            rf.registrar() 
        elif op == 2:
            rf.exibir() 
        elif op == 3:
            rf.save_info_to_excel() 
            print("Saindo do programa.")
            break


if __name__ == '__main__':
    menu = (
        '1. Registrar gasto',
        '2. Exibir planilha',
        '3. Sair',
    )
    main(menu)