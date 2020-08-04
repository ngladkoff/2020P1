#TP2 Ej1
import random


def a_cargar_lista_random():
    nros= []
    for i in range(random.randint(10,99)):
        nros.append(random.randint(10,99))
    return nros

def b_sumar_lista(lista):
    acumulador = 0
    #for i in range(len(lista)):
    #    acumulador = acumulador + lista[i]
    for numero in lista:
        acumulador += numero
    return acumulador

def c_eliminar_valor_lista(valor, lista):
    while buscar_valor_lista(valor, lista) != -1:
        lista.remove(valor)

def buscar_valor_lista(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def main():
    numeros = a_cargar_lista_random()
    print(numeros)
    sumatoria = b_sumar_lista(numeros)    
    print("Sumatoria: ", sumatoria)
    valor_a_borrar= int(input("Ingrese valor a eliminar: "))
    c_eliminar_valor_lista(valor_a_borrar, numeros)
    print(numeros)

if __name__ == '__main__':
    main()