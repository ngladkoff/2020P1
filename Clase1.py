# Modulo Clase1
import random
import funciones
import constantes

MAXIMO = 6

#def saludar_mal_definida():
#    print("Hola ", nombre_saludar)

def saludar(nombre):
    print("Hola ", nombre)
    return "Hola " + nombre
    
def imprimir_nombres(nombres):
    for i in range(constantes.MAX):
        print(nombres[i])
    
def main():
    nombre_saludar = "Carlos"
    nombres = ["Nicolas","Alejandro","Eduardo"]
    
    imprimir_nombres(nombres)
    
    for i in range(constantes.MAX):
        saludar(nombres[i])
    
    print("Menu")
    op = 1
    while op != 0:
        op= int(input("Ingrese opcion: "))
        if op == 1:
            saludar(nombre_saludar)
            #saludar_mal_definida()
        elif op == 2:
            print("Resultado: ", funciones.suma(3,5))
        elif op == 3:
            funciones.contar_hasta()
    print("Saludos")
    
if __name__ == '__main__':
    main()
