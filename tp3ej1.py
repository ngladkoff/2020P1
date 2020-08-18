#TP3 Ej 1
import random

class MenorMinimoError(Exception):
    pass


class MayorMaximoError(Exception):
    pass

def validar_numero(texto_numero, nro_min, nro_max):
    numero = int(texto_numero)
    if numero <= nro_min:
        raise MenorMinimoError()
    if numero >= nro_max:
        raise MayorMaximoError()
    return numero

def ingresar_numero(mensaje, nro_min, nro_max, mensaje_min, mensaje_max):
    
    while True:
        try:
            return validar_numero(input(mensaje), nro_min, nro_max)
        
        except ValueError:
            print("Debe ingresar un número entero")
        
        except MenorMinimoError:
            print(mensaje_min)
    
        except MayorMaximoError:
            print(mensaje_max)

def cargar_matriz(matriz):
    for f in range(0,len(matriz)):
        for c in range(0,len(matriz[f])):
            matriz[f][c] = ingresar_numero("Ingrese un número: ", 0, 100, "Ingrese un número mayor a cero", "Ingrese un número menor a 100")

def cargar_matriz_aleatoria(matriz):
    for f in range(0,len(matriz)):
        for c in range(0,len(matriz[f])):
            matriz[f][c] = random.randint(0,99)


def imprimir_matriz(matriz):
    for f in range(0,len(matriz)):
        for c in range(0,len(matriz[f])):
            print("{0:>2}".format(matriz[f][c]), end='|')
        print()

def porcentaje_impares_fila(matriz, fila):
    cantidad_impares = 0
    cantidad_columnas = len(matriz[0])

    for c in range(0, cantidad_columnas):
        if matriz[fila][c] % 2 != 0:
            cantidad_impares = cantidad_impares + 1

    porcentaje = ( cantidad_impares / cantidad_columnas ) * 100
    return porcentaje


def porcentaje_impares_columna(matriz, columna):
    cantidad_impares = 0
    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[0])
    
    for f in range(0, cantidad_filas):
        if matriz[f][columna] % 2 != 0:
            cantidad_impares = cantidad_impares + 1

    porcentaje = ( cantidad_impares / cantidad_filas ) * 100
    return porcentaje


def es_matriz_simetrica(matriz):
    for f in range(0,len(matriz)):
        for c in range(0,len(matriz[f])):
            if matriz[f][c] != matriz[c][f]:
                return False
    return True
    

def main():
    fila_columna= 10
    vector = [(0 * j) for j in range(fila_columna)]
    matriz = [vector for i in range(fila_columna)]
    
    imprimir_matriz(matriz)
    
    matriz_simetrica = [[1,2,3,4,5],[2,1,3,4,7],[3,3,1,4,6],[4,4,4,1,5],[5,7,6,5,1]]
    # imprimir_matriz(matriz_simetrica)
    matriz_asimetrica = [[1,2,3,4,5],[2,1,3,4,7],[3,3,1,4,6],[4,4,4,1,5],[5,7,6,9,1]]
    
    #Ejercicio a
    #cargar_matriz(matriz)
    
    #Ejercicio h
    cargar_matriz_aleatoria(matriz)
    porcentaje = porcentaje_impares_columna(matriz, 5)
    imprimir_matriz(matriz)
    print("Porcentaje: ", porcentaje)
    
    if es_matriz_simetrica(matriz_asimetrica):
        print("Es simetrica")
    else:
        print("Es asimetrica")
        
        
        
if __name__ == "__main__":
    main()
