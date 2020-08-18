#TP3 Ej 1

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

def imprimir_matriz(matriz):
    for f in range(0,len(matriz)):
        for c in range(0,len(matriz[f])):
            print("{0:>2}".format(matriz[f][c]), end='|')
        print()


def main():
    fila_columna= 3
    matriz = [[0] * fila_columna for i in range(fila_columna)]
    cargar_matriz(matriz)
    imprimir_matriz(matriz)
    
    
if __name__ == "__main__":
    main()
