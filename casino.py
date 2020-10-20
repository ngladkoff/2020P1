# Ejercicio Casino
from typing import List

DESVIO_MAXIMO = 0.005
FRECUENCIA_ESPERADA = 1/37

class Incidencia:
    def __init__(self, ruleta, numero, frecuencia, desvio):
        self.ruleta = ruleta
        self.numero = numero
        self.frecuencia = frecuencia
        self.desvio = desvio


class Tirada:
    def __init__(self, ruleta, numero):
        self.ruleta = ruleta
        self.numero = numero
    def __repr__(self):
        return "{}|{}".format(self.ruleta, self.numero)


class Ruleta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tiradas = 0
        self.ocurrencias = [0] * 37
        self.frecuencias = [0] * 37


def main():
    ruletas = []
    ruletas.append(Ruleta("A"))
    ruletas.append(Ruleta("B"))
    ruletas.append(Ruleta("C"))
    ruletas.append(Ruleta("D"))
    
    tiradas = leer_archivo()
    procesar_tiradas(tiradas, ruletas)
    calcular_frecuencias(ruletas)
    imprimir_informe(ruletas)
    incidencias = calcular_incidencias(ruletas)
    imprimir_incidencias(incidencias)
    exportar_incidencias(incidencias)


def leer_archivo():
    tiradas = []

    with open("ruletas.csv", "r") as archivo:
        for linea in archivo:
            datos = linea[:-1].split(',')
            tiradas.append(Tirada(datos[0], int(datos[1])))

    return tiradas


def procesar_tiradas(tiradas, ruletas):
    for tirada in tiradas:
        idx_ruleta= ord(tirada.ruleta) - 65
        ruletas[idx_ruleta].ocurrencias[tirada.numero] += 1
        ruletas[idx_ruleta].tiradas += 1


def calcular_frecuencias(ruletas : List[Ruleta]):
    for ruleta in ruletas:
        for i in range(0,37):
            ruleta.frecuencias[i]= ruleta.ocurrencias[i] / ruleta.tiradas


def imprimir_informe(ruletas):

    for i in range(0,37):
        print("{0:02d} | {1:1.4f} | {2:1.4f} | {3:1.4f} | {4:1.4f}".format(i,
                                                                           ruletas[0].frecuencias[i],
                                                                           ruletas[1].frecuencias[i],
                                                                           ruletas[2].frecuencias[i],
                                                                           ruletas[3].frecuencias[i]))


def calcular_incidencias(ruletas):
    incidencias = []

    for ruleta in ruletas:
        for i in range(0,37):
            # if abs(ruleta.frecuencias[i] - FRECUENCIA_ESPERADA) > DESVIO_MAXIMO:
            if ruleta.frecuencias[i] > FRECUENCIA_ESPERADA + DESVIO_MAXIMO or ruleta.frecuencias[i] < FRECUENCIA_ESPERADA - DESVIO_MAXIMO:
                #INCIDENCIA
                incidencias.append(Incidencia(ruleta.nombre, i, ruleta.frecuencias[i], ruleta.frecuencias[i] - FRECUENCIA_ESPERADA))

    return incidencias


def imprimir_incidencias(incidencias):
    for incidencia in incidencias:
        print("{0} | {1:02d} | {2:1.4f} | {3:1.4f}".format(incidencia.ruleta,
                                                           incidencia.numero,
                                                           incidencia.frecuencia,
                                                           incidencia.desvio))


def exportar_incidencias(incidencias):
    with open("reporte-incidencias.txt", "w", encoding="utf-8") as arch:
        for incidencia in incidencias:
            arch.write("{0} | {1:02d} | {2:1.4f} | {3:1.4f}\n".format(incidencia.ruleta,
                                                                    incidencia.numero,
                                                                    incidencia.frecuencia,
                                                                    incidencia.desvio))

if __name__ == "__main__":
    main()