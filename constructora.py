# Ejercicio constructora
import random

ESTADO_LIBRE= 0

class Departamento:
    def __init__(self, numero, descripcion, m2, estado, precio):
        self.numero = numero
        self.descripcion= descripcion
        self.m2= m2
        self.estado= estado
        self.precio= precio
    def __repr__(self):
        return self.descripcion

class ValMinMaxError(Exception):
    pass


def validar_valor(valor, valmin, valmax):
    if valor < valmin:
        raise ValMinMaxError
    if valor > valmax:
        raise ValMinMaxError


def ingresar_numero(mensaje, valmin, valmax, msgerror):
    while True:
        try:
            valor = int(input(mensaje))
            validar_valor(valor,valmin,valmax)
            return valor
        except ValueError:
            print("Debe ingresar un número")
        except ValMinMaxError:
            print(msgerror)


def main():
    departamentos= []
    op = 1
    while op != 0:
        op = menu()
        if op == 1:
            cargar_departamentos(departamentos)
        elif op == 2:
            guardar_departamentos(departamentos)
        elif op == 3:
            listado_dptos_libres(departamentos)
        elif op == 6:
            generar_csv_prueba()


def menu():
    print("1-Cargar")
    print("2-Guardar")
    print("3-Listado departamentos libres")
    print("4-Departamentos por Estado")
    print("5-Marcar como reservado")
    print("6-Generar datos de prueba")
    print("0-Salir")
    return ingresar_numero("Ingrese una opcion: ", 0, 6, "Ingrese un número entre 0 y 5")


def cargar_departamentos(departamentos):
    with open('deptos.csv', 'r') as arch:
        for linea in arch:
            l = linea[:-1].split(';')
            departamentos.append(Departamento(int(l[0]), l[1], int(l[2]), int(l[3]), float(l[4])))


def guardar_departamentos(departamentos):
    with open('deptos.csv', 'w', encoding='utf-8') as arch:
        for i in range(0, len(departamentos)):
            arch.write(get_departamento_como_csv(departamentos[i]))


def get_departamento_como_csv(dpto: Departamento):
    return "{0};{1};{2};{3};{4}\n".format(dpto.numero, dpto.descripcion, dpto.m2, dpto.estado, dpto.precio)


def listado_dptos_libres(departamentos):
    libres = obtener_deptos_libres(departamentos)
    ordenar(libres, "descripcion")
    generar_reporte_libres(libres)


def generar_reporte_libres(libres):
    with open('reporte_libres.txt', 'w', encoding='utf-8') as rpt:
        for d in libres:
            rpt.write("{0} - {1}\n".format(d.numero, d.descripcion))

def obtener_deptos_libres(deptos):
    lista = []

    for dpto in deptos:
        if dpto.estado == ESTADO_LIBRE:
            lista.append(dpto)

    return lista


def ordenar(lista, campo):
    for j in range(0,len(lista) - 1):
        for i in range(0,len(lista) - 1):
            if getattr(lista[i], campo) > getattr(lista[i + 1], campo):
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux


def generar_csv_prueba():
    lista = []
    for i in range(0, 10):
        lista.append(Departamento(i, "Dpto " + str(i), random.randint(40, 300), random.randint(0,3), random.randint(50000,100000)))
    guardar_departamentos(lista)

if __name__ == '__main__':
    main()