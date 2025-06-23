import utils as u
import registrar_fatura as rf

def main(menu: tuple):
	while True:
		op = u.show_menu(menu, 1, 2)
		if op == 1:
			action = rf.registrar()
			if action == 'EXIT_SYSTEM':
				break
		elif op == 2:
			rf.exibir()
			break


if __name__ == '__main__':
	menu = (
		'1. Registrar gasto',
        '2. Exibir planilha',
	)
	main(menu)