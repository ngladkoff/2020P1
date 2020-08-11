#TP2 Ej5

def sumar_elementos_hasta(lista, hasta):
    """Funcion que suma elementos de la lista hasta una determinada posición

    Args:
        lista ([int]): Lista de enteros a recorrer
        hasta (int): Ultimo indice a sumar

    Returns:
        int: Devuelve el resultado de la suma
    """
    acumulador = 0
    for i in range(0, hasta + 1):
        acumulador += lista[i]

    return acumulador

def main():
    lista = [1,1,2,3,5,8,13,21]
    lista_acumulada = []

    for i in range(0, len(lista)):
        lista_acumulada.append(sumar_elementos_hasta(lista, i))

    print(lista)
    print(lista_acumulada)


if __name__ == '__main__':
    main()