# Simulacro 1er Parcial
SOFTWARE= 4

class ErrorValMinMax(Exception):
    pass


def ejercicio_1():
    numero = ingresar_numero("Ingrese un número del 1 al 10: ", 1, 10, "Debe ingresar un número del 1 al 10")
    print("Numero ingresado: ", numero)


def ingresar_numero(mensaje, valmin, valmax, msgerror):
    while True:
        try:
            ingreso = int(input(mensaje))
            if ingreso < valmin:
                raise ErrorValMinMax
            if ingreso > valmax:
                raise ErrorValMinMax
            return ingreso
        except ValueError:
            print("Debe ingresar un número")
        except ErrorValMinMax:
            print(msgerror)


def ejercicio_2():
    temperaturas = [[10,14,20,16,23,25,25],[14,14,12,8,24,23,26],[4,8,8,2,27,23,23],[1,8,12,12,12,23,23]]
    informar_momento_mayor_temperatura(temperaturas)


def informar_momento_mayor_temperatura(temperaturas):
    maxfil= 0
    maxcol= 0
    for fila in range(0, len(temperaturas)):
        for columna in range(0, len(temperaturas[0])):
            if temperaturas[fila][columna] > temperaturas[maxfil][maxcol]:
                maxfil= fila
                maxcol= columna

    print("Día de mayor temperatura: ", convertir_dia_texto(maxcol))
    print("Periodo de mayor temperatura: ", convertir_periodo_texto(maxfil))


def convertir_dia_texto(dia):
    if dia == 0:
        return "Domingo"
    elif dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miercoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sabado"
    else:
        raise ValueError


def convertir_periodo_texto(periodo):
    periodos = ["Mañana", "Medio Día", "Tarde", "Noche"]
    return periodos[periodo]


def ejercicio_3():
    nombres = ["Juan Perez", "Carlos Gonzalez", "Sergio Fernandez", "Alberto Perez", "Juan Fernandez"]
    edades = [23, 25, 19, 20, 22]
    carreras = [1,4,4,4,1]
    aprobadas = [5,20,11,1,2]

    #mostrar_alumnos_mas10materias(SOFTWARE,nombres,carreras,aprobadas)

    #mostrar_alumnos_ordenado(nombres)

    promedio_alumnos_edad_por_carrera(edades, carreras)


def mostrar_alumnos_mas10materias(carrera, nombres,carreras,aprobadas):
    for i in range(0, len(nombres)):
        if carreras[i] == carrera and aprobadas[i] > 10:
            print(convertir_apellido_nombre(nombres[i]))


def convertir_apellido_nombre(nombre_apellido):
    nombre = nombre_apellido.split(' ')
    return "{0}, {1}".format(nombre[1], nombre[0])


def mostrar_alumnos_ordenado(nombres):
    nombres_ordenado = ordenar_por_apellido(nombres)
    for nombre in nombres_ordenado:
        print(nombre)

def ordenar_por_apellido(nombres):
    apellidos_nombres = []

    for nombre_apellido in nombres:
        apellidos_nombres.append(convertir_apellido_nombre(nombre_apellido))

    # ordenar_vector(apellidos_nombres)
    # return apellidos_nombres

    return devolver_vector_ordenado(apellidos_nombres)


def ordenar_vector(vector):
    for j in range(0, len(vector) - 1):
        for i in range(0, len(vector) - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux


def devolver_vector_ordenado(a_ordenar):
    vector = a_ordenar.copy()
    for j in range(0, len(vector) - 1):
        for i in range(0, len(vector) - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux
    return vector


def promedio_alumnos_edad_por_carrera(edades,carreras):
    texto_carreras = ["", "Contador", "Abogado", "Administracion", "Software"]
    for i in range(1, 5):
        print(texto_carreras[i])
        mostrar_promedios_carrera(i, edades, carreras)


def mostrar_promedios_carrera(carrera, edades, carreras):
    cantidad = 0
    edad = 0
    for i in range(0, len(carreras)):
        if carreras[i] == carrera:
            cantidad = cantidad + 1
            edad = edad + edades[i]

    print("Cantidad alumnos: ", cantidad)
    if cantidad > 0:
        print("Promedio Edad: ", edad // cantidad)

def main():
    #ejercicio_1()
    #ejercicio_2()
    ejercicio_3()



if __name__ == '__main__':
    main()
