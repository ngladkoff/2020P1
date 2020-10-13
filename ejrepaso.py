#Ejercicio Repaso
from dataclasses import dataclass

GENERO_ACCION= 1
GENERO_DRAMA= 2
GENERO_COMEDIA= 3

class ParNoEncontradoException(Exception):
    pass


def mayor_nro_par(vector):
    i_mayor = 0
    while True:
        if vector[i_mayor] % 2 != 0:
            i_mayor += 1
            if i_mayor >= len(vector):
                raise ParNoEncontradoException
        else:
            break

    for idx in range(0,len(vector)):
        if vector[idx] > vector[i_mayor]:
            if vector[idx] % 2 == 0:
                i_mayor= idx
    return vector[i_mayor]


def ejercicio_1():
    mi_vector= [11,1,3,6,7,9,8,5,0]
    #mi_vector= [11,1,3,1,7,9,3,5,7]
    try:
        respuesta= mayor_nro_par(mi_vector)
        print("Respuesta: ", respuesta)
    except ParNoEncontradoException:
        print("El vector no contiene numeros pares")


class Posicion:
    def __init__(self, fila, columna):
        self.fila= fila
        self.columna= columna


def buscar_en_matriz(valor_a_buscar, matriz):
    for fila in range(0, len(matriz)):
        for columna in range(0, len(matriz[fila])):
            if valor_a_buscar == matriz[fila][columna]:
                return Posicion(fila,columna)

    return Posicion(-1,-1)


def ejercicio_2():
    matriz= [[1,2,3,4,5],[5,6,7,8,5],[9,10,11,12,5],[13,14,15,16,5]]
    valor= 10
    pos = buscar_en_matriz(valor,matriz)
    print("Posición: Fila:{0} Columna:{1}".format(pos.fila, pos.columna))


def buscar_nombre(nombre, vector):
    for i in range(0, len(vector)):
        if vector[i] == nombre:
            return i
    return -1


def ejercicio_3():
    vector = ["Juan", "Carlos", "Alberto", "Alejandro"]
    respuesta = buscar_nombre("Alberto", vector)
    print("Respuesta: ", respuesta)
    respuesta = buscar_nombre("Nicolas", vector)
    print("Respuesta: ", respuesta)


@dataclass
class Pelicula:
    nombre: str
    anio: int
    genero: int


def listar_peliculas_genero(genero, peliculas):
    with open ('peliculas.txt', 'w', encoding='utf-8') as archivo:
        for i in range(0,len(peliculas)):
            if peliculas[i].genero == genero:
                archivo.write("{0:4d} | {1}\n".format(peliculas[i].anio, peliculas[i].nombre))


def ejercicio_4(peliculas):
    listar_peliculas_genero(GENERO_COMEDIA, peliculas)


def ejercicio_5(peliculas):
    with open ('peliculas.csv', 'w', encoding='utf-8') as archivo:
        for i in range(0,len(peliculas)):
            archivo.write("{0},{1},{2}\n".format(peliculas[i].anio, peliculas[i].nombre, peliculas[i].genero))

def main():
    peliculas = [Pelicula("Pelicula 1", 2020, GENERO_ACCION), Pelicula("Pelicula 2", 1990, 2),Pelicula("Pelicula 3", 2010, 1),Pelicula("Pelicula 4", 2019, 3),Pelicula("Pelicula 5", 2019, 3)]
    #ejercicio_1()
    #ejercicio_2()
    #ejercicio_3()
    #ejercicio_4(peliculas)
    ejercicio_5(peliculas)


if __name__ == '__main__':
    main()