def get_int_value(msg, min, max):
    while True:
        try:
            op = int(input(msg))
            if op >= min and op <= max:
                return op
            else:
                print('Valor fora do range especificado!')
        except:
            print('Valor inválido')


def show_menu(menu: tuple, min, max):
    for option in menu:
        print(option)
    return get_int_value("opção >> ", min, max)