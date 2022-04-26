import random

from data_values import CURSOS, ESTADOS, GRAUS, TURNOS


def generate_random_value() -> list:
    random.seed(10)
    registro = [
        random.choice(CURSOS),
        random.choice(GRAUS),
        random.choice(TURNOS),
        random.choice(ESTADOS),
        "{:.2f}".format(random.uniform(300.0, 9999.99)),
        random.randint(1, 15)
    ]
    return registro


def generate_registros(quantidade: int):
    registros = [generate_random_value() for i in range(0, quantidade, 1)]
    return registros
