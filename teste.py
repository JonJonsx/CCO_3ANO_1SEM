# encoding: iso-8859-1
import random
from data_values import CURSOS,TURNOS,ESTADOS,GRAUS

def generate_random_value() -> list:
    registro = [
        random.choice(CURSOS),
        random.choice(TURNOS),
        random.choice(ESTADOS),
        random.choice(GRAUS),
        "{:.2f}".format(random.uniform(300.0,9999.99))
    ]
    return registro

def generate_registros(quantidade:int):
    registros = [generate_random_value() for i in range(1,quantidade,1)]
    return registros

print(generate_registros(10))