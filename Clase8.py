# Clase 8 - Archivos
"""
open('./datos/nombre_archivo', 'modo', encoding='utf-8')
modo:
r -> solo lectura
w -> escritura, si existe lo borra
a -> agregar, agrega al final del archivo
r+ -> abre para lectura y escritura, si existe no lo borra
"""
PROV_BUENOS_AIRES = "06"
PROV_TUCUMAN = "90"
PROV_CORDOBA = "14"

class Alumno:
    def __init__(self, dni_alumno, apellido_alumno, nombre_alumno, provincia_examen,
                id_provincia, localidad, sede_nombre, sede_direccion, llamado_certificacion):
        self.dni= dni_alumno
        self.apellido= apellido_alumno
        self.nombre = nombre_alumno
        self.provincia= provincia_examen
        self.idProvincia= id_provincia
        self.localidad= localidad
        self.sede= sede_nombre
        self.direccion= sede_direccion
        self.llamado= llamado_certificacion
    def __repr__(self):
        return "{0} - {1}, {2} - {3} - {4}".format(self.dni, self.apellido, self.nombre,
            self.provincia, self.localidad)



def main():
    # leer un archivo completo
    datos = ""
    with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
        datos = archivo.read()
    
    print("=" * 10)
    print(datos)
    print("=" * 10)

    # leer una linea
    with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
        linea1 = archivo.readline()
        print(linea1, end="")
        linea2 = archivo.readline()
        print(linea2, end="")
        print(linea1[:-1])

    print("=" * 10)

    # leer linea a linea
    with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
        for linea in archivo:
            print(linea, end="")

    print("=" * 10)

    # leer linea a linea y agregar a lista
    lista = []
    with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
        for linea in archivo:
            lista.append(linea)

    print(lista)
    print("=" * 10)

    #crear una lista con las lineas
    lista = []
    with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
        lista = list(archivo)

    print(lista)
    print("=" * 10)

    #escribir en un archivo
    with open('miArchivo2.txt', 'w', encoding="utf-8") as archivo:
        archivo.write("Esto es un texto de prueba.\nEsta es una segunda linea.")
        archivo.write("Esto sigue en la segunda linea.")
        archivo.write("\nTercera linea.")


    #Leer un archivo CSV

    lista = []
    nombre_archivo = 'personas-certificadas.csv'
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo_csv:
        primera_linea = True
        for linea in archivo_csv:
            if primera_linea == True:
                primera_linea = False
                continue
            
            a = linea.split(',')
            #print("DNI: " + valumno[0])
            #print("Nombre Completo: " + valumno[2] + " " + valumno[1])
            lista.append(Alumno(int(a[0]),a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]))

    for i in range(0,11):
        print(lista[i])
    
    cant_prov_baires = 0
    cant_total = 0
    cant_prov_tucuman = 0
    for i in range(1,len(lista)):
        cant_total += 1
        if (lista[i].idProvincia == PROV_BUENOS_AIRES):
            cant_prov_baires += 1
        elif (lista[i].idProvincia == PROV_TUCUMAN):
            cant_prov_tucuman += 1
    c_total = "Cant. Total "
    str_total = str(cant_total)

    print(c_total + str(cant_total))
    print("Cant. Prov. BA ", cant_prov_baires)
    print("Cant. Prov. Tucuman ", cant_prov_tucuman)


    with open('personas-certificadas-cordoba.csv', 'w', encoding="utf-8") as csv:
        csv.write("{0}|{1}|{2}\n".format(lista[0].dni, lista[0].apellido, lista[0].nombre))
        for i in range(1,len(lista)):
            if lista[i].idProvincia == PROV_CORDOBA:
                csv.write("{0}|{1}|{2}\n".format(lista[i].dni, lista[i].apellido, lista[i].nombre))

    with open('personas-certificadas-ba.csv', 'w', encoding="utf-8") as csv:
        csv.write("{0}|{1}|{2}\n".format(lista[0].dni, lista[0].apellido, lista[0].nombre))
        for i in range(1,len(lista)):
            if lista[i].idProvincia == PROV_BUENOS_AIRES:
                csv.write("{0}|{1}|{2}\n".format(lista[i].dni, lista[i].apellido, lista[i].nombre))


if __name__ == "__main__":
    main()