#Generar archivo Casino
from dataclasses import dataclass
import random

RULETAS= ["A", "B", "C", "D"]


@dataclass
class Jugada:
    ruleta: str
    numero: int


jugadas = []
random.seed()

for i in range(0,15000):
    jugadas.append(Jugada(RULETAS[random.randint(0,3)], random.randint(0,36)))

with open("ruletas.csv", "w", encoding="utf-8") as file:
    for i in range(0,15000):
        file.write("{0},{1}\n".format(jugadas[i].ruleta,jugadas[i].numero))

