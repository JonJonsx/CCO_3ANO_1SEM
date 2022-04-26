# encoding: iso-8859-1
from db_manager import DatabaseManager
from generate_data import generate_registros

db = DatabaseManager()


def menu():
    print("-----------------------------")
    print("|1- Gerar valores aleatorios|")
    print("|2- Truncate table          |")
    print("|3- Sair                    |")
    print("-----------------------------")


def batata():
    quit = True
    while quit:
        menu()
        try:
            option = int(input("O que deseja fazer: "))
        except:
            print("Digite um valor valido entre 1 e 3)")

        if option >= 1 or option <= 3:

            if option == 1:
                quantidade = int(input(
                    "Digite a quantidade dados que deseja gerar: "))
                db.insert(generate_registros(quantidade))
            elif option == 2:
                db.truncate_table()
                print("A tabela foi limpa!\n")
            elif option == 3:
                quit = False
        else:
            print("Digite um valor valido entre 1 e 3)")

        option = 0


batata()
